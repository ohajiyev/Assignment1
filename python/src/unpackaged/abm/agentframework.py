# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:00:24 2019

@author: hao2d9
"""
import random

class Agent():
    
    def __init__(self, environment, agents):        
        self._x = random.randint(0, 99)
        self._y = random.randint(0, 99)
        self.environment = environment
        self.agents = agents
        self.store = 0
    
    #The returned property object also has the attributes fget, fset, and fdel 
    #corresponding to the constructor arguments.
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x    

    @property
    def y(self):
        """I'm the 'y' property."""
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @y.deleter
    def y(self):
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
            
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
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

    def distance_between(agents_row_a, agents_row_b):
        return (((agents_row_a.x - agents_row_b.x)**2) + 
                ((agents_row_a.y - agents_row_b.y)**2))**0.5    
        
 