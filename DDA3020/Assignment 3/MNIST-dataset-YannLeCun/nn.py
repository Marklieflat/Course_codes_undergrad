# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:53:32 2022

@author: Mark
"""

import pandas as pd
import os 
import numpy as np
import gzip
from sklearn.neural_network import MLPClassifier
# from sklearn.model_selection import GridSearchCV

def load_mnist(path ='./', flatten = False, binary_data = False):
    RESOURCES = [
        'train-images-idx3-ubyte.gz',
        'train-labels-idx1-ubyte.gz',
        't10k-images-idx3-ubyte.gz',
        't10k-labels-idx1-ubyte.gz']
    if binary_data:
       X,Y = get_images(path,binary_data), get_labels(path) 
    else: 
        X,Y = get_images(path), get_labels(path)
    X_train, X_test = X
    Y_train, Y_test = Y
    del X, Y  # free up memory
    assert X_train.shape == (60000, 28, 28)
    assert X_test.shape == (10000, 28, 28)
    assert Y_train.shape == (60000,)
    assert Y_test.shape == (10000,)
    if flatten:
        X_train = X_train.reshape(-1, 784)
        X_test = X_test.reshape(-1, 784) 
    return X_train, X_test, Y_train, Y_test

def get_images(path = './',binary_data = False):
    to_return = []
    with gzip.open(path + 'train-images-idx3-ubyte.gz', 'r') as f:
        magic_number = int.from_bytes(f.read(4), 'big')
        image_count = int.from_bytes(f.read(4), 'big')
        row_count = int.from_bytes(f.read(4), 'big')
        column_count = int.from_bytes(f.read(4), 'big')
        image_data = f.read()
        train_images = np.frombuffer(image_data, dtype=np.uint8)\
            .reshape((image_count, row_count, column_count))
        if binary_data:
            to_return.append(np.where(train_images > 127, 1, 0))
        else:
            to_return.append(train_images)
    with gzip.open(path + 't10k-images-idx3-ubyte.gz', 'r') as f:
        magic_number = int.from_bytes(f.read(4), 'big')
        image_count = int.from_bytes(f.read(4), 'big')
        row_count = int.from_bytes(f.read(4), 'big')
        column_count = int.from_bytes(f.read(4), 'big')
        image_data = f.read()
        test_images = np.frombuffer(image_data, dtype=np.uint8)\
            .reshape((image_count, row_count, column_count))
        if binary_data:
            to_return.append(np.where(test_images > 127, 1, 0))
        else:
            to_return.append(test_images)
    return to_return

def get_labels(path = './'):
    to_return = []
    with gzip.open(path + 'train-labels-idx1-ubyte.gz', 'r') as f:
        magic_number = int.from_bytes(f.read(4), 'big')
        label_count = int.from_bytes(f.read(4), 'big')
        label_data = f.read()
        train_labels = np.frombuffer(label_data, dtype=np.uint8)
        to_return.append(train_labels)
    with gzip.open(path + 't10k-labels-idx1-ubyte.gz', 'r') as f:
        magic_number = int.from_bytes(f.read(4), 'big')
        label_count = int.from_bytes(f.read(4), 'big')
        label_data = f.read()
        test_labels = np.frombuffer(label_data, dtype=np.uint8)
        to_return.append(test_labels)
    return to_return

X_train,X_test,Y_train,Y_test  = load_mnist(path = './', flatten = False,binary_data = True)
assert X_train.shape == (60000, 28, 28)
assert X_test.shape == (10000, 28, 28)
assert Y_train.shape == (60000,)
assert Y_test.shape == (10000,)
X_train,X_test,Y_train,Y_test  = load_mnist(path = './', flatten = True,binary_data = True) 
assert X_train.shape == (60000, 784)
assert X_test.shape == (10000, 784)
assert Y_train.shape == (60000,)
assert Y_test.shape == (10000,)
X_train,X_test,Y_train,Y_test  = load_mnist(path = './', flatten = True, binary_data=False) 
assert X_train.shape == (60000, 784)
assert X_test.shape == (10000, 784)
assert Y_train.shape == (60000,)
assert Y_test.shape == (10000,)
print("Test passed and data loaded successfully.")

# Training and Testing
# param = {'hidden_layer_sizes':[(50,),(200,),(784,),(50,50),(200,200),(784,784),(50,50,50),
#                                (200,200,200),(784,784,784)]}
# mlp_gs = MLPClassifier(activation = 'relu', solver = 'adam', 
#         random_state = 3020, max_iter = 10, verbose = False, learning_rate_init = 3e-4, alpha = 0.05)
# clf = GridSearchCV(mlp_gs, param, n_jobs=-1, cv=5)
# clf.fit(X_train, Y_train)
# print('Best Parameter Pairs: ', clf.best_params_)


# para = [(50,),(200,),(784,),(50,50),(200,200),(784,784),(50,50,50),(200,200,200),(784,784,784)]
# mlp = MLPClassifier(solver = 'adam', activation = 'relu', alpha = 0.05, hidden_layer_sizes = (784,784), 
#                     random_state = 3020, max_iter = 10, verbose = False, learning_rate_init = 3e-4)
# # mlp = MLPClassifier()
# mlp.fit(X_train, Y_train)
# print(mlp.score(X_test,Y_test))
# print(mlp.n_layers_)
# print(mlp.best_loss_)

res = pd.DataFrame(columns = ['n hidden nodes', 'n hidden layers', 'score', 'min loss'])

mlp = MLPClassifier(solver = 'adam', activation = 'relu', alpha = 0.05, hidden_layer_sizes = (784,784), 
                        random_state = 3020, max_iter = 50, verbose = False, learning_rate_init = 3e-4)
mlp.fit(X_train, Y_train)
chart = [(784,784)[0], len((784,784)), mlp.score(X_test,Y_test), mlp.best_loss_]
res.loc[len(res)] = chart


# mlp = MLPClassifier(hidden_layer_sizes=(784,784,784), max_iter=100, alpha=1e-4,
#                     solver='sgd', verbose=10, tol=1e-4, random_state=1,
#                     learning_rate_init=.1)

# mlp.fit(X_train, Y_train)
# print("Training set score: %f" % mlp.score(X_train, Y_train))
# print("Test set score: %f" % mlp.score(X_test, Y_test))























