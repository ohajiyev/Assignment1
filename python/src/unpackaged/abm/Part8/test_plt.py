# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:42:04 2019

@author: hao2d9
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.show()