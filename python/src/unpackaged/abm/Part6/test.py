# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:47:41 2019

@author: hao2d9
"""

def foo(i):
    return i, i + 0.5

[str(x)
    for i in range(3)
        for x in foo(i)
]


[print(str(x)) for i in range(3) for x in foo(i)]

## is same as
#for i in range(3):
#    for x in foo(i):
#        yield str(x)