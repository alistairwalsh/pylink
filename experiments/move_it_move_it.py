# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:28:09 2015

@author: Neuromancer
"""

import numpy as np
from psychopy import visual, event, core

win = visual.Window(size=(400, 400), fullscr=False, screen=0, allowGUI=False, allowStencil=False, units='pix',
monitor='testMonitor', colorSpace=u'rgb', color=[0.51,0.51,0.51])

keys = event.BuilderKeyResponse()

dot1 = visual.Circle(win=win, name='dot1',units='pix',
    radius=10, edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1,interpolate=True)



frameN = 50  # To set angle in first loop iteration
speed = 14  # initial speed in whatever unit the stimulus use.
angle = 45  # initial angle in degrees
x_change = np.cos(angle) * speed  # initial
y_change = np.sin(angle) * speed  # initial

while True:
    # More new stuff: Change direction angle (in degrees)
    if frameN == 50:
        angle_current = np.rad2deg(np.arctan(y_change / float(x_change)))  # float to prevent integer division
        angle_change = np.random.randint(-180, 180)  # change interval to your liking or set to a constant value or something
        angle = angle_current + angle_change  # new angle

        x_change = np.cos(angle) * speed
        y_change = np.sin(angle) * speed
        frameN = 0
    #frameN += 1

    dot1.pos+=(x_change,y_change)

    if dot1.pos[0] > 200 or dot1.pos[0] < -200:
        x_change = x_change * -1
    if dot1.pos[1] > 200 or dot1.pos[1] < -200:
        y_change = y_change * -1


    dot1.draw()
    win.flip()

    if event.getKeys(keyList=["escape"]):
        core.quit()