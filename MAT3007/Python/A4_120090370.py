import numpy as np
import cvxpy as cp

x = cp.Variable(shape = (4))
c = np.array([2, 3, 4, 7])
A = np.array([[4, 6, -2, 8], 
              [1, 2, -6, 7]])
b = np.array([20, 10])

objective = cp.Maximize(c @ x)

constraints = [A @ x == b]
constraints += [x >= 0]
constraints += [x[2] >= 2]

prob = cp.Problem(objective, constraints)
prob.solve()

print("Optimal solution:", x.value)
print("Optimal value:", prob.value)


