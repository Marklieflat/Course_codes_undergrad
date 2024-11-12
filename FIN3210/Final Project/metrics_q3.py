import numpy as np
import pandas as pd
from metrics import pearson_correlation, theil_u, mase

# df = pd.read_csv('LSTM_result_merged.csv')
# original = pd.read_csv('top_10_v5_selected.csv')[['code','date','close']]
# original['date'] = pd.to_datetime(original['date']).dt.strftime('%Y-%m-%d')
# original = original.loc[original['date'] == '2016-01-04'].reset_index(drop=True)
# original.drop(columns=['date'], inplace=True)
# df = pd.merge(df, original, on='code', how='left')
# df = df.rename({'close': 'original_close'}, axis=1)
# df['pred_price'] = df['original_close'] * (1 + df['pred'])
# df['true_price'] = df['original_close'] * (1 + df['true'])
# df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
# df['pred_ret'] = df.groupby(['code'])['pred_price'].pct_change()   
# df['true_ret'] = df.groupby(['code'])['true_price'].pct_change()
# df.dropna(inplace=True)
# df.reset_index(drop=True, inplace=True)
# df = df[['code','date','pred_ret','true_ret']]
# print(df)

df = pd.read_csv('threeModelOutput.csv')

for code in df['code'].unique():
    print(f"========Baseline Metrics for stock {code}========")
    print("MASE: ", mase(df.loc[df['code']==code, 'cum_ret_real'], df.loc[df['code']==code, 'cum_ret1']))
    print("Pearson Correlation: ", pearson_correlation(df.loc[df['code']==code, 'cum_ret_real'], df.loc[df['code']==code, 'cum_ret1']))
    print("Theil-U: ", theil_u(df.loc[df['code']==code, 'cum_ret_real'], df.loc[df['code']==code, 'cum_ret1']))
    print("\n")

    print(f"========Ridge Metrics for stock {code}========")
    print("MASE: ", mase(df.loc[df['code']==code, 'cum_ret_real'], df.loc[df['code']==code, 'cum_ret2']))
    print("Pearson Correlation: ", pearson_correlation(df.loc[df['code']==code, 'cum_ret_real'], df.loc[df['code']==code, 'cum_ret2']))
    print("Theil-U: ", theil_u(df.loc[df['code']==code, 'cum_ret_real'], df.loc[df['code']==code, 'cum_ret2']))
    print("\n")

    print(f"========WSAE-LSTM Metrics for stock {code}========")
    print("MASE: ", mase(df.loc[df['code']==code, 'cum_ret_real'], df.loc[df['code']==code, 'cum_ret3']))
    print("Pearson Correlation: ", pearson_correlation(df.loc[df['code']==code, 'cum_ret_real'], df.loc[df['code']==code, 'cum_ret3']))
    print("Theil-U: ", theil_u(df.loc[df['code']==code, 'cum_ret_real'], df.loc[df['code']==code, 'cum_ret3']))
    print("\n")