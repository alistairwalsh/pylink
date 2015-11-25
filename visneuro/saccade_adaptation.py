#!/usr/bin/python

# saccade_adaptation.py

import numpy as np

class fixation_area:
    '''
    takes radius and x,y coordinates and creates a circle defining a fixation area
    able to set radius, position
    calculates area
    returns radius,area,position
    '''
    pi = np.pi

    def __init__(self, radius=1,x = 0,y = 0):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, radius):
        self.radius = radius
    
    def set_position(self,x,y):
        self.x,self.y = x,y

    def get_radius(self):
        return self.radius

    def get_position(self):
        return self.x,self.y
    
def check_fixation_area(target_circle ,view_x=0,view_y=0):
    '''
    Takes a target_circle class object (as defined by fixationArea()), eyetracker x and y positions float values
    and calculates if eye position (x,y) is within the radius of the fixation area
    returns True or False.
    '''
    
    centre_x, centre_y = target_circle.get_position()[0], target_circle.get_position()[1]
    radius = target_circle.get_radius()
    if (view_x - centre_x)**2 + (view_y - centre_y)**2 < radius**2:
        return True
    else:
        return False
    
if __name__ == '__main__':
    pass
    