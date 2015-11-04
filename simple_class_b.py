# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:57:21 2015

@author: Neuromancer
"""


import time
import sys
from psychopy import visual,event,core

class col_boxes(object):
    def __init__(self,
                 start_pos = [0,0],
                 current_pos = [0,0],
                 colour = "white",
                 size = [100,100]):
        self.start_pos = start_pos
        self.current_pos = current_pos
        self.colour = colour
        self.size = size
    def __str__(self):
        return "start: {},\ncurrent: {}\ncolour: {}\nsize:{}".format(self.start_pos,self.current_pos,self.colour,self.size)

red_box = col_boxes()
red_box.colour = "red"
red_box.start_x = 2
red_box.start_x = 2

green_box = col_boxes()
green_box.colour = "green"


win = visual.Window(size=(400,400),color="white", units='pix')
square = visual.Rect(win,lineColor="black",size = [100,100],fillColor=red_box.colour)#,fillColor=red_box.colour ,size=red_box.size,)

for step in range(0,100):
    red_box.current_pos[0] += step
    red_box.current_pos[1] -= step 
    square.pos = red_box.current_pos
    square.draw()
    win.flip()
    core.wait(.1) #pause for 500 ms (half a second)
    
sys.exit()






    
