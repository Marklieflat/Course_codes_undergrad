from re import S
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import solve
from numpy.linalg import norm

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

def hess_poly(x):
    x1 = x[0]
    x2 = x[1]
    hessian = np.array([[12 * (x1**2) + 4 * x1 - 4 * x2 + 1, -4 * x1],
                        [-4 * x1, (8/3)]])
    return hessian

def obj_Rosenbrock(x):
    x1 = x[0]
    x2 = x[1]
    return 100 * (x2 - x1**2) ** 2 + (1 - x1) ** 2

def grad_Rosenbrock(x):
    x1 = x[0]
    x2 = x[1]
    grad1 = 400 * (x1 ** 3) - 400 * x2 * x1 + 2 * x1 - 2
    grad2 = -200 * (x1 ** 2) + 200 * x2
    grad = [grad1, grad2]
    return grad

def hess_Rosenbrock(x):
    x1 = x[0]
    x2 = x[1]
    hessian = np.array([[1200 * (x1**2) - 400 * x2 + 2, -400 * x1],
                        [-400 * x1, 200]])
    return hessian

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

def gradient_method_Armijo(x0, tol, sigma, gamma, obj, grad):
    x = x0
    all_x = list()
    all_x.append(x0)
    iteration = 0
    while norm(grad(x)) > tol:
        iteration += 1
        alpha = 1
        objective = obj(x)
        while obj(x - [i * alpha for i in grad(x)]) > objective - gamma * alpha * (norm(grad(x)) ** 2):
            alpha = sigma * alpha
        x = x - [i * alpha for i in grad(x)]
        all_x.append(x)

    return x, obj(x), iteration,all_x

def gradient_method_exactLineSearch(x0, tol, maxit, a, obj, grad):
    x = x0
    iteration = 1
    all_x = list()
    all_x.append(x0)
    while norm(grad(x)) > tol:
        alpha = golden_section_method(maxit, a, x, 1e-6, obj_poly, grad_poly)
        x = x - [i * alpha for i in grad(x)]
        all_x.append(x)
        iteration += 1
    return x, obj(x), iteration, all_x

def gradient_method_Adagrad(x0, tol, m, epsilon, sigma, gamma, obj, grad):
    x = x0
    all_x = list()
    all_x.append(x0)
    k = 0
    while norm(grad(x)) > tol:
        start = max(0, k - m)
        sum1 = 0
        sum2 = 0
        alpha = 1
        for j in range(start, k + 1):
            sum1 += grad(all_x[j])[0] ** 2
        for j in range(start, k + 1):
            sum2 += grad(all_x[j])[1] ** 2
        v1 = np.sqrt(epsilon + sum1)
        v2 = np.sqrt(epsilon + sum2)
        D = np.diag([v1, v2])
        d = -np.matmul(np.linalg.inv(D), grad(x))
        while obj(x + [i * alpha for i in d]) > obj(x) + gamma * alpha * np.dot(grad(x), d):
            alpha = sigma * alpha
        x = x + [alpha * i for i in d]
        all_x.append(x)
        k += 1
    return x, obj(x), k, all_x

def newton_glob(x0, tol, gamma, gamma1, gamma2, sigma, obj, grad, hess):
    x = x0
    iteration = 0
    flag_newton = 0 # judge if this method always uses Newton step
    flag_fullSize = 0 # judge if this method always uses the full step size
    all_x = list()
    all_x.append(x0)
    while norm(grad(x)) > tol:
        alpha = 1
        d =  np.array([i * (-1) for i in grad(x)])
        s = solve(hess(x), d)
        if np.dot(d, s) >= gamma1 * min(1, norm(s) ** gamma2) * norm(s) ** 2:
            d = s
        else:
            flag_newton = 1
        while obj(x + [i * alpha for i in d]) > obj(x) + gamma * alpha * np.dot(grad(x), d):
            alpha = sigma * alpha
            flag_fullSize = 1
        x = x + [alpha * i for i in d]
        all_x.append(x)
        iteration += 1
    return x, obj(x), iteration, all_x, flag_newton, flag_fullSize

def figure():
    m1 = list()
    m2 = list()
    for X in all_x:
        m1.append(X[0])
        m2.append(X[1])
    plt.plot(m1, m2, marker = 'o', markersize = 3)

# 2 part(a)
print("Problem 2(a):")
x0 = np.array([3, 3])

print("Backtracking:")
x, objective, itr, all_x = gradient_method_Armijo(x0, 1e-5, 0.5, 0.1, obj_poly, grad_poly)
print("x =", [float('{:.3f}'.format(i)) for i in x], "objective =", round(objective, 3), "number of iterations =", itr)
 
print("Exact Line Search:")
x, objective, itr, all_x = gradient_method_exactLineSearch(x0, 1e-5, 100, 2, obj_poly, grad_poly)
print("x =", [float('{:.3f}'.format(i)) for i in x], "objective =", round(objective, 3), "number of iterations =", itr)

# 2 part(b)
x0 = [np.array([-3, -3]), np.array([3, -3]), np.array([-3, 3]), np.array([3, 3])]
X1 = np.arange(-4.5, 4.5, 0.01)
X2 = np.arange(-4.5, 4.5, 0.01)
X1_, X2_ = np.meshgrid(X1, X2)

Y = X1**4 + (2/3) * (X1_**3) + (1/2) * (X1_ ** 2) - 2 * (X1_**2) * X2_ + (4/3) * (X2_**2)

plt.contour(X1_, X2_, Y, 25)
for i in x0:
    x, objective, itr, all_x = gradient_method_Armijo(i, 1e-5, 0.5, 0.1, obj_poly, grad_poly)
    figure()
plt.title("Backtracking")
plt.show()
    

plt.contour(X1_, X2_, Y, 25)
for i in x0:
    x, objective, itr, all_x = gradient_method_exactLineSearch(i, 1e-5, 100, 0.2, obj_poly, grad_poly)
    plt.contour(X1_, X2_, Y, 25)
    figure()
plt.title("Exact Line Search")
plt.show()

# 3 part(b)
plt.contour(X1_, X2_, Y, 25)
for i in x0:
    x, objective, itr, all_x = gradient_method_Adagrad(i, 1e-5, 25, 1e-6, 0.5, 0.1, obj_poly, grad_poly)
    figure()
plt.title("Adagrad")
plt.show()

# 3 part(c)
print("\nProblem 3(c):")
maxit = 100
x0 = np.array([3, 3])
for m in range(5, maxit + 5, 5):    
    x, objective, itr, all_x = gradient_method_Adagrad(x0, 1e-5, m, 1e-6, 0.5, 0.1, obj_poly, grad_poly)
    print("m:", m, "x =", [float('{:.3f}'.format(i)) for i in x], "objective =", round(objective, 3), "number of iterations =", itr)

# 4 part(a)
print("\nProblem 4(a):")
x0 = np.array([-1, -0.5])
x, objective, itr, all_x, flag_newton, flag_fullSize = newton_glob(x0, 1e-7, 1e-4, 1e-6, 0.1, 0.5, obj_Rosenbrock, grad_Rosenbrock, hess_Rosenbrock)
print("Globalized Newton:", "x =", [float('{:.3f}'.format(i)) for i in x], "objective =", round(objective, 3), "number of iterations =", itr)
if(flag_newton == 1):
    print("Not always ultilize the Newton direction")
else:
    print("Always ultilize the Newton direction")
if(flag_fullSize == 1):
    print("Not always use the full step size alpha_k = 1")
else:
    print("Always use the full step size alpha_k = 1")

x, objective, itr, all_x = gradient_method_Armijo(x0, 1e-7, 0.5, 1e-4, obj_Rosenbrock, grad_Rosenbrock)
print("Gradient Method:", "x =", [float('{:.3f}'.format(i)) for i in x], "objective =", round(objective, 3), "number of iterations =", itr)

# 4 part(b)
x0 = [np.array([-3, -3]), np.array([3, -3]), np.array([-3, 3]), np.array([3, 3])]
X1 = np.arange(-8, 8, 0.01)
X2 = np.arange(-9, 8, 0.01)
X1_, X2_ = np.meshgrid(X1, X2)
Y = X1**4 + (2/3) * (X1_**3) + (1/2) * (X1_ ** 2) - 2 * (X1_**2) * X2_ + (4/3) * (X2_**2)
plt.contour(X1_, X2_, Y, 25)
for i in x0:
    x, objective, itr, all_x, flag_newton, flag_fullSize = newton_glob(i, 1e-5, 0.1, 1e-6, 0.1, 0.5, obj_poly, grad_poly, hess_poly)
    figure()
plt.title("Globalized Newton Method")
plt.show()

