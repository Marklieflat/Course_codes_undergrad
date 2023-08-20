import cvxpy as cp
import numpy as np

C = np.array([2500, 3000, 1400, 1600, 3200])
x = cp.Variable(shape = (5, 3), integer = True)
c = cp.Variable(shape = 5)

objective = cp.Minimize(10 * cp.max(0, 2800 - sum([x[i, 0] * c[i] for i in range(0, 5)])) + 6 * cp.max(0, 4200 - sum([x[i, 1] * c[i] for i in range(0, 5)])) + \
                        8 * cp.max(0, 5000 - sum([x[i, 2] * c[i] for i in range(0, 5)])))
constraints = [c <= C, c >= 0]
constraints += [2800 - sum([x[i, 0] * c[i] for i in range(0, 3)]) <= 500]
constraints += [4200 - sum([x[i, 1] * c[i] for i in range(0, 3)]) <= 400]
constraints += [5000 - sum([x[i, 2] * c[i] for i in range(0, 3)]) <= 300]
constraints += [x >= 0, x <= 1]
constraints += [sum(x[i, :]) <= 1 for i in range(0, 5)]

prob = cp.Problem(objective, constraints)
prob.solve()

print("Optimal solution:", x.value)
print("Optimal value:", prob.value)
