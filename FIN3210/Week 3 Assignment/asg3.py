import pandas as pd
import numpy as np
from linearmodels import PanelOLS
import matplotlib.pyplot as plt

# df = pd.read_excel('FIN3210 Week 3 Stock returns.xlsx', sheet_name='data')
# df.to_csv('FIN3210 Week 3 Stock returns.csv', index=False)
df = pd.read_csv('FIN3210 Week 3 Stock returns.csv')
data = df.drop(['stknme','conme'], axis=1).copy()
data['month'] = pd.to_datetime(data['month'], format='%Y-%m').dt.to_period('M')
data['year_quarter'] = data['month'].dt.strftime('%Y-Q%q')

# """
# 1)	Using the data set of stock returns, sort stocks into quintiles by size every quarter, 
# hold stocks over the quarter, and calculate monthly portfolio returns
# """
# data['size_label'] = data.groupby('year_quarter')['size'].transform(lambda x: pd.qcut(x, 5, labels=[1,2,3,4,5]))
# data['last_size_label'] = data.groupby(['stkcd','year_quarter'])['size_label'].shift(1)
# data.loc[data['last_size_label'].isnull(),'last_size_label'] = data.loc[data['last_size_label'].isnull(),'size_label']
# port_res = data.groupby(['month','last_size_label'])['retrf'].mean().reset_index()
# print(port_res.head(50))

# """
# 2)	Using the data set of stock returns, sort stocks into quintiles by institutional 
# ownership every quarter, hold stocks over the quarter, and calculate monthly portfolio returns
# """
# data['inst_label'] = data.groupby('year_quarter')['instown'].transform(lambda x: pd.qcut(x, 5, labels=[1,2,3,4,5]))
# data['last_inst_label'] = data.groupby(['stkcd','year_quarter'])['inst_label'].shift(1)
# data.loc[data['last_inst_label'].isnull(),'last_inst_label'] = data.loc[data['last_inst_label'].isnull(),'inst_label']
# port_res = data.groupby(['month','last_inst_label'])['retrf'].mean().reset_index()
# print(port_res.head(50))

# """
# 3)	Using the data set of stock returns, perform panel regression, 
# and regress stock returns on firm characteristics such as size, 
# book-to-market ratio, return12, roa, leverage, ppe, intang, number of analysts, 
# institutional ownership, controlling for or not for firm and year-month fixed effects. 
# Cluster standard errors by firm and year-month (double clustering)
# """
# panel_data = data[['stkcd','month','retrf','bm','return12','roa','lev','ppe','intang','numanalyst','instown']].copy()
# panel_data['month'] = pd.to_numeric(panel_data['month'].dt.strftime('%Y%m'))
# panel_data.set_index(['stkcd','month'], inplace=True)
# model = PanelOLS(panel_data['retrf'], panel_data[['bm','return12','roa','lev','ppe','intang','numanalyst','instown']], entity_effects=True, time_effects=True)
# res = model.fit(cov_type='clustered', cluster_entity=True, cluster_time=True)
# print(res.summary)

"""
4)	Using the data set of Online sales, aggregate monthly online sales over quarters, 
download reported quarterly total sales from CSMAR, and plot figures including both online 
sales and reported quarterly sales.
"""
# sales = pd.read_excel('FIN3210 Week 3 Online sales.xlsx', sheet_name='月度销售')
# sales = sales.melt(id_vars=['时间'], var_name='Brand', value_name='online_sales')
# sales.rename({'时间':'month'}, axis=1, inplace=True)
# sales['month'] = pd.to_datetime(sales['month'], format='%Y-%m').dt.to_period('M')
# sales['year_quarter'] = sales['month'].dt.strftime('%Y-Q%q')
# sales['stkcd'] = sales['Brand'].str.extract('(\d+)').astype('int')
# sales = sales.groupby(['year_quarter'])['online_sales'].sum().reset_index()
report_sales = pd.read_csv('FS_Comins.csv')
report_sales['Accper'] = pd.to_datetime(report_sales['Accper'], format='%Y-%m-%d').dt.to_period('M')
report_sales['Accper'] = report_sales['Accper'].dt.strftime('%Y-Q%q')
report_sales = report_sales.loc[report_sales['Typrep']=='B',:]
print(report_sales['Stkcd'].value_counts())
# report_sales.drop(['B001101000','Typrep'], axis=1, inplace=True)
# report_sales.reset_index(drop=True, inplace=True)
# report_sales.rename({'B001100000':'report_sales'}, axis=1, inplace=True)
# report_sales = report_sales.groupby(['Accper'])['report_sales'].sum().reset_index()
# online_report = pd.merge(sales, report_sales, how='left', left_on=['year_quarter'], right_on=['Accper'])

# plt.figure(figsize=(10,8))
# plt.plot(online_report['year_quarter'], online_report['online_sales'], label='online_sales')
# plt.plot(online_report['year_quarter'], online_report['report_sales'], label='report_sales')
# plt.title('Online sales vs Reported sales')
# plt.xticks(rotation=45)
# plt.xlabel('Year Quarter')
# plt.ylabel('Sales')
# plt.legend()
# plt.show()