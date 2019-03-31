# -*- coding: utf-8 -*-
"""
Date Last Updated: 
    Mar 30, 2019

Author: 
    Orkhan Hajiyev (gy17oh)

Title: 
    Assignment 2. Module GEOG5991M
    White Star Line Project

Version: 
    2.0

Purpose: 
    To implement the requirements of the Assignment 2 of the Module GEOG5991M.
    The version was built to analyse the images with MULTIPLE icebergs.
    
    White Star Line was selected as the project to satisfy the assignment's
    description. The link to the project's problem definition:
    https://www.geog.leeds.ac.uk/courses/computing/
    study/core-python-odl/assessment2/ice.html
    
    Briefly, the goal is to analyse two raster files of the size 300 by 300 of 
    the radar and lidar images of the sea and identify the multiple bergs. 
    
License: 
    Copyright (c) 2019 Orkhan Hajiyev
    Lisence under MIT License
    License link: 
        https://github.com/ohajiyev/Assignment2/blob/master/LICENSE.md
       
Github Repo Link: 
    https://github.com/ohajiyev/Assignment2
    
Code Folder Link:
    https://github.com/ohajiyev/Assignment2/tree/master/python/src/unpackaged/
    ice/Version2

Zip file link:
    https://github.com/ohajiyev/Assignment2/tree/master/python/src/unpackaged/
    ice/Version2/assignment2.zip

Instructions to run:
    Download 'assignment2.zip' file and extract.
    The extracted folder should contain the following files and folders, as 
    minimum:
        'ice_v2.py' - main code to run from command prompt
        'icebergstructure.py' - Iceberg class definiton
        'imagesupport.py' - ImageHandle class definiton
        'ice2_notebook.ipynb' - Jupyter Notebook file
        'input' - folder which contains input images 'white2.lidar' and 
                  'white2.radar'
        'input/white2.lidar' - lidar image (300x300) of an area of sea with 
                               the multiple bergs. Values (0-255) contain 
                               height data of the objects
        'input/white2.radar' - radar image (300x300) of an area of sea with 
                               the multiple bergs. Values (0-255) contain 
                               information to idenitify the bergs (>=100)
        'output' - folder which is output folder for the result text file 
                   ('result.txt)
    Software requirements:
        Anaconda3 (64bit):
            Python 3.7
            Spyder 3.3.2
            Jupiter Notebook
            Anaconda prompt
        
    The code can be run in Anaconda command line, Spyder and Jupyter notebook.
        Anaconda cmd: 
            1. 'python ice_v2.py'
        Spyder: 
            1. Open 'ice_v2.py
            2. Ensure that IPython console is activated
            3. Run '#%matplotlib qt5' command in IPython console to interact
               with interface.
            4. Press 'F5' button or 'Run' from the  menu to run the code
        Jupyter Notebook:
            1. Open 'ice2_notebook.ipynb' in browser
            2. Run first line '%matplotlib notebook' to enable interaction
               with the output
            3. Press 'Run all' from Run menu
        
Limitations:
    The code only was tested and developed with/for available two sets of the 
    inputs provided by the University. It is assumed that the bergs data should 
    be continuous and without any gaps. Any gaps in input data may wrongly 
    identify the bergs. These are artificial files and in the reality
    no image can come ideally without any gaps or distortions. For real images
    the algorithms which is used to bergs identification hardly can be applied.
    For the real case object classification method of machine learning should
    be applied. Also the algorithm cannot differentiate the  bergs with 
    overlaps.
    
Evident improvements:
    Code can be improved by creating __init__ method in HandleImage
    class and be enhanced by using real GUI not relying only on matplotlib
    capability. Machine learning techniques can be implemented to improve
    identification of bergs.
    
Python version: 
    3.7 (Python 3.7.1 64-bit | Qt 5.9.6 | PyQt5 5.9.2 | Windows 10)

Coding Tool:
    Spyder Version 3.3.2

"""




"""
Created on Wed Mar  6 20:16:39 2019

@author: hao2d9

The script shows the results of Part 7 instructions.

Part 6 enhacemnet was added to the script. The modified environment state
is written to the new file.

"""

"""
===============================================================================
===============================================================================
PART 6 REQUIRED IMPROVEMENTS

So, that's kind of cool. We've now got agents that interact with our 
environment. If you've got some time, have a think about implementing the 
following:

Using the lecture notes, can you write out the environment as a file at the 
end?

Can you make a second file that writes out the total amount stored by all the 
agents on a line? Can you get the model to append the data to the file, rather 
than clearing it each time it runs?

Can you override __str__(self) in the agents, as mentioned in the lecture on 
classes, so that they display this information information about their location 
and stores when printed?

Can you get the agents to wander around the full environment by finding out the 
size of environment inside the agents, and using the size when you randomize 
their starting locations and deal with the boundary conditions?

At the moment, the agents only eat 10 units at a time. This will leave a few 
units in each area, even if intensly grazed. Can you get them to eat the last 
few bits, if there's less than 10 left, without leaving negative values?

Can you get the agents to sick up their store in a location if they've been 
greedy guts and eaten more than 100 units? (note that when you add or subtract 
from the map, the colours will re-scale).

===============================================================================
===============================================================================
                                            
PART 7 REQUIRED IMPROVEMENTS

All the major model parameters are in model.py, as we discussed earlier. 
Can you get the model so that it reads these from the command line using argv, 
the command line arguments we talked about in the lecture? i.e., so it runs 
like this:

python model.py 200 20 30

Where, for example, 200 is the number of agents, 20 is the number of 
iterations, and 30 is the neighbourhood. Remember that you may need to catch 
exceptions when the user types something that can't be cast to an int.

If you can do this, can you write a python program that uses subprocess.call 
to run the model with a variety of results using ranges to set those parameters 
(remember to leave some defaults)? For example, can you get it to run stepping 
up agent numbers by ten each time it runs, and append the total amount stored 
to a file for each run? This is called "parameter sweeping", and it isn't 
unusual to have a model running class that runs a model multiple times to 
explore how it responds to parameter variations. You might want an argv 
variable that also turns off the visual output for multiple runs (if you want 
to make this a boolean, note that all non-empty strings, even "False" are true. 
For the solution, see this StackOverflow answer).

===============================================================================
===============================================================================
"""


#==============================================================================
# Import modules

import matplotlib.pyplot
import matplotlib.animation
import agentframework

# End of Import modules
#==============================================================================


#==============================================================================
# Function definitions

def draw_environment(agents, environment, num_of_agents):
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.show()
    
def update(frame_number, environment, file_output):
    
    fig.clear()   
    
    # Move and eat the agents.
    for i in range(num_of_agents):
            agents[i].move() 
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood) 
        
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)    
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    if frame_number == (num_of_iterations -1):
        write_last_state(environment, file_output)
        
def write_last_state(environment, file_output_name):
    ##Write the state of the environemnt dataset to the file
    with open(file_output_name, 'w') as file_object:
        for env_row in environment:
            file_object.write(','.join(str(env_value) for env_value in 
                                       env_row) + '\n')


# End of Function definitions
#==============================================================================

##==============================================================================
## Start of Main function

#             
## End of Main function
##==============================================================================


#==========================================================================
# Create variables

num_of_agents = 10 # number of agents
num_of_iterations = 10 # number of iterations
neighbourhood = 20
environment = [] # empty list of environment variable 
agents = [] # empty list of Agent objects
file_input_name = "in.txt" # input file name
file_output_name = "out.txt" # output file name

# End of Create variables
#==========================================================================

# Setup figure parameters
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])  

# Read input file values and assign into environment variable
with open(file_input_name) as file_input:
    for data_row in file_input:
        row_list = []
        for single_value in data_row.split(","):
            row_list.append(int(single_value))
        environment.append(row_list)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
        
animation = matplotlib.animation.FuncAnimation(
        fig,
        lambda frame_number: update(frame_number, environment, file_output_name), 
        interval=1, 
        repeat=False, 
        frames=num_of_iterations
        )
matplotlib.pyplot.show()
