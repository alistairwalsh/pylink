# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:45:43 2015

@author: Neuromancer
"""

import numpy as np
from psychopy import visual, core, event, monitors

win = visual.Window(color='black')
rect = visual.Rect(win,
	width =.5, 
	height =.3, 
	fillColor ='red')
rect.draw() 
win.flip()  # don't forget to flip when done with drawing all stimuli so that the stimuli become visible
event.waitKeys()
win.close()