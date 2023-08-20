# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:58:16 2022

@author: Mark
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_excel('./HW1/Classification iris.xlsx', header = None)

df = df.rename(columns = {0:' sepal length', 1:'sepal width', 2:'petal length', 3:'petal width', 4:'class'})

df = pd.get_dummies(df)

def fit(X,y):
    w_close = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    return w_close

def calculate_res(w1, x, y):
    y_hat = x.dot(w1)
    max_index = np.argmax(y_hat, 1)
    y_real = np.argmax(y, 1)
    result_arr = (max_index == y_real)
    err_rate = 1 - np.sum(result_arr) / result_arr.size
    return err_rate
      
ran_seeds = [i for i in range(2022,2032)]
X = df.iloc[:, :4].to_numpy()
X_ = np.hstack((np.ones((X.shape[0],1)),X))
y = df.iloc[:, 4:].to_numpy()
result = pd.DataFrame(columns = ['Training_error','Testing_error'])

for i in ran_seeds:
    x_train, x_test, y_train, y_test = train_test_split(X_, y, test_size=0.2, random_state=i)
    w1 = fit(x_train, y_train)
    err_rate_test = calculate_res(w1, x_test, y_test)
    err_rate_train = calculate_res(w1, x_train, y_train)
    lst = [err_rate_train, err_rate_test]
    result.loc[len(result)] = lst
    
print(result)

#%%

from sklearn.linear_model import LinearRegression

for i in range(2022,2032):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    
    model = LinearRegression()
    
    model.fit(x_train,y_train)
    
    y_hat_test = model.predict(x_test)
    
    max_index = np.argmax(y_hat_test, 1)
    y_real = np.argmax(y_test, 1)
    result_arr = (max_index == y_real)
    err_rate = 1 - np.sum(result_arr) / result_arr.size
    print(err_rate)
    
    
    
    
    
    
    
    
    
