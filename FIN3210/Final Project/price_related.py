from BIAS import calculate_BIAS
from boll import calculate_boll
from CCI import calculate_CCI
from EMV import calculate_EMV
from MA import calculate_MA
from MACD import calculate_MACD
from MTM import calculate_MTM 
from RSI import calculate_RSI
from TRIX import calculate_TRIX
from VOSC import calculate_VOSC
from VRSI import calculate_VRSI
from VWAP import calculate_VWAP
import pandas as pd
import sqlite3

conn = sqlite3.connect("data.db")

df = pd.read_sql_query("SELECT * FROM data_total", conn)
data = df[['code', 'date', 'TRD_Dalyr-Opnprc', 'TRD_Dalyr-Hiprc', 'TRD_Dalyr-Loprc', 
           'TRD_Dalyr-Clsprc', 'TRD_Dalyr-Dnshrtrd', 'STK_MKT_DALYR-Turnover']].copy()

data.columns = ['code', 'date', 'open', 'high', 'low', 'close', 'volume', 'turnover']
data['date'] = pd.to_datetime(data['date'])
data.dropna(inplace=True)
data.to_sql('price_related_data', conn, if_exists='replace', index=False)

grouped = data.groupby('code')
results = {}

# Define a list of all the calculation functions
indicator_names = {
    'BIAS': calculate_BIAS,
    'CCI' : calculate_CCI,
    'EMV' : calculate_EMV,
    'MA10' : calculate_MA,
    'MA20' : calculate_MA,
    'MACD' : calculate_MACD,
    'MTM6' : calculate_MTM,
    'MTM12' : calculate_MTM,
    'RSI' : calculate_RSI,
    'TRIX' : calculate_TRIX,
    'VOSC' : calculate_VOSC,
    'VRSI' : calculate_VRSI,
    'VWAP' : calculate_VWAP,
}

for name, group in grouped:
    # Sort group by date and set index
    group = group.sort_values(by='date').set_index('date')
    group_index = group.index  # Store the original index
    group_results = pd.DataFrame(index=group_index)
    # Apply each function to the group
    for indicator_name, func in indicator_names.items():
        if func == calculate_MA:
            if indicator_name == 'MA10':
                result = func(group, 10)
            else: result = func(group, 20)
        elif func == calculate_MTM:
            if indicator_name == 'MTM6':
                result = func(group, m=6)
            else: result = func(group, m=12)
        else:
            result = func(group)
        result = result.reindex(group_index)
        result.name = indicator_name
        group_results = pd.concat([group_results, result], axis=1)
    group_results['code'] = name
    results[name] = group_results

all_results = pd.concat(results.values()).reset_index()
all_results = all_results[(all_results['date'] >= '2016-01-01') & (all_results['date'] <= '2022-12-31')]

# merge data and all_results
all_results = pd.merge(all_results, data, how='left', on=['code', 'date'])

all_results = all_results[['code', 'date', 'open', 'high', 'low', 'close', 'volume', 'turnover',
                          'BIAS', 'CCI', 'EMV', 'MA10', 'MA20', 'MACD', 'MTM6', 'MTM12', 'RSI',
                          'TRIX', 'VOSC', 'VRSI', 'VWAP']]
all_results.to_sql('price_related_factors', conn, if_exists='replace', index=False)
conn.close()