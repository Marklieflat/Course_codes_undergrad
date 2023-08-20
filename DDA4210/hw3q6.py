# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:36:09 2023

@author: Mark
"""

import math

def v_val(S):
    if 1 in S:
        a = 1
    else: a = 0
    if 2 in S:
        b = 1
    else: b = 0
    if 3 in S:
        c = 1
    else: c = 0
    if 4 in S:
        d = 1
    else: d = 0
    if 5 in S:
        e = 1
    else: e = 0
    value = 2*b + 3*c + 4*d + 5*a*c + 7*b*e - 12*a*b*c
    return value

# print(v_val({1,2,3,4}))

def get_subset(S):
    res = [[]]
    for i in S:
        for element in res[:]:
            x = element[:]
            x.append(i)
            res.append(x)
    return res

# print(get_subset({1,2,3}))
        
def shapley_val(i):
    playerset = {1,2,3,4,5}
    modset = playerset.copy()
    modset.remove(i)
    sub = get_subset(modset)
    val = 0
    for j in sub:
        x = j.copy()
        x.append(i)
        val += (math.factorial(len(j))*math.factorial((5-1-len(j)))/math.factorial(5))*(v_val(x)-v_val(j))
    return val

print(shapley_val(5))

# playerset = {1,2,3,4,5}
# modset = playerset.copy()
# modset.remove(1)
# sub = get_subset(modset)
# val = 0
# for j in sub:
#     x = j.copy()
#     x.append(1)
#     val += (math.factorial(len(j))*math.factorial((5-1-len(j)))/math.factorial(5))*(v_val(x)-v_val(j))






