# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:24:59 2023

@author: Mark
"""

import pandas as pd
import numpy as np
import os
import time
import random

random.seed(0)
np.random.seed(0)

os.chdir('D:\Code Library\CSC3170\CSC3170 Project')

skin = pd.read_csv('skin.csv')
prod = pd.read_csv('product.csv')
sephora = pd.read_csv('sephora_website_dataset.csv')
user = pd.read_csv('user.csv')
address1 = pd.read_csv('testdata1.csv', header = None)
address2 = pd.read_csv('testdata2.csv', header = None)
address3 = pd.read_csv('testdata3.csv', header = None)
address4 = pd.read_csv('testdata4.csv', header = None)
address = pd.concat([address1, address2, address3, address4])
address = address.to_numpy()
user = user[['USER_ID']]

sephora = sephora.iloc[:9000, :]
brand = sephora.iloc[:, 1:2]
brand = brand.drop_duplicates().reset_index(drop = True)
brand = brand.rename({'brand':'BRAND_NAME'}, axis = 1)

order = prod[['PRODUCT_ID','PRODCUT_NAME','PRICE']]
order_id = np.random.randint(1000000000, 2000000000, size = (21000, ), dtype = int)
order_id = np.random.choice(order_id, 20000, replace = False)
item_quant = np.random.randint(1, 100, size = (20000, ))
shipping_cost = np.random.randint(50, 200, size = (20000, )).astype(np.float64)
shipping_prec = np.round(np.random.random((20000, )), 2)
shipping_cost += shipping_prec

def generate_time():
    a1=(2022,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
    a2=(2023,4,1,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）
    
    start=time.mktime(a1)    #生成开始时间戳
    end=time.mktime(a2)      #生成结束时间戳
    
    #随机生成10个日期字符串
    date_list = []
    for i in range(20000):      
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y-%m-%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        date_list.append(date)
    return np.array(date_list)

timestamp = generate_time()

user_id = np.random.choice(user['USER_ID'].to_numpy(), size = (20000, ))
order_att = np.column_stack((order_id, item_quant, address, shipping_cost, timestamp, user_id))

order_att = pd.DataFrame(order_att, columns = ['ORDER_ID','ITEM_QUANTITY','SHIPPING_ADDRESS','TOTAL_SHIPPING_COST','TIMESTAMP','USER_ID'])
order = pd.concat([order, order_att], axis = 1)
namelist = {'PRODCUT_NAME':'PRODUCT_NAME','PRICE':'ITEM_PRICE'}
order = order.rename(namelist, axis = 1)
order['ITEM_PRICE'] = order['ITEM_PRICE']/20
order['ITEM_PRICE'] = order['ITEM_PRICE'].round(2)
order['TOTAL_COST'] = order['ITEM_PRICE']*order['ITEM_QUANTITY'] + order['TOTAL_SHIPPING_COST']
order = order[['ORDER_ID','ITEM_PRICE','ITEM_QUANTITY','SHIPPING_ADDRESS','TOTAL_SHIPPING_COST', 'TOTAL_COST','TIMESTAMP','PRODUCT_NAME','USER_ID']]

prod = pd.read_csv('product.csv')
prod = prod[['PRODUCT_ID','PRODCUT_NAME','PRICE']]
prod_new = np.random.choice(prod['PRODCUT_NAME'].to_numpy(), size = (20000, ))
prod_new = pd.DataFrame(prod_new, columns = ['PRODUCT_NAME'])
prod_new = pd.merge(prod_new, prod, how = 'left', left_on = 'PRODUCT_NAME', right_on = 'PRODCUT_NAME')
prod_new = prod_new.drop_duplicates()
prod_new = prod_new[['PRODUCT_NAME','PRICE']]
prod_name = np.random.choice(prod_new['PRODUCT_NAME'], 20000)
prod_name = pd.DataFrame(prod_name, columns = ['PRODUCT_NAME'])
prod_final = pd.merge(prod_name, prod_new, how = 'left', on = 'PRODUCT_NAME')
prod_new = prod_final
order['ITEM_PRICE'] = prod_new['PRICE']
order['ITEM_PRICE'] = order['ITEM_PRICE']/20
order['ITEM_PRICE'] = order['ITEM_PRICE'].round(2)
order['PRODUCT_NAME'] = prod_new['PRODUCT_NAME']
order['TOTAL_COST'] = order['ITEM_PRICE']*order['ITEM_QUANTITY'] + order['TOTAL_SHIPPING_COST']

prod = pd.read_csv('product.csv')
order_cate = pd.merge(order, prod, how = 'left', left_on = ['PRODUCT_NAME'], right_on = ['PRODCUT_NAME'])
order_cate = order_cate[['ORDER_ID','ITEM_PRICE','ITEM_QUANTITY','SHIPPING_ADDRESS','TOTAL_SHIPPING_COST', 'TOTAL_COST','TIMESTAMP','PRODUCT_NAME', 'PRODUCT_ID','USER_ID','CATEGORY']]
order_cate = order_cate.drop_duplicates()
order_cate[['ITEM_QUANTITY']] = order_cate[['ITEM_QUANTITY']].astype(int)
order_cate[['TOTAL_SHIPPING_COST','TOTAL_COST']] = order_cate[['TOTAL_SHIPPING_COST','TOTAL_COST']].astype(float)


order_cate['TIMESTAMP'] = pd.to_datetime(order_cate['TIMESTAMP']).dt.strftime("%Y-%m-%d")
mask = (order_cate['TIMESTAMP'] > '2022-12-01') & (order_cate['TIMESTAMP'] < '2023-03-20') & (order_cate['CATEGORY'] == 'Skincare')
new_quant = order_cate.loc[mask, 'ITEM_QUANTITY'] + 50
mask = (order_cate['TIMESTAMP'] > '2022-01-01') & (order_cate['TIMESTAMP'] < '2022-03-20') & (order_cate['CATEGORY'] == 'Skincare')
new_quant = order_cate.loc[mask, 'ITEM_QUANTITY'] + 50
order_cate.loc[mask, 'ITEM_QUANTITY'] = new_quant

test_skin = order_cate.loc[mask]  
order_output = order_cate.iloc[:, :10]
order_output = order_output.drop_duplicates(subset = 'ORDER_ID')
order_output = order_output.drop('PRODUCT_NAME', axis = 1)
    
order_output.to_csv('order.csv', index = False, encoding = 'utf-8')
