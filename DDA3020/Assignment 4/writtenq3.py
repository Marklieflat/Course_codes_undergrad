# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:35:19 2022

@author: Mark
"""

import numpy as np

X = np.array([[2,0,1,-3,-2],
              [0,2,-3,-3,-2],
              [1,2,1,3,-2],
              [-1,1,3,2,-1],
              [1,0,1,-1,1],
              [2,3,-1,1,-2],
              [-2,3,-3,3,2],
              [-2,-2,2,3,-2],
              [-2,-3,1,-2,-3],
              [-3,2,0,-1,-2]])

X = X.T
mu = np.mean(X, axis = 1)
cov_matrix = np.cov(X, ddof = 0)
eigen = np.linalg.eig(cov_matrix)
eigenvalue = eigen[0]
eigenvector = eigen[1]
U = eigenvector[:, 3:]
mumatrix = np.array([mu]*10).T
new = np.dot(U.T, (X-mumatrix))

print(mu)
print(cov_matrix)
print(eigenvalue)
print(eigenvector)
print(new)
# print(X-mumatrix)