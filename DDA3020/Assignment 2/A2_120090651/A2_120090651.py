# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:50:23 2022

@author: Mark
"""

import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier

def delete_bracket_for_w(lst):
    output = [float(round(x, 8)) for i in lst for x in i]
    return output

def delete_bracket_for_b(lst):
    output = ','.join(str(round(i, 8)) for i in lst)
    return output

train = pd.read_table('./train.txt', sep = '\t')
test = pd.read_table('./test.txt', sep = '\t')

X_train = train.iloc[:, 1:].to_numpy()
y_train = train.iloc[:, 0].to_numpy()
X_test = test.iloc[:, 1:].to_numpy()
y_test = test.iloc[:, 0].to_numpy()

#%% Question 1
model_1 = OneVsRestClassifier(SVC(C = 1e5, kernel = 'linear', random_state = 3020))
model_1.fit(X_train,y_train)
train_y_pred = model_1.predict(X_train)
test_y_pred = model_1.predict(X_test)
training_error = (train_y_pred != y_train).sum() / len(y_train)
testing_error = (test_y_pred != y_test).sum() / len(y_test)

file = open("SVM_linear.txt", 'w')
str1 = "training error: " + str(training_error)
str2 = "testing_error: " + str(testing_error)
inter3 = delete_bracket_for_b(delete_bracket_for_w(model_1.estimators_[0].coef_.tolist()))
str3 = "w_of_setosa: " + inter3
str4 = "b_of_setosa: " + str(round(model_1.estimators_[0].intercept_[0],8))
inter5 = delete_bracket_for_b(model_1.estimators_[0].support_.tolist())
str5 = "support_vector_indices_of_setosa: " + inter5
inter6 = delete_bracket_for_b(delete_bracket_for_w(model_1.estimators_[1].coef_.tolist()))
str6 = "w_of_versicolor: " + inter6
str7 = "b_of_versicolor: " + str(round(model_1.estimators_[1].intercept_[0],8))
inter8 = delete_bracket_for_b(model_1.estimators_[1].support_.tolist())
str8 = "support_vector_indices_of_versicolor: " + inter8
inter9 = delete_bracket_for_b(delete_bracket_for_w(model_1.estimators_[2].coef_.tolist()))
str9 = "w_of_virginica: " + inter9
str10 = "b_of_virginica: " + str(round(model_1.estimators_[2].intercept_[0],8))
inter11 = delete_bracket_for_b(model_1.estimators_[2].support_.tolist())
str11 = "support_vector_indices_of_virginica: " + inter11

strlist = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11]
for rows in strlist:
    file.write(rows)
    file.write('\n')
    
file.close()

y_train_mod = y_train.copy()
y_train_mod = np.where(y_train_mod == 0, 1, 0)
train_loss0 = 1 - model_1.estimators_[0].score(X_train, y_train_mod)
res0 = (train_loss0 == 0)

y_train_mod = y_train.copy()
y_train_mod = np.where(y_train_mod == 1, 1, 0)
train_loss1 = 1 - model_1.estimators_[1].score(X_train, y_train_mod)
res1 = (train_loss1 == 0)

y_train_mod = y_train.copy()
y_train_mod = np.where(y_train_mod == 2, 1, 0)
train_loss2 = 1 - model_1.estimators_[2].score(X_train, y_train_mod)
res2 = (train_loss2 == 0)

print(f"Label 0 linearly separable: {res0}")
print("train_loss for label 0: " + str(train_loss0))
print(f"Label 1 linearly separable: {res1}")
print("train_loss for label 1: " + str(train_loss1))
print(f"Label 2 linearly separable: {res2}")
print("train_loss for label 2: " + str(train_loss2))

#%% Question 2
def slack_var(model, est_index):
    svm = model.estimators_[est_index]
    distance = svm.decision_function(X_train)
    label = y_train.copy()
    indicator = np.where(label == est_index, 1, -1)
    ones = np.ones(len(y_train))
    slack = ones - indicator*distance
    slack = np.where(slack>0, slack, 0)
    return slack

file = open("SVM_slack.txt", 'a')
for t in range(1,11):
    model_2 = OneVsRestClassifier(SVC(C = 0.1*t, kernel = 'linear', random_state = 3020))
    model_2.fit(X_train,y_train)
    train_y_pred = model_2.predict(X_train)
    test_y_pred = model_2.predict(X_test)
    training_error = (train_y_pred != y_train).sum() / len(y_train)
    testing_error = (test_y_pred != y_test).sum() / len(y_test)
    para = round(0.1*t, 1)
    title = f'----- SVM with slack variable C={para}-----'
    file.write(title)
    file.write('\n')
    str1 = "training error: " + str(training_error)
    str2 = "testing_error: " + str(testing_error)
    inter3 = delete_bracket_for_b(delete_bracket_for_w(model_2.estimators_[0].coef_.tolist()))
    str3 = "w_of_setosa: " + inter3
    str4 = "b_of_setosa: " + str(round(model_2.estimators_[0].intercept_[0],8))
    inter5 = delete_bracket_for_b(model_2.estimators_[0].support_.tolist())
    str5 = "support_vector_indices_of_setosa: " + inter5
    slack1 = "slack_variable_of_setosa: " + delete_bracket_for_b(slack_var(model_2, 0).tolist())
    inter6 = delete_bracket_for_b(delete_bracket_for_w(model_2.estimators_[1].coef_.tolist()))
    str6 = "w_of_versicolor: " + inter6
    str7 = "b_of_versicolor: " + str(round(model_2.estimators_[1].intercept_[0],8))
    inter8 = delete_bracket_for_b(model_2.estimators_[1].support_.tolist())
    str8 = "support_vector_indices_of_versicolor: " + inter8
    slack2 = "slack_variable_of_versicolor: " + delete_bracket_for_b(slack_var(model_2, 1).tolist())
    inter9 = delete_bracket_for_b(delete_bracket_for_w(model_2.estimators_[2].coef_.tolist()))
    str9 = "w_of_virginica: " + inter9
    str10 = "b_of_virginica: " + str(round(model_2.estimators_[2].intercept_[0],8))
    inter11 = delete_bracket_for_b(model_2.estimators_[2].support_.tolist())
    str11 = "support_vector_indices_of_virginica: " + inter11
    slack3 = "slack_variable_of_virginica: " + delete_bracket_for_b(slack_var(model_2, 2).tolist())
    strlist = [str1, str2, str3, str4, str5, slack1, str6, str7, str8, slack2, str9, str10, str11, slack3]
    for rows in strlist:
        file.write(rows)
        file.write('\n')
        
file.close()

#%% Question 3

#Problem a
model_3 = OneVsRestClassifier(SVC(C = 1, kernel = 'poly', degree = 2, gamma = 1,random_state = 3020))
model_3.fit(X_train, y_train)
train_y_pred = model_3.predict(X_train)
test_y_pred = model_3.predict(X_test)
training_error = (train_y_pred != y_train).sum() / len(y_train)
testing_error = (test_y_pred != y_test).sum() / len(y_test)
file = open("SVM_poly2.txt", 'w')
str1 = "training error: " + str(training_error)
str2 = "testing_error: " + str(testing_error)
str4 = "b_of_setosa: " + str(round(model_3.estimators_[0].intercept_[0],8))
inter5 = delete_bracket_for_b(model_3.estimators_[0].support_.tolist())
str5 = "support_vector_indices_of_setosa: " + inter5
str7 = "b_of_versicolor: " + str(round(model_3.estimators_[1].intercept_[0],8))
inter8 = delete_bracket_for_b(model_3.estimators_[1].support_.tolist())
str8 = "support_vector_indices_of_versicolor: " + inter8
str10 = "b_of_virginica: " + str(round(model_3.estimators_[2].intercept_[0],8))
inter11 = delete_bracket_for_b(model_3.estimators_[2].support_.tolist())
str11 = "support_vector_indices_of_virginica: " + inter11

strlist = [str1, str2, str4, str5, str7, str8, str10, str11]
for rows in strlist:
    file.write(rows)
    file.write('\n')
    
file.close()

#Problem b
model_3 = OneVsRestClassifier(SVC(C = 1, kernel = 'poly', degree = 3, gamma = 1, random_state = 3020))
model_3.fit(X_train, y_train)
train_y_pred = model_3.predict(X_train)
test_y_pred = model_3.predict(X_test)
training_error = (train_y_pred != y_train).sum() / len(y_train)
testing_error = (test_y_pred != y_test).sum() / len(y_test)
file = open("SVM_poly3.txt", 'w')
str1 = "training error: " + str(training_error)
str2 = "testing_error: " + str(testing_error)
str4 = "b_of_setosa: " + str(round(model_3.estimators_[0].intercept_[0],8))
inter5 = delete_bracket_for_b(model_3.estimators_[0].support_.tolist())
str5 = "support_vector_indices_of_setosa: " + inter5
str7 = "b_of_versicolor: " + str(round(model_3.estimators_[1].intercept_[0],8))
inter8 = delete_bracket_for_b(model_3.estimators_[1].support_.tolist())
str8 = "support_vector_indices_of_versicolor: " + inter8
str10 = "b_of_virginica: " + str(round(model_3.estimators_[2].intercept_[0],8))
inter11 = delete_bracket_for_b(model_3.estimators_[2].support_.tolist())
str11 = "support_vector_indices_of_virginica: " + inter11

strlist = [str1, str2, str4, str5, str7, str8, str10, str11]
for rows in strlist:
    file.write(rows)
    file.write('\n')
    
file.close()

#Problem c
model_3 = OneVsRestClassifier(SVC(C = 1, kernel = 'rbf', gamma = 0.5, random_state = 3020))
model_3.fit(X_train, y_train)
train_y_pred = model_3.predict(X_train)
test_y_pred = model_3.predict(X_test)
training_error = (train_y_pred != y_train).sum() / len(y_train)
testing_error = (test_y_pred != y_test).sum() / len(y_test)
file = open("SVM_rbf.txt", 'w')
str1 = "training error: " + str(training_error)
str2 = "testing_error: " + str(testing_error)
str4 = "b_of_setosa: " + str(round(model_3.estimators_[0].intercept_[0],8))
inter5 = delete_bracket_for_b(model_3.estimators_[0].support_.tolist())
str5 = "support_vector_indices_of_setosa: " + inter5
str7 = "b_of_versicolor: " + str(round(model_3.estimators_[1].intercept_[0],8))
inter8 = delete_bracket_for_b(model_3.estimators_[1].support_.tolist())
str8 = "support_vector_indices_of_versicolor: " + inter8
str10 = "b_of_virginica: " + str(round(model_3.estimators_[2].intercept_[0],8))
inter11 = delete_bracket_for_b(model_3.estimators_[2].support_.tolist())
str11 = "support_vector_indices_of_virginica: " + inter11

strlist = [str1, str2, str4, str5, str7, str8, str10, str11]
for rows in strlist:
    file.write(rows)
    file.write('\n')
    
file.close()

#Problem d
model_3 = OneVsRestClassifier(SVC(C = 1, kernel = 'sigmoid', gamma = 'auto',random_state = 3020))
model_3.fit(X_train, y_train)
train_y_pred = model_3.predict(X_train)
test_y_pred = model_3.predict(X_test)
training_error = (train_y_pred != y_train).sum() / len(y_train)
testing_error = (test_y_pred != y_test).sum() / len(y_test)
file = open("SVM_sigmoid.txt", 'w')
str1 = "training error: " + str(training_error)
str2 = "testing_error: " + str(testing_error)
str4 = "b_of_setosa: " + str(round(model_3.estimators_[0].intercept_[0],8))
inter5 = delete_bracket_for_b(model_3.estimators_[0].support_.tolist())
str5 = "support_vector_indices_of_setosa: " + inter5
str7 = "b_of_versicolor: " + str(round(model_3.estimators_[1].intercept_[0],8))
inter8 = delete_bracket_for_b(model_3.estimators_[1].support_.tolist())
str8 = "support_vector_indices_of_versicolor: " + inter8
str10 = "b_of_virginica: " + str(round(model_3.estimators_[2].intercept_[0],8))
inter11 = delete_bracket_for_b(model_3.estimators_[2].support_.tolist())
str11 = "support_vector_indices_of_virginica: " + inter11

strlist = [str1, str2, str4, str5, str7, str8, str10, str11]
for rows in strlist:
    file.write(rows)
    file.write('\n')
    
file.close()

