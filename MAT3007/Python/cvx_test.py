# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 19:54:51 2022

@author: Mark
"""

import cvxpy as cp

def main():
    x = cp.Variable()
    y = cp.Variable()
    obj = cp.Maximize(6*x+5*y)
    consts = [x+y<=5, 3*x+2*y<=12, x>=0, y>=0]
    prob = cp.Problem(obj,consts)
    result = prob.solve()
    print(result)
    
if __name__ == '__main__':
    main()