# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:16:39 2019

@author: hao2d9

The script shows the results of Part 3 instructions
"""
#import modules
import random # To generate random numbers
import operator # To be able to find the max list for x or y
import matplotlib.pyplot # To plot points

# Number of agents
num_of_agents = 10

# NUmber of iterations
num_of_iterations = 100

# Create empty agent list.
agents = []

# Fill agents list with the random values
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
    
    
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for agent in agents:
    matplotlib.pyplot.scatter(agent[1], agent[0], color='red')

max_agent = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(max_agent[1], max_agent[0], color='green')
matplotlib.pyplot.show()

# Iterate number of iterations 
for i in range(num_of_iterations):
    # Iterate through the agents list
    for agent in agents:
        if random.random() < 0.5:
            agent[0] = (agent[0] + 1) % 100
        else:
            agent[0] = (agent[0] - 1) % 100
    
        if random.random() > 0.5:
            agent[1] = (agent[1] + 1) % 100
        else:
            agent[1] = (agent[1] - 1) % 100
 
# Work out the distance between the two sets of y and xs.
#distance = (((x0 - x1)**2) + ((y0 - y1)**2))**0.5

# Plot points on canvas
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for agent in agents:
    matplotlib.pyplot.scatter(agent[1], agent[0], color='red')

max_agent = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(max_agent[1], max_agent[0], color='green')
matplotlib.pyplot.show()