# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:16:39 2019

@author: hao2d9

The script shows the results of Part 7 instructions.

Part 6 enhacemnet was added to the script. The modified environment state
is written to the new file.

"""
#==============================================================================
# Import modules

import random
import operator
import matplotlib.pyplot
import agentframework_part7 as agentframework
import csv

# End of Import modules
#==============================================================================


#==============================================================================
# Function definitions

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.y - agents_row_b.y)**2) + 
        ((agents_row_a.x - agents_row_b.x)**2))**0.5

# End of Function definitions
#==============================================================================

#==============================================================================
# Start of Main function
def main():
    
    #==========================================================================
    # Create variables
    
    num_of_agents = 10 # number of agents
    num_of_iterations = 100 # number of iterations
    neighbourhood = 20
    environment = [] # empty list of environment variable 
    agents = [] # empty list of Agent objects
    file_input = open("in.txt") # read the input file
    
    # End of Create variables
    #==========================================================================
    
    
    # Read input file values and assign into environment variable
    for data_row in file_input:
        row_list = []
        for single_value in data_row.split(","):
            row_list.append(int(single_value))
        environment.append(row_list)
    
    # Make the agents.
    for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment, agents))
    
    # Print the state of environment and agents before changes
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.show()
    
    # Move and eat the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)  
            
    # Print the state of environment and agents after changes
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.show()
    
    # Write the new state  of environemnt to the file
    with open('out.txt', 'w') as file_output:
        for env_row in environment:
            file_output.write(','.join(str(env_value) for env_value in env_row) + '\n')
             
    print(agents[0].x, agents[0].y) 
    print(agents[0].agents[1].x, agents[0].agents[1].y)
    print()
            
# End of Main function
#==============================================================================
        
        
# Main part of the script
if __name__ == "__main__":
    main()        
