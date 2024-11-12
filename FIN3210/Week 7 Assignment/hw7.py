import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# Generate concatenated csv files for each cryptocurrency
# btcfiles = glob.glob('Bitcoin/*.csv')
# count = 0
# for file in btcfiles:
#     df = pd.read_csv(file, sep = ';')
#     if count == 0:
#         result = df
#     else:
#         result = pd.concat([result, df])
#     count += 1
# result.sort_values(by = 'timeOpen', inplace = True)
# result.to_csv('Bitcoin.csv', index = False)

# ethfiles = glob.glob('Ethereum/*.csv')
# count = 0
# for file in ethfiles:
#     df = pd.read_csv(file, sep = ';')
#     if count == 0:
#         result = df
#     else:
#         result = pd.concat([result, df])
#     count += 1
# result.sort_values(by = 'timeOpen', inplace = True)
# result.to_csv('Ethereum.csv', index = False)

btc = pd.read_csv('Bitcoin.csv')
eth = pd.read_csv('Ethereum.csv')

plt.figure(figsize = (10, 8))
plt.plot(pd.to_datetime(btc['timeOpen']).dt.strftime('%Y-%m-%d'), btc['close'])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.xticks(rotation = 45)
x_major_locator=MultipleLocator(150)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.gcf().subplots_adjust(bottom=0.15)
plt.title('Bitcoin Closing Price')
plt.show()

plt.figure(figsize = (10, 8))
plt.plot(pd.to_datetime(eth['timeOpen']).dt.strftime('%Y-%m-%d'), eth['close'])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.xticks(rotation = 45)
x_major_locator=MultipleLocator(150)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.gcf().subplots_adjust(bottom=0.15)
plt.title('Ethereum Closing Price')
plt.show()
