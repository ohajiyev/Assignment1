# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:16:39 2019

@author: hao2d9
"""
#import modules
import random # To generate random numbers
import operator # To be able to find the max list for x or y
import matplotlib.pyplot # To plot points

# Create empty agent list.
agents = []

# Make a y variable random between 0-99.
y0 = random.randint(0,99)
y1 = random.randint(0,99)

# Make a x variable random between 0-99.
x0 = random.randint(0,99)
x1 = random.randint(0,99)

# Add y, x random integer between 0-99 variables to the list
agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])

#print agents list to view the results
print(agents)
print(max(agents))
print(max(agents, key=operator.itemgetter(1)))

# Change y and x based on random numbers.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1


# Make a second set of y and xs, and make these change randomly as well.
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

# Work out the distance between the two sets of y and xs.
distance = (((x0 - x1)**2) + ((y0 - y1)**2))**0.5

print(distance)

            