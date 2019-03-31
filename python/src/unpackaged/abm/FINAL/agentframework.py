# -*- coding: utf-8 -*-
"""
Date Last Updated: Mar 31, 2019

Author: Orkhan Hajiyev (gy17oh)

Title: Agent class

Purpose: 
    Agent class contains agent's states and define its behaviour
    
License: 
    Copyright (c) 2019 Orkhan Hajiyev
    Lisence under MIT License
    License link: 
        https://github.com/ohajiyev/Assignment2/blob/master/LICENSE.md
       
Python version: 3.7
"""

# Import modules
import random
import os

# Create Agent class
class Agent():    
    """ Initalize the class """
    def __init__ (self, environment, agents):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        
    # Set the property of the private variables to use Incapsulation
    ###########################################################################

    @property
    def x(self):
        """Get the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        """Set the 'x' property."""
        self._x = value  

    @property
    def y(self):
        """Get the 'y' property."""
        return self._y

    @y.setter
    def y(self, value):
        """Set the 'y' property."""
        self._y = value

    # End of property
    ###########################################################################
        
    def move(self):
        """
        Function randomly change the position of the agent
        """
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
    def eat(self):
        """
        Function simulate the 'eat' behaviour of the agent and the agent 
        decrease the value of the environment dataset at the location of 
        the agent. Eat method was altered to eat everything what left on 
        the environment
        """
        if self.environment[self._y][self._x] >= 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        elif (self.environment[self._y][self._x] > 0) and \
                                     (self.environment[self._y][self._x] < 10):
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
            
    def distance_between(self, agent):
        """
        Function returns the distance between two agents
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5  
                
    def share_with_neighbours(self, neighbourhood):
        """
        Function share the resources between two close agents
        """
        for agent in self.agents:
            if self != agent:
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave

    def __str__(self):
        """ Overwrite the method to create the string to convert to text """
        return 'Agent x: {0}\
                {3}Agent y: {1}\
                {3}Agent store: {2}'\
                .format(self._x, \
                        self._y, \
                        round(self.store, 1), \
                        os.linesep)