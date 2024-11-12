import pandas as pd
import numpy as np
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import time
import warnings
warnings.filterwarnings("ignore")
import statsmodels.api as sm


def extract_trends(wordlist, location):
    """
    Extract the google trends data of the given word list
    :param wordlist: list of words
    :return: pandas dataframe
    """
    count = 0
    for i in range(0, len(wordlist), 5):
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=wordlist[i:i+5], timeframe='2018-9-1 2023-8-31', geo = location)
        py_res = pytrend.interest_over_time().reset_index()
        if count == 0:
            print(py_res)
            py_res.drop(columns=['isPartial'], axis=1, inplace=True)
            res = py_res
        else:
            py_res.drop(columns=['isPartial', 'date'], axis=1, inplace=True)
            res = pd.concat([res, py_res], axis=1)
        count += 1
        time.sleep(120)
    return res

# Q1
us_china_keywords = [
    "Tariffs",
    "South China Sea",
    "Huawei",
    "Trade War",
    "Made in China",
    "Tibet",
    "Hong Kong",
    "Taiwan",
    "U.S.-China",
    "5G"
]

res = extract_trends(us_china_keywords, 'US')
print(res)
res.to_csv('us_china.csv', index=False)

origin_index = pd.read_csv('us_china.csv')
origin_index.drop(['U.S.-China'], axis=1, inplace=True)
index_list = origin_index.columns.tolist()[1:]
origin_index['total_index'] = origin_index[index_list].mean(axis=1)
corr_data = origin_index.drop(columns=['date','total_index'], axis=1)
print(corr_data.corr())

plt.figure(figsize=(10, 5))
plt.plot(origin_index['date'], origin_index['total_index'])
plt.title('US-China Political Relations')
plt.xlabel('Date')
plt.ylabel('Google Trends Index')
x_major_locator=MultipleLocator(35)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.show()

# Q2
positive_words_list = ['boom', 'buy', 'credit', 'gain', 'profit', 'reward', 'surge', 'rise', 'boost', 'win']
negative_words_list = ['bankrupt', 'capital', 'decline', 'default', 'fall', 'inflation', 'liability', 'loss', 'recession', 'short']

pos_result = extract_trends(positive_words_list, 'CN')
pos_result.to_csv('positive_words.csv', index=False)
neg_result = extract_trends(negative_words_list, 'CN')
neg_result.to_csv('negative_words.csv', index=False)

pos_result = pd.read_csv('positive_words.csv')
neg_result = pd.read_csv('negative_words.csv')

pos_result['pos_total_index'] = pos_result[positive_words_list].mean(axis=1)
neg_result['neg_total_index'] = neg_result[negative_words_list].mean(axis=1)
neg_result.drop(['date'], axis=1, inplace=True)
result = pd.concat([pos_result, neg_result], axis=1)
result['total_index'] = result['pos_total_index'] - result['neg_total_index']
result['y_w'] = pd.to_datetime(result['date']).dt.strftime('%Y-%U')

ret_data = pd.read_csv('return.csv')
ret_data['Idxtrd08'] = ret_data['Idxtrd08']/100
ret_data['year_week'] = pd.to_datetime(ret_data['Idxtrd01']).dt.strftime('%Y-%U')
ret_data['cum_ret'] = 1 + ret_data['Idxtrd08']
ret_idx = ret_data.groupby('year_week').agg({'cum_ret': np.prod}).reset_index()
ret_idx['week_ret'] = ret_idx['cum_ret'] - 1

reg_data = pd.merge(result, ret_idx, left_on='y_w', right_on='year_week', how='left')
reg_data = reg_data[['year_week', 'total_index', 'week_ret']]
reg_data['week_ret'] = reg_data['week_ret'].shift(1)
reg_data.dropna(inplace=True)
X = reg_data['total_index']
y = reg_data['week_ret']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

plt.figure(figsize=(10, 5))
plt.plot(pos_result['date'], pos_result['total_index'], label='Positive')
plt.plot(neg_result['date'], neg_result['total_index'], label='Negative')
plt.title('Chinese Economy')
plt.xlabel('Date')
plt.ylabel('Google Trends Index')
plt.legend()
x_major_locator=MultipleLocator(35)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.show()

