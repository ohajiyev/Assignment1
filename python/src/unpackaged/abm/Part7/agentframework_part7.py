# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 06:56:06 2019

@author: hao2d9

Agentframework creation. The script shows the results of Part 7 instructions.

Eat method was altered to eat everything what left on the environment

"""

# Import modules
import random

# Create Agent class
class Agent():    
    def __init__ (self, environment, agents):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        
    #The returned property object also has the attributes fget, fset, and fdel 
    #corresponding to the constructor arguments.
    @property
    def x(self):
        """Get the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        """Set the 'x' property."""
        self._x = value

    @x.deleter
    def x(self):
        """Delete the 'x' property."""
        del self._x    

    @property
    def y(self):
        """Get the 'y' property."""
        return self._y

    @y.setter
    def y(self, value):
        """Set the 'y' property."""
        self._y = value

    @y.deleter
    def y(self):
        """Delete the 'y' property."""
        del self._y    
        
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
    def eat(self): # Now it eat what is left
        if self.environment[self._y][self._x] >= 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        elif (self.environment[self._y][self._x] > 0) and \
                                     (self.environment[self._y][self._x] < 10):
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
            
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + 
                ((self.y - agent.y)**2))**0.5  
                
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if self != agent:
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    #print("sharing " + str(dist) + " " + str(ave))