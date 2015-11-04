# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:17:40 2015

@author: Alistair Walsh
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
    
Thanks = visual.TextStim(win=win, ori=0, name='Thanks',
    text='Task complete.\nThank you for your time.',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
    
win.flip()

core.wait(5)
    
win.close()
core.quit()

