# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:30:45 2015

@author: Neuromancer
"""

import time
import sys
from psychopy import visual,event,core
 
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
square.draw()
win.flip()
core.wait(.5) #pause for 500 ms (half a second)
sys.exit()