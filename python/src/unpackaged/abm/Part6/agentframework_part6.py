# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 06:56:06 2019

@author: hao2d9

Agentframework creation. The script shows the results of Part 6 instructions.

"""

# Import modules
import random

# Create Agent class
class Agent():    
    def __init__ (self):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        
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
