# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 21:19:55 2022

@author: Mark
"""
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import MultipleLocator
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor

carseats = pd.read_csv('./Carseats.csv')

X = carseats.drop(['Sales'], axis = 1)
X = pd.get_dummies(X)
y = carseats['Sales']

X_train = X.head(300)
y_train = y.head(300)
X_test = X.tail(100)
y_test = y.tail(100)

#Data Statistics
numerical = carseats.drop(['ShelveLoc','Urban','US'], axis = 1)
categorical = carseats[['ShelveLoc','Urban','US']]
print(numerical.describe())
print(categorical['ShelveLoc'].value_counts())
print(categorical['Urban'].value_counts())
print(categorical['US'].value_counts())

fig, ax =plt.subplots(1,3,constrained_layout=True, figsize=(8, 3))
pic = sns.histplot(carseats, x = "Sales", ax = ax[0], bins = 10)
pic.set_title('Sales')
pic = sns.histplot(carseats, x = "CompPrice", ax = ax[1], bins = 10)
pic.set_title('CompPrice')
pic = sns.histplot(carseats, x = "Income", ax = ax[2], bins = 10)
pic.set_title('Income')

fig, ax =plt.subplots(1,3,constrained_layout=True, figsize=(8, 3))
pic = sns.histplot(carseats, x = "Advertising", ax = ax[0], bins = 10)
pic.set_title('Advertising')
pic = sns.histplot(carseats, x = "Population", ax = ax[1], bins = 10)
pic.set_title('Population')
pic = sns.histplot(carseats, x = "Price", ax = ax[2], bins = 10)
pic.set_title('Price')

fig, ax =plt.subplots(1,3,constrained_layout=True, figsize=(8, 3))
pic = sns.histplot(carseats, x = "ShelveLoc", ax = ax[0], bins = 10)
pic.set_title('ShelveLoc')
pic = sns.histplot(carseats, x = "Age", ax = ax[1], bins = 10)
pic.set_title('Age')
pic = sns.histplot(carseats, x = "Education", ax = ax[2], bins = 10)
pic.set_title('Education')

fig, ax =plt.subplots(1,2,constrained_layout=True, figsize=(8, 3))
pic = sns.histplot(carseats, x = "Urban", ax = ax[0], bins = 10)
pic.set_title('Urban')
pic = sns.histplot(carseats, x = "US", ax = ax[1], bins = 10)
pic.set_title('US')

# Decision Tree
def decision_tree(maxdepth, minleafsamples):
    reg = tree.DecisionTreeRegressor(max_depth = maxdepth, min_samples_leaf = minleafsamples, random_state = 3020)
    reg.fit(X_train, y_train)
    y_train_pred = reg.predict(X_train)
    train_MSE = metrics.mean_squared_error(y_train, y_train_pred)
    y_test_pred = reg.predict(X_test)
    test_MSE = metrics.mean_squared_error(y_test, y_test_pred)
    return train_MSE, test_MSE

diff_depth = pd.DataFrame(columns = ['max depth', 'train_MSE', 'test_MSE'])
for i in range(1,11):
    train_mse, test_mse = decision_tree(i, 9)
    chart = [i, train_mse, test_mse]
    diff_depth.loc[len(diff_depth)] = chart
    
plt.plot(diff_depth['max depth'], diff_depth['train_MSE'], color = 'r', label = 'Training_MSE')
plt.plot(diff_depth['max depth'], diff_depth['test_MSE'], color = 'b', label = 'Testing_MSE')
plt.xlabel('Max Depth')
plt.ylabel('MSE')
plt.title('Plot of MSE and Max Depth')
plt.legend(loc = "best")
plt.show()

diff_leaf_size = pd.DataFrame(columns = ['least node size', 'train_MSE', 'test_MSE'])
for i in range(1,21):
    train_mse, test_mse = decision_tree(8, i)
    chart = [i, train_mse, test_mse]
    diff_leaf_size.loc[len(diff_leaf_size)] = chart
    
plt.plot(diff_leaf_size['least node size'], diff_leaf_size['train_MSE'], color = 'r', label = 'Training_MSE')
plt.plot(diff_leaf_size['least node size'], diff_leaf_size['test_MSE'], color = 'b', label = 'Testing_MSE')
plt.xlabel('Least Node Size')
plt.ylabel('MSE')
x_major_locator=MultipleLocator(2)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.title('Plot of MSE and Least Node Size')
plt.legend(loc = "best")
plt.show()

params = {'max_depth':[i for i in range(1,11)],'min_samples_leaf':[x for x in range(1,21)]}
grid = GridSearchCV(tree.DecisionTreeRegressor(random_state=3020),param_grid = params, cv=5, n_jobs = -1)
grid.fit(X_train,y_train)
print('Best Parameter Pairs: ', grid.best_params_)

tree1 = tree.DecisionTreeRegressor(random_state = 3020)
tree1.fit(X_train, y_train)
fig1 = plt.figure(figsize = (25,20), dpi = 600)
fig1 = tree.plot_tree(tree1, feature_names=X.columns)
plt.savefig('p1.png', format = 'png')

tree2 = tree.DecisionTreeRegressor(max_depth = 4, min_samples_leaf = 10, random_state = 3020)
tree2.fit(X_train, y_train)
fig2 = plt.figure(figsize = (25,20), dpi = 600)
fig2 = tree.plot_tree(tree2, feature_names=X.columns)
plt.savefig('p2.png', format = 'png')

tree3 = tree.DecisionTreeRegressor(max_depth = 4, min_samples_leaf = 20, random_state = 3020)
tree3.fit(X_train, y_train)
fig3 = plt.figure(figsize = (25,20), dpi = 600)
fig3 = tree.plot_tree(tree3, feature_names=X.columns)
plt.savefig('p3.png', format = 'png')

tree4 = tree.DecisionTreeRegressor(max_depth = 8, min_samples_leaf = 10, random_state = 3020)
tree4.fit(X_train, y_train)
fig4 = plt.figure(figsize = (25,20), dpi = 600)
fig4 = tree.plot_tree(tree4, feature_names=X.columns)
plt.savefig('p4.png', format = 'png')

tree5 = tree.DecisionTreeRegressor(max_depth = 8, min_samples_leaf = 20, random_state = 3020)
tree5.fit(X_train, y_train)
fig5 = plt.figure(figsize = (25,20), dpi = 600)
fig5 = tree.plot_tree(tree5, feature_names=X.columns)
plt.savefig('p5.png', format = 'png')

# Bagging
def Bagging(depth, numtrees):
    reg = BaggingRegressor(base_estimator = tree.DecisionTreeRegressor(max_depth = depth, 
        min_samples_leaf = 9, random_state = 3020), n_estimators = numtrees)
    reg.fit(X_train, y_train)
    y_train_pred = reg.predict(X_train)
    train_MSE = metrics.mean_squared_error(y_train, y_train_pred)
    y_test_pred = reg.predict(X_test)
    test_MSE = metrics.mean_squared_error(y_test, y_test_pred)
    return train_MSE, test_MSE
    
diff_depth = pd.DataFrame(columns = ['max depth', 'train_MSE', 'test_MSE'])
for i in range(1,11):
    train_mse, test_mse = Bagging(i, 50)
    chart = [i, train_mse, test_mse]
    diff_depth.loc[len(diff_depth)] = chart
    
plt.plot(diff_depth['max depth'], diff_depth['train_MSE'], color = 'r', label = 'Training_MSE')
plt.plot(diff_depth['max depth'], diff_depth['test_MSE'], color = 'b', label = 'Testing_MSE')
plt.xlabel('Depth')
plt.ylabel('MSE')
plt.title('Plot of MSE and Depth')
plt.legend(loc = "best")
plt.show()

diff_numtree = pd.DataFrame(columns = ['numtrees', 'train_MSE', 'test_MSE'])
for i in range(1,101):
    train_mse, test_mse = Bagging(6, i)
    chart = [i, train_mse, test_mse]
    diff_numtree.loc[len(diff_numtree)] = chart

plt.plot(diff_numtree['numtrees'], diff_numtree['train_MSE'], color = 'r', label = 'Training_MSE')
plt.plot(diff_numtree['numtrees'], diff_numtree['test_MSE'], color = 'b', label = 'Testing_MSE')
plt.xlabel('Number of Trees')
plt.ylabel('MSE')
plt.title('Plot of MSE and Number of Trees')
plt.legend(loc = "best")
plt.show()

# Random Forests
params = {'n_estimators' : [10,15,20,30],
    'max_depth' : [i for i in range(1,11)],
    'max_features': [i for i in range(3,8)],
    'min_samples_leaf': [i for i in range(5,9)]}
grid = GridSearchCV(RandomForestRegressor(random_state=3020), params, cv = 5, n_jobs = -1)
grid.fit(X_train,y_train)
print('Best Parameter Pairs: ', grid.best_params_)

def random_forests(numtrees, m):
    reg = RandomForestRegressor(n_estimators = numtrees, max_depth = 7, min_samples_leaf = 5, 
                                max_features = m, random_state = 3020)
    reg.fit(X_train, y_train)
    y_train_pred = reg.predict(X_train)
    train_MSE = metrics.mean_squared_error(y_train, y_train_pred)
    y_test_pred = reg.predict(X_test)
    test_MSE = metrics.mean_squared_error(y_test, y_test_pred)
    return train_MSE, test_MSE

diff_numtree = pd.DataFrame(columns = ['numtrees', 'train_MSE', 'test_MSE'])
for i in range(1,101):
    train_mse, test_mse = random_forests(i, 7)
    chart = [i, train_mse, test_mse]
    diff_numtree.loc[len(diff_numtree)] = chart

plt.plot(diff_numtree['numtrees'], diff_numtree['train_MSE'], color = 'r', label = 'Training_MSE')
plt.plot(diff_numtree['numtrees'], diff_numtree['test_MSE'], color = 'b', label = 'Testing_MSE')
plt.xlabel('Number of Trees')
plt.ylabel('MSE')
plt.title('Plot of MSE and Number of Trees')
plt.legend(loc = "best")
plt.show()

diff_m = pd.DataFrame(columns = ['m', 'train_MSE', 'test_MSE'])
for i in range(1,11):
    train_mse, test_mse = random_forests(20, i)
    chart = [i, train_mse, test_mse]
    diff_m.loc[len(diff_m)] = chart

plt.plot(diff_m['m'], diff_m['train_MSE'], color = 'r', label = 'Training_MSE')
plt.plot(diff_m['m'], diff_m['test_MSE'], color = 'b', label = 'Testing_MSE')
plt.xlabel('The number of candidate attributes')
plt.ylabel('MSE')
plt.title('Plot of MSE and Number of candidate attributes')
plt.legend(loc = "best")
plt.show()

# Bias and Variance
result = pd.DataFrame(columns = ['numtrees','square_bias','variance'])
for numtrees in range(10,101,10):
    reg = RandomForestRegressor(n_estimators = numtrees, max_depth = 7, min_samples_leaf = 5, 
                            max_features = 7, random_state = 3020)
    reg.fit(X_train, y_train)
    y_test_pred = reg.predict(X_test)
    y_test_avg = np.mean(y_test_pred)
    y_test_avg = np.full(len(y_test_pred), y_test_avg)
    test_bias = np.mean((y_test_pred - y_test)**2)
    test_var = 0
    for estimator in range(numtrees):
        subtree = reg.estimators_[estimator]
        y_sub_pred = subtree.predict(X_test)
        var = np.sum((y_sub_pred - y_test_pred)**2) / len(y_sub_pred)
        test_var += var
    test_var /= numtrees**2
    chart = [numtrees, test_bias, test_var]
    result.loc[len(result)] = chart
    
plt.plot(result['numtrees'], result['square_bias'])
plt.title("Relationship between bias^2 and number of trees")
plt.xlabel("Number of trees")
plt.ylabel("Bias^2")
plt.show()

plt.plot(result['numtrees'], result['variance'])
plt.title("Relationship between variance and number of trees")
plt.xlabel("Number of trees")
plt.ylabel("variance")
plt.show()


# reg = RandomForestRegressor(n_estimators = 10, max_depth = 7, min_samples_leaf = 5, 
#                             max_features = 7, random_state = 3020)
# reg.fit(X_train, y_train)
# y_test_pred = reg.predict(X_test)
# y_test_avg = np.mean(y_test_pred)
# y_test_avg = np.full(len(y_test_pred), y_test_avg)
# test_bias = np.mean((y_test_pred - y_test)**2)
# test_var = 0
# for estimator in range(10):
#     subtree = reg.estimators_[estimator]
#     y_sub_pred = subtree.predict(X_test)
#     var = np.sum((y_sub_pred - y_test_pred)**2) / len(y_sub_pred)
#     test_var += var
# test_var /= 10**2
# chart = []


# from mlxtend.evaluate import bias_variance_decomp
# X_train = X_train.values
# X_test = X_test.values
# y_train = y_train.values
# y_test = y_test.values
# result = pd.DataFrame(columns = ['numtrees','square_bias','variance'])
# for numtrees in range(10,101,10):
#     reg = RandomForestRegressor(n_estimators = numtrees, max_depth = 7, min_samples_leaf = 5, max_features = 7, n_jobs = -1)
#     avg_expected_loss, avg_bias, avg_var = bias_variance_decomp(
#             reg, X_train, y_train, X_test, y_test, 
#             loss='mse',
#             random_seed=3020)
#     chart = [numtrees, avg_bias, avg_var]
#     result.loc[len(result)] = chart
# plt.plot(result['numtrees'], result['square_bias'])
# plt.title("Relationship between bias^2 and number of trees")
# plt.xlabel("Number of trees")
# plt.ylabel("Bias^2")
# plt.show()








