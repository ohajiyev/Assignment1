import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv



file_in = open("in.txt")

environment = []
for datarow in file_in:
    rowlist = []
    for d in datarow.split(","):
        rowlist.append(int(d))
    environment.append(rowlist)
    
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

agents = []



# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.imshow(environment)
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
#matplotlib.pyplot.show()

def update(frame_number, agents):
    
    fig.clear()   
       
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
            print(agents[i][0],agents[i][1])
 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

animation = matplotlib.animation.FuncAnimation(fig, update(agents), interval=1)

matplotlib.pyplot.show()
       
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.imshow(environment)
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
#matplotlib.pyplot.show()

       
#display the environment        
#matplotlib.pyplot.xlim(0, 300)
#matplotlib.pyplot.ylim(0, 300)
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
