# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 00:27:34 2023

@author: Mark
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

train = pd.read_csv(r'D:\Code Library\DDA4210\miniproj\train.csv')
test = pd.read_csv(r'D:\Code Library\DDA4210\miniproj\test.csv')

train = train.drop(['example_id'], axis = 1)
test = test.drop(['example_id'], axis = 1)
X = train.iloc[:, :4]
y = train.iloc[:, 4:].to_numpy()
X = np.log(X)
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 2023)

#%%

# PCA graph
pca = PCA(n_components = 2)
out = pca.fit_transform(X_train, y_train)
output = np.concatenate((out, y_train), axis = 1)
outputdf = pd.DataFrame(output, columns = ['pc0', 'pc1', 'label'])

plt.plot(outputdf.loc[outputdf.label == 0, 'pc0'],outputdf.loc[outputdf.label == 0, 'pc1'], 'ro', label = '1')
plt.plot(outputdf.loc[outputdf.label == 1, 'pc0'],outputdf.loc[outputdf.label == 1, 'pc1'], 'bo', label = '2')
plt.legend()
plt.show()

# TSNE graph
tsne = TSNE(n_components = 2)
output = tsne.fit_transform(X_train)
outputl = np.concatenate((output, y_train),axis = 1)
outputdf = pd.DataFrame(outputl, columns=['ts0', 'ts1', 'label'])

plt.plot(outputdf.loc[outputdf.label == 0, 'ts0'],outputdf.loc[outputdf.label == 0, 'ts1'], 'ro', label = '1')
plt.plot(outputdf.loc[outputdf.label == 1, 'ts0'],outputdf.loc[outputdf.label == 1, 'ts1'], 'bo', label = '2')
plt.legend()
plt.show()

#%% 98.25% prediction with kmeans denoising

perc = [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.81,0.85,0.9,0.92,0.95]
print(train.describe(percentiles = perc))

#clustering and deal with unnormal points
from sklearn.cluster import KMeans
X = train.iloc[:, 1:4].to_numpy()
kmeans = KMeans(n_clusters = 2, random_state = 2023)
kmeans.fit(X)
y_pred = kmeans.predict(X)
y_pred = y_pred+1
y_pred = np.where(y_pred == 2, 0, 1)
df_y_pred = pd.DataFrame(y_pred, columns = ['clust_label'])
train = pd.concat([train, df_y_pred], axis = 1)
train.to_csv(r'D:\Code Library\DDA4210\miniproj\train_clean.csv', index = False)
train = train[train.label == train['clust_label']]
train.to_csv(r'D:\Code Library\DDA4210\miniproj\train_final.csv', index = False)
y_pred = y_pred[:, np.newaxis]
output = np.concatenate((X, y_pred), axis = 1)

tsne = TSNE(n_components = 2)
output = tsne.fit_transform(X)
outputl = np.concatenate((output, y_pred),axis = 1)
outputdf = pd.DataFrame(outputl, columns=['ts0', 'ts1', 'label'])

plt.plot(outputdf.loc[outputdf.label == 0, 'ts0'],outputdf.loc[outputdf.label == 0, 'ts1'], 'ro', label = '1')
plt.plot(outputdf.loc[outputdf.label == 1, 'ts0'],outputdf.loc[outputdf.label == 1, 'ts1'], 'bo', label = '2')
plt.legend()
plt.show()

# Adaboost with kernel SVM

train = pd.read_csv(r'/nas_01/private/luguangli03/fuzzy_matching_Mark/Mark_test/4210mini/train_final.csv')
test = pd.read_csv(r'/nas_01/private/luguangli03/fuzzy_matching_Mark/Mark_test/4210mini/test.csv')

X = train.iloc[:, :4].to_numpy()
y = train.iloc[:, 4].to_numpy()
X = np.log(X)
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

params = {'base_estimator__C': [1,2,3], 'base_estimator__kernel': ['linear', 'poly', 'rbf', 'sigmoid'], 
          'base_estimator__gamma' : [0.1, 0.5, 1, 1.5, 2]}
weakclf = SVC()
ada = AdaBoostClassifier(base_estimator = weakclf, algorithm='SAMME')
grid = GridSearchCV(ada, params, cv = 5, n_jobs = -1)
grid.fit(X, y)
print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_) 

X_test = test.iloc[:, :4].to_numpy()
X_test = np.log(X_test)
scaler = StandardScaler()
scaler.fit(X_test)
X_test = scaler.transform(X_test)

weakclf = SVC(C=2, gamma=1.5, kernel='poly')
ada = AdaBoostClassifier(base_estimator = weakclf, algorithm='SAMME', n_estimators=500, learning_rate = 0.1)
ada.fit(X, y)
y_pred = ada.predict(X_test)
df_y_pred = pd.DataFrame(y_pred, columns = ['prediction'])
test_new = pd.concat([test, df_y_pred], axis = 1)
test_new = test_new.iloc[:, 4:]
test_new.to_csv(r'/nas_01/private/luguangli03/fuzzy_matching_Mark/Mark_test/4210mini/prediction.csv',  index = False)

#%% GMM denoising

from sklearn.mixture import GaussianMixture
X = train.iloc[:, 1:4].to_numpy()
gmm = GaussianMixture(n_components = 2)
gmm.fit(X)
y_pred = gmm.predict(X)
y_pred = y_pred+1
y_pred = np.where(y_pred == 2, 0, 1)
df_y_pred = pd.DataFrame(y_pred, columns = ['clust_label'])
train = pd.concat([train, df_y_pred], axis = 1)
train = train[train.label == train['clust_label']]

tsne = TSNE(n_components = 2)
output = tsne.fit_transform(X)
y_pred = y_pred[:, np.newaxis]
outputl = np.concatenate((output, y_pred),axis = 1)
outputdf = pd.DataFrame(outputl, columns=['ts0', 'ts1', 'label'])

plt.plot(outputdf.loc[outputdf.label == 0, 'ts0'],outputdf.loc[outputdf.label == 0, 'ts1'], 'ro', label = '1')
plt.plot(outputdf.loc[outputdf.label == 1, 'ts0'],outputdf.loc[outputdf.label == 1, 'ts1'], 'bo', label = '2')
plt.legend()
plt.show()

#%% 先降维在聚类 95.5

kmeans = KMeans(n_clusters = 2, random_state = 2023)
kmeans.fit(output)
y_pred = kmeans.predict(output)
y_pred = y_pred+1
y_pred = np.where(y_pred == 2, 0, 1)
df_y_pred = pd.DataFrame(y_pred, columns = ['clust_label'])
train = pd.concat([train, df_y_pred], axis = 1)
train.to_csv(r'D:\Code Library\DDA4210\miniproj\train_clean.csv', index = False)
train = train[train.label == train['clust_label']]
train.to_csv(r'D:\Code Library\DDA4210\miniproj\train_final_1.csv', index = False)
y_pred = y_pred[:, np.newaxis]
output = np.concatenate((X, y_pred), axis = 1)

train = pd.read_csv(r'D:\Code Library\DDA4210\miniproj\train_final_1.csv')
test = pd.read_csv(r'D:\Code Library\DDA4210\miniproj\test.csv')

X = train.iloc[:, :4].to_numpy()
y = train.iloc[:, 4].to_numpy()
X = np.log(X)
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

params = {'base_estimator__C': [1,2,3], 'base_estimator__kernel': ['linear', 'poly', 'rbf', 'sigmoid'], 
          'base_estimator__gamma' : [0.1, 0.5, 1, 1.5, 2]}
weakclf = SVC()
ada = AdaBoostClassifier(base_estimator = weakclf, algorithm='SAMME')
grid = GridSearchCV(ada, params, cv = 5, n_jobs = -1)
grid.fit(X, y)
print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_) 

X_test = test.iloc[:, :4].to_numpy()
X_test = np.log(X_test)
scaler = StandardScaler()
scaler.fit(X_test)
X_test = scaler.transform(X_test)

weakclf = SVC(C=2, gamma=1.5, kernel='poly')
ada = AdaBoostClassifier(base_estimator = weakclf, algorithm='SAMME', n_estimators=100, learning_rate = 0.1)
ada.fit(X, y)
y_pred = ada.predict(X_test)
df_y_pred = pd.DataFrame(y_pred, columns = ['prediction'])
test_new = pd.concat([test, df_y_pred], axis = 1)
test_new = test_new.iloc[:, 4:]
test_new.to_csv(r'D:\Code Library\DDA4210\miniproj\prediction_1.csv',  index = False)

#%% SMOTE扩增
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import SVMSMOTE

train = pd.read_csv(r'D:\Code Library\DDA4210\miniproj\train_final.csv')
test = pd.read_csv(r'D:\Code Library\DDA4210\miniproj\test.csv')

X = train.iloc[:, :4].to_numpy()
y = train.iloc[:, 4].to_numpy()

smo = SMOTE(random_state=2023, k_neighbors=5, n_jobs = -1)
X_res, y_res = smo.fit_resample(X, y)

print(np.unique(y_res, return_counts = True))
    
X_res = np.log(X_res)
scaler = StandardScaler()
scaler.fit(X_res)
X_res = scaler.transform(X_res)

X_test = test.iloc[:, :4].to_numpy()
X_test = np.log(X_test)
scaler = StandardScaler()
scaler.fit(X_test)
X_test = scaler.transform(X_test)

weakclf = SVC(C=2, gamma=1.5, kernel='poly')
ada = AdaBoostClassifier(base_estimator = weakclf, algorithm='SAMME', n_estimators=500, learning_rate = 0.1)
ada.fit(X_res, y_res)
y_pred = ada.predict(X_test)
df_y_pred = pd.DataFrame(y_pred, columns = ['prediction'])
test_new = pd.concat([test, df_y_pred], axis = 1)
test_new = test_new.iloc[:, 4:]
test_new.to_csv(r'/nas_01/private/luguangli03/fuzzy_matching_Mark/Mark_test/4210mini/prediction.csv',  index = False)











