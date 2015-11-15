# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:30:45 2015

@author: Neuromancer
"""

import time
import sys
from psychopy import visual,event,core
 

 
win = visual.Window(size=(400,400),color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
square.draw()
win.flip()
core.wait(.5) #pause for 500 ms (half a second)
core.quit()
#sys.exit()

 
#win = visual.Window([400,400],color="black", units='pix')
#square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
#square.draw()
#win.flip()
#core.wait(.5) #pause for 500 ms (half a second)
#sys.exit()