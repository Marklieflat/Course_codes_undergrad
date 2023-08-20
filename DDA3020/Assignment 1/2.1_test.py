# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:40:00 2022

@author: Mark
"""


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('./HW1/Regression.csv')

df = df.drop(['station','Date'], axis = 1)

# print(df.describe())

df = df.dropna()

def fit(X, y):
    w_close = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    return w_close

ran_seeds = [i for i in range(2022,2032)]
X = df.iloc[:, :21].to_numpy()
X_ = np.hstack((np.ones((X.shape[0],1)),X))
y = df.iloc[:, 21:].to_numpy()
result = pd.DataFrame(columns = ['Training_RMSE_Next_Tmax','Training_RMSE_Next_Tmin','Testing_RMSE_Next_Tmax','Testing_RMSE_Next_Tmin'])
res = pd.DataFrame(columns = ['Training_RMSE','Testing_RMSE'])
for i in ran_seeds:
    x_train, x_test, y_train, y_test = train_test_split(X_, y, test_size=0.2, random_state=i)
    w1 = fit(x_train, y_train)
    y_hat_test = x_test.dot(w1)
    y_hat_train = x_train.dot(w1)
    y0_rmse_test = np.sqrt(np.sum((y_hat_test[:,0] - y_test[:,0]) ** 2) / len(x_test))
    y1_rmse_test = np.sqrt(np.sum((y_hat_test[:,1] - y_test[:,1]) ** 2) / len(x_test))
    y0_rmse_train = np.sqrt(np.sum((y_hat_train[:,0] - y_train[:,0]) ** 2) / len(x_train))
    y1_rmse_train = np.sqrt(np.sum((y_hat_train[:,1] - y_train[:,1]) ** 2) / len(x_train))
    y_rmse_test = (y0_rmse_test + y1_rmse_test)/2
    y_rmse_train = (y0_rmse_train + y1_rmse_train)/2
    # lst = [y0_rmse_train, y1_rmse_train, y0_rmse_test, y1_rmse_test]
    # result.loc[len(result)] = lst
    chart = [y_rmse_train, y_rmse_test]
    res.loc[len(res)] = chart
    # print((mean_squared_error(y_test, y_hat_test, squared = False)))
    
    
print(res)

# error = y_hat_train - y_train
# norm = np.linalg.norm(error, axis = 1)
# result = (sum(norm)/len(y_hat_train))**0.5

#%%
"""SKlearn Testing part"""

from sklearn.linear_model import LinearRegression

for i in range(2022,2032):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    
    model = LinearRegression()
    
    model.fit(x_train,y_train)
    
    y_hat_test = model.predict(x_test)
    
    y_hat_train = model.predict(x_train)
    
    print((mean_squared_error(y_test, y_hat_test, squared = False)))
    
    # print((mean_squared_error(y_train, y_hat_train, squared = False)))
