# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 18:04:28 2023

@author: Mark
"""

import pandas as pd
import numpy as np
import os
import time
import random
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
user = user[['ID']]

sephora = sephora.iloc[:9000, :]
brand = sephora.iloc[:, 1:2]
brand = brand.drop_duplicates().reset_index(drop = True)
brand = brand.rename({'brand':'BRAND_NAME'}, axis = 1)

order = prod[['NAME','PRICE']]
order_id = np.random.randint(1000000000, 2000000000, size = (20000, ), dtype = int)
item_quant = np.random.randint(1, 150, size = (20000, ))
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

user_id = np.random.choice(user['ID'].to_numpy(), size = (20000, ))
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
prod = prod[['NAME','PRODUCT_PRICE']]
prod_new = np.random.choice(prod['NAME'].to_numpy(), size = (20000, ))
prod_new = pd.DataFrame(prod_new, columns = ['PRODUCT_NAME'])
prod_new = pd.merge(prod_new, prod, how = 'left', left_on = 'PRODUCT_NAME', right_on = 'NAME')
prod_new = prod_new.iloc[:20000, :]
prod_new = prod_new[['PRODUCT_NAME','PRODUCT_PRICE']]
order['ITEM_PRICE'] = prod_new['PRODUCT_PRICE']
order['PRODUCT_NAME'] = prod_new['PRODUCT_NAME']
order['TOTAL_COST'] = order['ITEM_PRICE']*order['ITEM_QUANTITY'] + order['TOTAL_SHIPPING_COST']
