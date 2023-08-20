# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:02:35 2022

@author: Mark
"""

import pandas as pd
import numpy as np
import random

txt = np.loadtxt(r'./seeds_dataset.txt', dtype = float)
X = txt[:, :7]
y = txt[:, 7]

def compute_distance(x, y):
    return np.linalg.norm(y-x)

def initialize_centroid(data, K):
    data = list(data)
    init_centroid = random.sample(data, K)
    return init_centroid

def assign_centroids(curr_cluster, K):
    centroids = []
    for idx in range(K):
        centroid = np.mean(curr_cluster[idx], axis = 0)
        centroids.append(centroid)
    return centroids

def assign_cluster(data, curr_centroids, K):
    curr_cluster = {}
    for i in data:
        curr_min_dist = 1e8
        clusteridx = -1
        for j in range(K):
            centroid = curr_centroids[j]
            curr_dist = compute_distance(i, centroid)
            if curr_dist < curr_min_dist:
                curr_min_dist = curr_dist
                clusteridx = j
            if clusteridx not in curr_cluster.keys():
                curr_cluster[clusteridx] = []
        curr_cluster[clusteridx].append(i)
    return curr_cluster

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

def fit(k, tolerence):
    K = k
    tol = tolerence
    centroids = initialize_centroid(X, K)
    current_clusters = assign_cluster(X, centroids, K)
    loop = True
    while loop:
        prev = centroids
        centroids = assign_centroids(current_clusters, K)
        current_clusters = assign_cluster(X, centroids, K)
        dist_sum = 0
        for i in range(len(centroids)):
            dist_sum += compute_distance(prev[i], centroids[i])
        if dist_sum < tol:
            loop = False
    sil = silhouette_coefficient(current_clusters, K)
    ran = rand_index(current_clusters, txt, K)
    return sil, ran

# def performance_evaluation(k ,tol):
#     result = pd.DataFrame(columns = ['silhouette_coef', 'rand_index'])
#     for i in range(10):
#         sil, ran = fit(k ,tol)
#         chart = [sil, ran]
#         result.loc[len(result)] = chart
#     return result

# res = performance_evaluation(3, 0.000001)
# sil_std = res['silhouette_coef'].std()
# ran_std = res['rand_index'].std()


from sklearn.metrics.cluster import rand_score
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3).fit(X)
true = y
pred = kmeans.predict(X)
rand_score(true, pred)


