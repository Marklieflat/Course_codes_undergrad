import pandas as pd
from sklearn.linear_model import Ridge
from metrics import mase, pearson_correlation, theil_u
import sqlite3
import statsmodels.api as sm
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

def code_str(df):
    df['code'] = df['code'].astype(str)
    df['code'] = df['code'].str.zfill(6)
    df['code'] = df['code'].astype(object)
    return df

def metrics(data, name_real, name_pred):
    metrics = {}
    for code in data.index.get_level_values('code').unique():
        code_data = data[data.index.get_level_values('code') == code]
        real = code_data[name_real]
        pred = code_data[name_pred]
        mase_value = mase(real, pred)
        pearson_corr = pearson_correlation(real, pred)
        theil_u_stat = theil_u(real, pred)
        metrics[code] = [mase_value, pearson_corr, theil_u_stat]
    metrics_df = pd.DataFrame(metrics, index=['mase', 'pearson_corr', 'theil_u_stat']).T
    return metrics_df

conn = sqlite3.connect("data.db")
df = pd.read_sql_query("SELECT * FROM top_10", conn)
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# Q1 model: rm-rf, SMB, HML, and fixed effects
X1 = df[['code', 'date', 'rm-rf', 'SMB', 'HML', 'GDPGrowth', 'totalConsumptionLevel', 'Ind_1',
         'Ind_2', 'Ind_3','Ind_4', 'Ind_5']]
X1 = sm.add_constant(X1)

# Q2 model: rm-rf, SMB, HML, and fixed effects, and additional factors
X2 = df[['code', 'date', 'rm-rf', 'SMB', 'HML', 'GDPGrowth', 'totalConsumptionLevel', 'Ind_1',
         'Ind_2', 'Ind_3', 'Ind_4', 'Ind_5', 'B/M', 'roe_ttm', 'roa_ttm',
         'current_ratio', 'PB', 'PE', 'PCF', 'DivYield', 'PS', 'NPM/CA', 'operatingMargin',
         'liquidityRatio', 'cashRatio', 'LTDebt/E', 'turnover', 'BIAS', 'CCI',
         'EMV', 'MA10', 'MA20', 'MACD', 'MTM6', 'MTM12', 'RSI', 'TRIX', 'VOSC', 'VRSI', 'VWAP']]
X2 = sm.add_constant(X2)

y = df[['code', 'date', 'excess_ret']]

# split by timestamp, for each stock code, the first 1500 rows are training set, the rest are test set
X1_train = X1.groupby('code').head(1500)
X1_test = X1.drop(X1_train.index)
X2_train = X2.groupby('code').head(1500)
X2_test = X2.drop(X2_train.index)
y_train = y.groupby('code').head(1500)
y_test = y.drop(y_train.index)

# set 'code', 'date' as index
df.set_index(['code', 'date'], inplace=True)
X1_train.set_index(['code', 'date'], inplace=True)
X1_test.set_index(['code', 'date'], inplace=True)
X2_train.set_index(['code', 'date'], inplace=True)
X2_test.set_index(['code', 'date'], inplace=True)
y_train.set_index(['code', 'date'], inplace=True)
y_test.set_index(['code', 'date'], inplace=True)

# Q1 model(clustered OLS regression)
model1 = sm.OLS(y_train, X1_train).fit(cov_type='cluster', cov_kwds={'groups': df.loc[X1_train.index, 'year']})
y_pred1 = model1.predict(X1_test)
y_pred1 = pd.DataFrame(y_pred1, index=y_test.index, columns=['pred1'])

# Q2 model (ridge regression)
ridge_reg = Ridge(alpha=0.5)
ridge_reg.fit(X2_train, y_train)
y_pred2 = ridge_reg.predict(X2_test)
mase_value2 = mase(y_test, y_pred2)
pearson_corr2 = pearson_correlation(y_test, y_pred2)
theil_u_stat2 = theil_u(y_test, y_pred2)
# assign y_pred2 index the same as y_test
y_pred2 = pd.DataFrame(y_pred2, index=y_test.index, columns=['pred2'])

# load the deep learning result file
df_dl = pd.read_csv('/Users/bhchen/Desktop/FIN3210/project/LSTM_result_merged.csv')
df_dl['date'] = pd.to_datetime(df_dl['date'])
df_dl = code_str(df_dl) 
df_dl.set_index(['code', 'date'], inplace=True)
df_dl.columns = ['cum_ret3', 'real']

y_pred = df_dl.copy()

df['r_f'] = df['r_f'].astype(float)
tmp = pd.merge(y_pred1, y_pred2, how='left', on=['code', 'date'])
tmp = pd.merge(tmp, y_test, how='left', on=['code', 'date'])
tmp.columns = ['pred1', 'pred2', 'real']
tmp = pd.merge(tmp, df[['r_f']], how='left', on=['code', 'date'])
tmp['pred1'] = tmp['pred1'] + tmp['r_f']
tmp['pred2'] = tmp['pred2'] + tmp['r_f']
tmp['real'] = tmp['real'] + tmp['r_f']
tmp.drop(columns=['r_f'], inplace=True)
tmp['cum_ret1'] = tmp['pred1'].groupby('code').cumsum()
tmp['cum_ret2'] = tmp['pred2'].groupby('code').cumsum()
tmp['cum_ret_real'] = tmp['real'].groupby('code').cumsum()
y_pred = pd.merge(y_pred, tmp, how='left', on=['code', 'date'])

normalized_data = {}
inverse_normalized_data = {}

for code in y_pred.index.get_level_values('code').unique():
    code_data = y_pred[y_pred.index.get_level_values('code') == code]
    mean1 = code_data['real_x'].mean()
    std1 = code_data['real_x'].std()
    mean2 = code_data['cum_ret_real'].mean()
    std2 = code_data['cum_ret_real'].std()

    code_data['normalized_pred'] = (code_data['cum_ret3'] - mean1) / std1
    code_data['normalized_actual'] = (code_data['real_x'] - mean1) / std1

    code_data['inverse_normalized_pred'] = code_data['normalized_pred'] * std2 + mean2
    code_data['inverse_normalized_actual'] = code_data['normalized_actual'] * std2 + mean2

    normalized_data[code] = code_data[['normalized_pred', 'normalized_actual']]
    inverse_normalized_data[code] = code_data[['inverse_normalized_pred', 'inverse_normalized_actual']]

normalized_df = pd.concat(normalized_data)
inverse_normalized_df = pd.concat(inverse_normalized_data)
normalized_df.index = normalized_df.index.droplevel(0)
inverse_normalized_df.index = inverse_normalized_df.index.droplevel(0)
y_pred['cum_ret3'] = inverse_normalized_df['inverse_normalized_pred']
y_pred['invNorm_actual'] = inverse_normalized_df['inverse_normalized_actual']

y_pred.drop(columns=['real_x'], inplace=True)
y_pred.rename(columns={'real_y': 'real'}, inplace=True)
y_pred['pred3'] = y_pred['cum_ret3'].groupby('code').diff()
y_pred.dropna(inplace=True)

# chaneg the order
y_pred = y_pred[['real', 'pred1', 'pred2', 'pred3', 'cum_ret_real', 'cum_ret1', 'cum_ret2', 'cum_ret3', 'invNorm_actual']]
print(y_pred)
y_pred.to_csv('threeModelOutput.csv')

print('------------------Q1 model-------------------')
print(metrics(y_pred, 'real', 'pred1'))
print(metrics(y_pred, 'real', 'pred1').mean())
print('---------------------------------------------')
print('------------------Q2 model-------------------')
print(metrics(y_pred, 'real', 'pred2'))
print(metrics(y_pred, 'real', 'pred2').mean())
print('---------------------------------------------')
print('------------------Q3 model-------------------')
print(metrics(y_pred, 'real', 'pred3'))
print(metrics(y_pred, 'real', 'pred3').mean())  
print('---------------------------------------------')


# draw the plot for 10 graphs
unique_codes = df.index.get_level_values('code').unique()

n_subplots = 10
n_rows = 5
n_cols = 2
fig, axes = plt.subplots(n_rows, n_cols, figsize=(14*n_cols, 7*n_rows))
for idx, code in enumerate(unique_codes):
    test_indices = y_pred.index.get_level_values('code') == code
    
    # Get the actual and predicted values
    # Plan A: cumulative return
    actual_values = y_pred[test_indices]['cum_ret_real']
    predicted_values1 = y_pred[test_indices]['cum_ret1']
    predicted_values2 = y_pred[test_indices]['cum_ret2']
    predicted_values3 = y_pred[test_indices]['cum_ret3']

    # # Plan B: return
    # actual_values = y_pred[test_indices]['real']
    # predicted_values1 = y_pred[test_indices]['pred1']
    # predicted_values2 = y_pred[test_indices]['pred2']
    # predicted_values3 = y_pred[test_indices]['pred3']

    row = idx // n_cols
    col = idx % n_cols
    ax = axes[row, col]    

    ax.plot(actual_values.index.get_level_values('date'), actual_values, color='red', label='Actual')
    ax.plot(predicted_values1.index.get_level_values('date'), predicted_values1, color='green', label='Baseline')
    ax.plot(predicted_values2.index.get_level_values('date'), predicted_values2, color='blue', label='Ridge')
    ax.plot(predicted_values3.index.get_level_values('date'), predicted_values3, color='orange', label='WSAE-LSTM')

    ax.set_title(f'Actual vs Predicted for stock code {code}')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cumulative Return')
    ax.legend()

plt.tight_layout()
plt.savefig('10Graphs.png')
plt.show()