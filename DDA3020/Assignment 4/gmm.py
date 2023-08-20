# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:58:30 2022

@author: Mark
"""

from sklearn.utils import shuffle
import numpy as np
from scipy.special import logsumexp
from scipy.stats import multivariate_normal

def compute_distance(x, y):
    return np.linalg.norm(y-x)

def initialize_para(data, K):
    pi = [1 / K] * K
    split_data = np.array_split(data, K)
    mu = [np.mean(split, axis = 0) for split in split_data]
    sigma = [np.cov(split.T) for split in split_data]
    return pi, mu, sigma

def predict(data, K, pi, mu, sigma):
    gamma = np.zeros((len(data), K))
    for n in range(len(data)):
        for k in range(K):
            num = pi[k] * multivariate_normal.pdf(data[n], mu[k], sigma[k])
            deno = []
            for j in range(K):
                element = pi[j] * multivariate_normal.pdf(data[n], mu[j], sigma[j])
                deno.append(element)
            gamma[n][k] = num / logsumexp(deno)
        label = []
        for i in range(len(data)):
            l = np.argmax(gamma[i])
            label.append(l)
    return label
    
def fit(data, K, pi, mu, sigma, tol):
    flag = True
    while flag:
        gamma = np.zeros((len(data), K))
        for n in range(len(data)):
            for k in range(K):
                num = pi[k] * multivariate_normal.pdf(data[n], mu[k], sigma[k])
                deno = []
                for j in range(K):
                    element = pi[j] * multivariate_normal.pdf(data[n], mu[j], sigma[j])
                    deno.append(element)
                gamma[n][k] = num / logsumexp(deno)
        N = np.sum(gamma, axis = 0)
        for k in range(K):
            musum = 0
            for n in range(len(data)):
                musum += gamma[n][k] * data[n]
            mu[k] = musum / N[k]
        for k in range(K):
            musum = 0
            for n in range(len(data)):
                musum += gamma[n][k] * np.outer((data[n] - mu[k]), (data[n] - mu[k]).T)
            sigma[k] = musum / N[k]
        prev = list(pi)
        pi = [N[k] / len(data) for k in range(K)]
        diffsum = 0
        for i in range(len(prev)):
            diffsum += (prev[i] - pi[i])**2
        if diffsum <= tol:
            flag = False
    return pi, mu, sigma

def get_curr_clusters(label, data, K):
    labelarr = np.array(label)
    labelarr = labelarr[:,np.newaxis]
    new = np.hstack((data, labelarr))
    current_clusters = {}
    for i in range(K):
        current_clusters[i] = []
    for i in range(len(data)):
        if new[i, 7] == 0:
            current_clusters[0].append(data[i, :7])
        elif new[i, 7] == 1:
            current_clusters[1].append(data[i, :7])
        elif new[i, 7] == 2:
            current_clusters[2].append(data[i, :7])
    return current_clusters

def silhouette_coefficient(current_clusters, K):
    coeflist = []
    for i in range(K):
        near_num = [m for m in range(K)]
        near_num.remove(i)
        for j in current_clusters[i]:
            a = 0
            for k in current_clusters[i]:
                if np.array_equal(j, k) == False:
                    a += compute_distance(j, k)
            a = a / (len(current_clusters[i])-1)
            b1 = []
            for m in near_num:
                blst = []
                for n in current_clusters[m]:
                    blst.append(compute_distance(j, n))
                bsum = sum(blst)/len(blst)
                b1.append(bsum)
            b = min(b1)
            s = (b - a) / max(a, b)
            coeflist.append(s)
    return sum(coeflist)/210

def rand_index(current_clusters, txt, K):
    predictlist = []
    for i in range(len(current_clusters)):
        for j in current_clusters[i]:
            j = np.insert(j, 7, i)
            predictlist.append(j)
    matrix = np.stack(predictlist, axis = 0)
    r1 = np.core.records.fromarrays([matrix[:,1],matrix[:,0]],names='a,b')
    matrix = matrix[r1.argsort()]
    r2 = np.core.records.fromarrays([txt[:,1],txt[:,0]],names='a,b')
    txt_new = txt[r2.argsort()]
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if (matrix[i, 7] == matrix[j, 7]) & (txt_new[i, 7] == txt_new[j, 7]):
                a += 1
            elif (matrix[i, 7] != matrix[j, 7]) & (txt_new[i, 7] != txt_new[j, 7]):
                b += 1
            elif (matrix[i, 7] == matrix[j, 7]) & (txt_new[i, 7] != txt_new[j, 7]):
                c += 1
            elif (matrix[i, 7] != matrix[j, 7]) & (txt_new[i, 7] == txt_new[j, 7]):
                d += 1
    RI = (a + b) / (a + b + c + d)
    return RI

def main():
    txt = np.loadtxt(r'./seeds_dataset.txt', dtype = float)
    X = txt[:, :7]
    for i in range(10):
        X = shuffle(X)
        pi, mu, sigma = initialize_para(X, 3)
        pi, mu, sigma = fit(X, 3, pi, mu, sigma, 0.000001)
        label = predict(X, 3, pi, mu, sigma)
        current_clusters = get_curr_clusters(label, X, 3)
        print(silhouette_coefficient(current_clusters, 3))
        print(rand_index(current_clusters, txt, 3))

# main()
# txt = np.loadtxt(r'./seeds_dataset.txt', dtype = float)
# X = txt[:, :7]
# K = 3
# pi = [1 / K] * K
# split_data = np.array_split(X, K)
# mu = [np.mean(split, axis = 0) for split in split_data]
# sigma = [np.cov(split.T) for split in split_data]

from sklearn.metrics.cluster import rand_score
from sklearn import mixture
txt = np.loadtxt(r'./seeds_dataset.txt', dtype = float)
X = txt[:, :7]
y = txt[:, 7]
gmm = mixture.GaussianMixture(n_components=3).fit(X)
pred = gmm.predict(X)
true = y
print(rand_score(true, pred))

