# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:57:21 2015

@author: Neuromancer
"""

class col_boxes(object):
    colour = 'red'
    size = [.6,.6]
    
    def __init__(self,
                 start_pos = [0,0],
                 current_pos = [0,0],
                 colour = 'white',
                 size = [.6,.6]):
        self.start_pos = start_pos
        self.current_pos = current_pos
        self.colour = colour
        self.size = size
    def __str__(self):
        return "start: {},\ncurrent: {}\ncolour: {}\nsize:{}".format(self.start_pos,self.current_pos,self.colour,self.size)
        



red_box = col_boxes()
red_box.colour = 'red'
red_box.start_x = 2
red_box.start_x = 2

green_box = col_boxes()
green_box.colour = 'green'


print red_box
print green_box
    
