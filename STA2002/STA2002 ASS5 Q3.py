# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 00:48:14 2021

@author: Mark
"""

inputs = input('please enter the number:')
lst = inputs.split(' ')
lst.sort()
lsts = []
for i in range(0,len(lst),3):
    temlst = lst[i:i+3]
    lsts.append(temlst)
print(lsts)