from re import S
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import solve
from numpy.linalg import norm

def golden_section_method(maxit, a, x, tol, obj, grad):
    left = 0
    right = a
    phi = (3 - np.sqrt(5)) / 2
    interation = 0
    while right - left > tol and interation < maxit:
        left_ = phi * right + (1 - phi) * left
        right_ = phi * left + (1 - phi) * right
        if obj(x - [i * left_ for i in grad(x)]) < obj(x -  [i * right_  for i in grad(x)]):
            right = right_
        else:
            left = left_
    alpha_final = (left + right) / 2
    return alpha_final

def gradient_method_exactLineSearch(x0, tol, maxit, a, obj, grad):
    x = x0
    iteration = 1
    all_x = list()
    all_x.append(x0)
    while norm(grad(x)) > tol:
        left = 0
        right = a
        phi = (3 - np.sqrt(5)) / 2
        interation = 0
        while right - left > tol and interation < maxit:
            left_ = phi * right + (1 - phi) * left
            right_ = phi * left + (1 - phi) * right
            if obj_poly(x - [i * left_ for i in grad_poly(x)]) < obj_poly(x -  [i * right_  for i in grad_poly(x)]):
                right = right_
            else:
                left = left_
        alpha_final = (left + right) / 2
        alpha = alpha_final
        x = x - [i * alpha for i in grad(x)]
        all_x.append(x)
        iteration += 1
    return x, obj(x), iteration, all_x

def obj_poly(x):
    x1 = x[0]
    x2 = x[1]
    return x1**4 + (2/3) * (x1**3) + (1/2) * (x1 ** 2) - 2 * (x1**2) * x2 + (4/3) * (x2**2)

def grad_poly(x):
    x1 = x[0]
    x2 = x[1]
    grad1 = 4 * (x1**3) + 2 * (x1**2) + x1 - 4 * x1 * x2
    grad2 = -2 * (x1**2) + (8/3) * x2
    grad = [grad1, grad2]
    return grad


def figure():
    m1 = list()
    m2 = list()
    for X in all_x:
        m1.append(X[0])
        m2.append(X[1])
    plt.plot(m1, m2, marker = 'o', markersize = 3)

# x0 = np.array([-3, 3])
# print("Exact Line Search:")
# x, objective, itr, all_x = gradient_method_exactLineSearch(x0, 1e-5, 100, 2, obj_poly, grad_poly)
# print("x =", [float('{:.3f}'.format(i)) for i in x], "objective =", round(objective, 3), "number of iterations =", itr)

x0 = [np.array([-3, -3]), np.array([3, -3]), np.array([-3, 3]), np.array([3, 3])]
X1 = np.arange(-4.5, 4.5, 0.01)
X2 = np.arange(-4.5, 4.5, 0.01)
X1_, X2_ = np.meshgrid(X1, X2)

Y = X1**4 + (2/3) * (X1_**3) + (1/2) * (X1_ ** 2) - 2 * (X1_**2) * X2_ + (4/3) * (X2_**2)

plt.contour(X1_, X2_, Y, 25)
for i in x0:
    x, objective, itr, all_x = gradient_method_exactLineSearch(i, 1e-5, 100, 0.2, obj_poly, grad_poly)
    plt.contour(X1_, X2_, Y, 25)
    figure()
plt.title("Exact Line Search")
plt.show()