import numpy as np
import pandas as pd
import sqlite3
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler

conn = sqlite3.connect("data.db")

df = pd.read_sql_query("SELECT * FROM data_total", conn)
df_price_factor = pd.read_sql_query("SELECT * FROM price_related_factors", conn)
df_fama = pd.read_sql_query("SELECT * FROM ff_3", conn)

# keep the data from 2016 to 2022
df = df[df['date'] >= '2016-01-01']
df = df[df['date'] <= '2022-12-31']

# create a map for original column name and new column name
col_map = {}

col_map['FI_T5-F050504C'] = 'roe_ttm'
col_map['FI_T5-F050204C'] = 'roa_ttm'
col_map['FI_T10-F101001A'] = 'current_ratio'
col_map['STK_MKT_DALYR-PB'] = 'PB'
col_map['STK_MKT_DALYR-PE'] = 'PE'
col_map['STK_MKT_DALYR-PCF'] = 'PCF'
col_map['STK_MKT_DALYR-Ret'] = 'DivYield'
col_map['STK_MKT_DALYR-PS'] = 'PS'
col_map['FI_T5-F050304C'] = 'NPM/CA' # Net profit margin on current assets
col_map['FI_T5-F051401C'] = 'operatingMargin'
col_map['FI_T1-F010101A'] = 'liquidityRatio'
col_map['FI_T1-F010401A'] = 'cashRatio'  
col_map['FI_T1-F012001A'] = 'LTDebt/E'
col_map['CME_Qqgdp-Gdpcurrperiod'] = 'GDPGrowth'
col_map['CME_Consmp1-Ec0101'] = 'totalConsumptionLevel'

# the name of the factors, which need to be normalized
# to store the factor name, including B/M, industry dummies, year dummies, 
# the values of col_map, InflationRate_1, and InflationRate_2
factor_to_norm = ['code', 'date', 'B/M', 'InflationRate_1', 'InflationRate_2']
factor_to_norm.extend(col_map.values())
factor_to_norm.remove('GDPGrowth')
factor_to_norm.remove('totalConsumptionLevel')

# the name of the factors, which does not need to be normalized
factor_raw = ['code', 'date', 'GDPGrowth', 'totalConsumptionLevel', 'Ind_1',
              'Ind_2', 'Ind_3', 'Ind_4', 'Ind_5', 'year_2016','year_2017',
              'year_2018', 'year_2019', 'year_2020', 'year_2021']

# If column name is in df, and is also in col_map, change it into new name
for col in df.columns:
    if col in col_map.keys():
        df.rename(columns={col: col_map[col]}, inplace=True)

def reverse_normalize(factor_series):
    non_na_series = factor_series.fillna(method='ffill')
    # Adjusted percentile calculation to avoid 0 and 1
    percentile_values = (non_na_series.rank() - 0.5) / len(non_na_series)
    # Map to standard normal distribution quantiles
    normalized_values = norm.ppf(percentile_values)
    result_series = pd.Series(np.nan, index=factor_series.index)
    result_series[non_na_series.index] = normalized_values
    return result_series

# Based on the daily data, calculate the daily value of 
# the factor exposure for each factor
def get_factor_exposure(df_factors, factors_name):
    result = df_factors.copy()
    for col in factors_name:
        result[col] = result.groupby('date')[col].apply(lambda x: reverse_normalize(x))
    return result

# print(df_fama.columns)
df_model1 = df_fama[['code', 'date', 'ret', 'r_f', 'r_m', 'excess_ret', 'total_MV', 'SMB', 'HML']].copy()
df_model1 = pd.merge(df_model1, df[factor_raw], how='left', on=['code', 'date'])
df_model1 = pd.merge(df_model1, df[factor_to_norm], how='left', on=['code', 'date'])

# concatenate the price related factors by date and code
df_model1 = pd.merge(df_model1, df_price_factor, how='left', on=['code', 'date'])
df_model1.fillna(method='ffill', inplace=True)
df_model1 = df_model1.groupby('code').filter(lambda x: len(x) == 1703)

# add df_price_factor.columns except the first and last column
fac_names = factor_to_norm[2:]
fac_names.extend(df_price_factor.columns[8:])
df_exposure = get_factor_exposure(df_model1, fac_names)

df_model1.to_sql('df_model_1703', conn, if_exists = "replace", index=False)
df_exposure.to_sql('df_model_exp_1703', conn, if_exists = "replace", index=False)

tmp = df_exposure[['code', 'date', 'total_MV']].copy()
tmp['date'] = pd.to_datetime(tmp['date'])
tmp.sort_values(by=['date', 'total_MV'], ascending=[True, False], inplace=True)
# Rank the stocks for each date
tmp['rank'] = tmp.groupby('date')['total_MV'].rank(ascending=False)
pivot_table = tmp.pivot_table(index='date', columns='code', values='rank')

# Calculate weights for the ranks based on recency (more recent dates get higher weights), here I used a linearly increasing weight
max_date = tmp['date'].max()
pivot_table['weights'] = (pivot_table.index - pivot_table.index.min()) / (max_date - pivot_table.index.min())
pivot_table['weights'] = pivot_table['weights'] + 1  # So that the earliest date has a weight of 1

# Apply weights to the ranks
for col in pivot_table.columns:
    if col != 'weights':
        pivot_table[col] = pivot_table[col] * pivot_table['weights']

pivot_table.drop(columns=['weights'], inplace=True)
sum_weighted_ranks = pivot_table.sum().sort_values(ascending=False)

# get the top 10 stocks
top_10_stocks  = sum_weighted_ranks.head(10).index.tolist()
print(top_10_stocks)

df_selected = df_exposure[df_exposure['code'].isin(top_10_stocks)]

df_selected['rm-rf'] = df_selected['r_m']-df_selected['r_f']
# take the logarithm of totalConsumptionLevel
df_selected['totalConsumptionLevel'] = df_selected['totalConsumptionLevel'].apply(lambda x: np.log(x))

columns_to_normalize = ['totalConsumptionLevel', 'GDPGrowth','open','high','low','close','volume']

def normalize_group(group):
    scaler = StandardScaler()
    for column in columns_to_normalize:
       group[column] = scaler.fit_transform(group[column].values.reshape(-1, 1))
    return group

# Applying the function to each group
df_selected = df_selected.groupby('code').apply(normalize_group)

df_selected.to_sql('top_10', conn, if_exists = "replace", index=False)
conn.close()