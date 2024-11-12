import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('LSTM_result_merged.csv')
df = df.loc[df['code'] == 12].reset_index(drop=True)
# print(df)



# df['cum_pred'] = (1 + df['pred']).cumprod()-1
# df['cum_true'] = (1 + df['true']).cumprod()-1

# plt.plot(df['cum_pred'], label='pred')
# plt.plot(df['cum_true'], label='true')
# plt.legend()
# plt.show()



plt.figure(figsize=(15, 8))
plt.plot(df['pred'], label='pred')
plt.plot(df['true'], label='true')
plt.legend()
plt.show()

# ori_df = pd.read_csv('top_10_v5_selected_normalized.csv')
# df = ori_df.loc[ori_df['code'] == 12].reset_index(drop=True)
# df = df.iloc[1500:]
# df['cumret'] = (1 + df['ret']).cumprod()-1
# plt.figure(figsize=(15, 6))
# plt.ylim(-0.4,0.8)
# plt.plot(df['cumret'])
# plt.show()

# original_df = pd.read_csv('top_10_v5_selected.csv')
# df = pd.read_csv('top_10_v5_selected_normalized.csv')
# df['close'] = original_df['close']
# df.to_csv('top_10_v5_selected_normalized_new.csv', index=False)
