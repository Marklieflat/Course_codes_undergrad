import matplotlib.pyplot as plt
import numpy as np

def func0(x):
    return 4*x*np.log(x) + 2*x

def func1(x):
    return 2**np.log(x)

def func2(x):
    return x**2 + 10*x

funcs = [func0, func1, func2]

xs = np.arange(0,10,1)
for idx, func in enumerate(funcs):
    ys = [func(x) for x in xs]
    plt.plot(xs, ys, marker = 'o', label = 'func%d' % idx)

plt.legend()
plt.show()