# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:42:04 2019

@author: hao2d9
"""

import matplotlib.pyplot as plt
import numpy as np

carry_on = True

def gen_function(b = [0]):
    a = 0
    print(a)
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        print(a)
        yield a			# Returns control and waits next call.
        a = a + 1
        print(a)

x = np.arange(0, 10, 0.2)
y = np.sin(x)
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(x, y)
#plt.show()

gen_function()