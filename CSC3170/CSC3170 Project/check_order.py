# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:54:44 2023

@author: Mark
"""

import pandas as pd
import numpy as np
import os
import time
import random
os.chdir('D:\Code Library\CSC3170\CSC3170 Project')

order = pd.read_csv('order.csv')
# prod = pd.read_csv('product.csv')
# prod = prod[['NAME','PRODUCT_PRICE']]
# prod_new = np.random.choice(prod['NAME'].to_numpy(), size = (20000, ))
# prod_new = pd.DataFrame(prod_new, columns = ['PRODUCT_NAME'])
# prod_new = pd.merge(prod_new, prod, how = 'left', left_on = 'PRODUCT_NAME', right_on = 'NAME')
# prod_new = prod_new.iloc[:20000, :]
# prod_new = prod_new[['PRODUCT_NAME','PRODUCT_PRICE']]
# order['ITEM_PRICE'] = prod_new['PRODUCT_PRICE']
# order['PRODUCT_NAME'] = prod_new['PRODUCT_NAME']
# order['TOTAL_COST'] = order['ITEM_PRICE']*order['ITEM_QUANTITY'] + order['TOTAL_SHIPPING_COST']
# order.to_csv('order.csv', index = False, encoding = 'utf_8_sig')
item_quant = np.random.randint(1, 150, size = (20000, ))
order['ITEM_QUANTITY'] = item_quant
order['TOTAL_COST'] = order['ITEM_PRICE']*order['ITEM_QUANTITY'] + order['TOTAL_SHIPPING_COST']
order.to_csv('order.csv', index = False, encoding = 'utf-8')
