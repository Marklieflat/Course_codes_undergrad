# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:08:10 2022

@author: Mark
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
x, y = np.meshgrid(x,y)
z = x**4 + 2/3 * (x**3) + 1/2 * (x**2) - 2*(x**2)*y + 4/3 *(y**2)
surf = ax.plot_surface(x,y,z,rstride = 1, cstride = 1, cmap = 'rainbow')
fig.colorbar(surf, shrink = 0.5, aspect = 5)
plt.show()