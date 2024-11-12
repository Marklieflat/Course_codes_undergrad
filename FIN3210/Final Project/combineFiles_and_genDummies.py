import numpy as np
import pandas as pd
import sqlite3
from scipy.stats import norm

conn = sqlite3.connect("data.db")

def code_str(df):
    df['code'] = df['code'].astype(str)
    df['code'] = df['code'].str.zfill(6)
    df['code'] = df['code'].astype(object)
    return df

df_stocks = [
    pd.read_csv("/Users/bhchen/Desktop/FIN3210/project/data source/combine/15-17/跨表查询.csv"),
    pd.read_csv("/Users/bhchen/Desktop/FIN3210/project/data source/combine/18-20/跨表查询.csv"),
    pd.read_csv("/Users/bhchen/Desktop/FIN3210/project/data source/combine/21-22/跨表查询.csv")
]
# a file contains the inflation rate of each year for different countries
df_inflation = pd.read_csv("/Users/bhchen/Desktop/FIN3210/project/data source/inflation/OBOR_INFLATIONRATEY.csv")
# a file contains the market return of each day
df_market = pd.read_csv("/Users/bhchen/Desktop/FIN3210/project/data source/market/TRD_Cndalym.csv")
# a file contains the book value of each stock
df_book_value = pd.read_csv("/Users/bhchen/Desktop/FIN3210/project/data source/book value/FS_Combas.csv")

merged_df_stocks = pd.concat(df_stocks, axis=0)
merged_df_stocks = merged_df_stocks.sort_values(by=['code', 'TRD_Nrrate-Clsdt'])
merged_df_stocks['date'] = pd.to_datetime(merged_df_stocks['TRD_Nrrate-Clsdt'])
merged_df_stocks = code_str(merged_df_stocks)

# List of columns obtained from financial statements (quarter data)
columns_to_fill = ['FI_T5-Typrep', 'FI_T5-F050504C', 'FI_T5-F050204C', 'FI_T5-F050304C', 'FI_T5-F051401C',
                   'FI_T1-Typrep', 'FI_T1-F010101A', 'FI_T1-Accper', 'FI_T1-F010401A', 'FI_T1-F012001A','FI_T10-F101001A']

merged_df_stocks['FI_T10-Accper'] = pd.to_datetime(merged_df_stocks['FI_T10-Accper'])
merged_df_stocks[columns_to_fill] = merged_df_stocks.groupby(['code', 'CME_Qqgdp-Quarter'])[columns_to_fill].fillna(method='bfill')

# only CountryCode == CHN
df_inflation = df_inflation[df_inflation['CountryCode'] == 'CHN']
df_inflation = df_inflation.iloc[:, [1, 2, 4, 5]]
# group by year, keep the last value of each year
df_inflation = df_inflation.groupby('SgnYear').tail(1)
# InflationRate_1: 按GDP平减指数衡量的年通胀率(%); InflationRate_2: 按消费者价格指数(CPI)衡量的年通胀率(%)
df_inflation.columns = ['Year', 'CountryCode', 'InflationRate_1', 'InflationRate_2']
df_inflation.Year = df_inflation.Year.astype(object)

# only df_market['Markettype'] == 63, 沪深AB股和创业板和科创板
df_market = df_market[df_market['Markettype'] == 63]

# r_m_eqW:考虑现金红利再投资的综合日市场回报率(等权平均法); 
# r_m_weightedByMV: 考虑现金红利再投资的综合日市场回报率(流通市值加权平均法)
df_market.columns = ['MarketType', 'date', 'r_m_eqW', 'r_m_weightedByMV']
df_market['date'] = pd.to_datetime(df_market['date'])

df_book_value['Accper'] = pd.to_datetime(df_book_value['Accper'])
df_book_value = df_book_value[df_book_value['Typrep'] == 'A']
df_book_value['BookValue'] = df_book_value['A001000000'] - df_book_value['A002000000']
df_book_value = df_book_value[['Stkcd', 'Accper', 'BookValue']]
df_book_value.columns = ['code', 'date', 'BookValue']
df_book_value = code_str(df_book_value)
# delete the date end with 01-01
df_book_value = df_book_value[~df_book_value['date'].dt.strftime('%m-%d').isin(['01-01'])]

merged_df_stocks = pd.merge(merged_df_stocks, df_book_value, how='left', on=['code', 'date'])
# fillna with the last value of each stock
merged_df_stocks['BookValue'] = merged_df_stocks.groupby('code')['BookValue'].fillna(method='bfill')
# combine df_market to merged_df_stocks by daily date
merged_df_stocks['Year'] = merged_df_stocks['date'].dt.year
# combine df_inflation to merged_df_stocks by year
merged_df_stocks['Year'] = merged_df_stocks['Year'].astype(object)
merged_df_stocks = pd.merge(merged_df_stocks, df_market, how='left', on='date')
merged_df_stocks = pd.merge(merged_df_stocks, df_inflation, how='left', on='Year')
merged_df_stocks.drop(columns=['Year'], inplace=True)
# delete the rows if the date is not trading date, TRD_Dalyr-Trddt is the trading date
merged_df_stocks = merged_df_stocks[merged_df_stocks['TRD_Dalyr-Trddt'].notna()]
merged_df_stocks['B/M'] = merged_df_stocks['BookValue'] / merged_df_stocks['TRD_Dalyr-Dsmvtll']

# TRD_Co-Indcd[行业代码A] - 1=金融，2=公用事业，3=房地产，4=综合，5=工业，6=商业
industry_dummies = pd.get_dummies(merged_df_stocks['TRD_Co-Indcd'], prefix='Ind')
industry_dummies = industry_dummies.iloc[:, :-1]

merged_df_stocks['year'] = pd.to_datetime(merged_df_stocks['date']).dt.year
year_dummies = pd.get_dummies(merged_df_stocks['year'], prefix='year')
merged_df_stocks.drop(columns=['year'], inplace=True)
year_dummies = year_dummies.iloc[:, 1:-1] # delete the first（2015） and last year（2022）
merged_df_stocks = pd.concat([merged_df_stocks, industry_dummies, year_dummies], axis=1)

# store the data to database
merged_df_stocks.to_sql('data_total', conn, if_exists = "replace", index=False)
df_inflation.to_sql('inflation', conn, if_exists = "replace", index=False)
df_market.to_sql('market', conn, if_exists = "replace", index=False)

conn.close()