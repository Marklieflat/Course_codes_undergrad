import pandas as pd
import sqlite3

def get_monthly_thresholds(group):
    # Determine the small/big and high/low BM thresholds
    small_threshold = group['size_rank'].quantile(0.5)
    low_BM_threshold = group['BM_rank'].quantile(0.3)
    high_BM_threshold = group['BM_rank'].quantile(0.7)

    # Assign the portfolio labels within the group
    group['small_stock'] = group['size_rank'] <= small_threshold
    group['big_stock'] = group['size_rank'] > small_threshold
    group['high_BM_stock'] = group['BM_rank'] >= high_BM_threshold
    group['low_BM_stock'] = group['BM_rank'] <= low_BM_threshold
    return group

# Define a function to calculate the SMB and HML factors
def calculate_monthly_factors(df):
    df['date'] = pd.to_datetime(df['date'])
    # Extract year and month to a separate column for easier grouping
    df['YYYYMM'] = df['date'].dt.strftime('%Y%m')

    # Calculate monthly size rank and BM rank within each month
    df['size_rank'] = df.groupby('YYYYMM')['total_MV'].rank()
    df['BM_ratio'] = df['BookValue'] / df['total_MV']
    df['BM_rank'] = df.groupby('YYYYMM')['BM_ratio'].rank()

    # Apply the function to assign portfolio labels for each month
    df = df.groupby('YYYYMM').apply(get_monthly_thresholds)

    # Calculate SMB and HML for each month
    smb_monthly = df.groupby('YYYYMM').apply(
        lambda x: x[x['small_stock']]['ret'].mean() - x[x['big_stock']]['ret'].mean()
    )
    hml_monthly = df.groupby('YYYYMM').apply(
        lambda x: x[x['high_BM_stock']]['ret'].mean() - x[x['low_BM_stock']]['ret'].mean()
    )

    smb_monthly = smb_monthly.reset_index(name='SMB')
    hml_monthly = hml_monthly.reset_index(name='HML')

    df = df.merge(smb_monthly, on='YYYYMM', how='left')
    df = df.merge(hml_monthly, on='YYYYMM', how='left')
    return df

conn = sqlite3.connect("data.db")
tmp = pd.read_sql_query("SELECT * FROM data_total", conn)

df_fama = tmp[['code', 'date', 'TRD_Dalyr-Clsprc','TRD_Dalyr-Dsmvosd', 'TRD_Dalyr-Dsmvtll', 'BookValue',
               'TRD_Dalyr-Dretwd','TRD_Nrrate-Nrrdaydt', 'r_m_weightedByMV']].copy()
df_fama.columns = ['code', 'date', 'closePrice', 'circulating_MV', 'total_MV', 'BookValue', 'ret', 'r_f', 'r_m']
df_fama.BookValue = df_fama.BookValue / 1000
df_fama.dropna(inplace=True)

df_fama['excess_ret'] = df_fama['ret'] - df_fama['r_f']

# Calculate the daily SMB and HML factors
df_fama = calculate_monthly_factors(df_fama)

df_fama.to_sql('ff_3', conn, if_exists = "replace", index=False)
conn.close()