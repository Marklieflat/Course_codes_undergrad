#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:19:41 2023

@author: rnd
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from imblearn.over_sampling import SMOTE

def addfeature(df):
    if df['feature_4'] <= 30:
        df['feature_5'] = 0
    else:
        df['feature_5'] = 1
    return df

train = pd.read_csv(r'D:\Code Library\DDA4210\miniproj\train.csv')
train = train.apply(addfeature, axis = 1)
train = train[['feature_1','feature_2','feature_3','feature_4','feature_5','label','example_id']]
test = pd.read_csv(r'D:\Code Library\DDA4210\miniproj\test.csv')

X = train.iloc[:, :5].to_numpy()
y = train.iloc[:, 5].to_numpy()

smo = SMOTE(random_state=2023, k_neighbors=5, n_jobs = -1)
X_res, y_res = smo.fit_resample(X, y)

print(np.unique(y_res, return_counts = True))
    
# X_res = np.log(X_res)
# scaler = StandardScaler()
# scaler.fit(X_res)
# X_res = scaler.transform(X_res)

# params = {'base_estimator__C': [1,2,3,4,5], 'base_estimator__kernel': ['linear', 'poly', 'rbf', 'sigmoid'], 
#           'base_estimator__gamma' : [0.1, 0.5, 1, 1.5, 2,2.5,3]}
# weakclf = SVC()
# ada = AdaBoostClassifier(base_estimator = weakclf, algorithm='SAMME')
# grid = GridSearchCV(ada, params, cv = 5, n_jobs = -1)
# grid.fit(X_res, y_res)
# print(grid.best_score_)
# print(grid.best_params_)
# print(grid.best_estimator_)

# X_test = test.iloc[:, :4].to_numpy()
# X_test = np.log(X_test)
# scaler = StandardScaler()
# scaler.fit(X_test)
# X_test = scaler.transform(X_test)

weakclf = SVC(C=5, gamma=2.5, kernel='poly')
ada = AdaBoostClassifier(base_estimator = weakclf, algorithm='SAMME', n_estimators=100, learning_rate = 0.1)
# ada = AdaBoostClassifier(n_estimators=100, learning_rate = 0.1)
ada.fit(X_res, y_res)
# y_pred = ada.predict(X_test)
# df_y_pred = pd.DataFrame(y_pred, columns = ['prediction'])
# test_new = pd.concat([test, df_y_pred], axis = 1)
# test_final = test_new.iloc[:, 4:]
# test_final.to_csv(r'/nas_01/private/luguangli03/fuzzy_matching_Mark/Mark_test/4210mini/prediction_5.csv',  index = False)

def testing(test):
    final = pd.read_csv(r'/nas_01/private/luguangli03/fuzzy_matching_Mark/Mark_test/4210mini/resultfinal.csv')
    final = final['prediction'].to_numpy()
    test = test['prediction'].to_numpy()
    acc = np.sum(final == test) / len(final)
    return acc

testdt = pd.read_csv(r'/nas_01/private/luguangli03/fuzzy_matching_Mark/Mark_test/4210mini/prediction_5.csv')
print(testing(testdt))

add_test = pd.read_csv(r'D:\Code Library\DDA4210\miniproj\augmented_test.csv')
add_test = add_test.apply(addfeature, axis = 1)
add_test = add_test[['feature_1','feature_2','feature_3','feature_4','feature_5','example_id']]
add_X_test = add_test.iloc[:, :5].to_numpy()
# add_X_test = np.log(add_X_test)
# scaler = StandardScaler()
# scaler.fit(add_X_test)
# add_X_test = scaler.transform(add_X_test)
add_y_pred = ada.predict(add_X_test)
add_df_y_pred = pd.DataFrame(add_y_pred, columns = ['prediction'])
add_test_new = pd.concat([add_test, add_df_y_pred], axis = 1)
add_test_final = add_test_new.iloc[:, 4:]
add_test_final.to_csv(r'D:\Code Library\DDA4210\miniproj\additional_1.csv',  index = False)

# Additional test visualization
tsne = TSNE(n_components = 2)
output = tsne.fit_transform(add_X_test)
ylabel = add_test_new.iloc[:, 5].to_numpy()
ylabel = ylabel[:, np.newaxis]
outputl = np.concatenate((output, ylabel),axis = 1)
outputdf = pd.DataFrame(outputl, columns=['ts0', 'ts1', 'label'])

plt.plot(outputdf.loc[outputdf.label == 0, 'ts0'],outputdf.loc[outputdf.label == 0, 'ts1'], 'ro', label = '1')
plt.plot(outputdf.loc[outputdf.label == 1, 'ts0'],outputdf.loc[outputdf.label == 1, 'ts1'], 'bo', label = '2')
plt.legend()
plt.show()











