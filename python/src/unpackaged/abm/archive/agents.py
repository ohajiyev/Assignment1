# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:21:02 2019

@author: hao2d9
"""

import random
import operator
import matplotlib.pyplot
import time

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2 + (agents_row_a[1] - agents_row_b[1])**2)**0.5)

start = time.process_time()

num_of_agents = 10
num_of_iterations = 100

# Create an empty list.
agents = []

# Set up variables.
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

print(agents)

for j in range(num_of_iterations):  
    for i in range(num_of_agents):
    
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
        
print(agents)
        
for i in range(num_of_agents-1):
    for j in range(i+1, num_of_agents):
        print(distance_between(agents[i], agents[j]))
        
answer = distance_between(agents[0], agents[1])
print(answer)

matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

end = time.process_time()

print("time = " + str(end - start))

#matplotlib.pyplot.ylim(0, 100)
#matplotlib.pyplot.xlim(0, 100)
#matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#m = max(agents, key=operator.itemgetter(1))
#matplotlib.pyplot.scatter(m[1],m[0], color='red')
#matplotlib.pyplot.show()




