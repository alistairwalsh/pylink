#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Wed  4 Nov 12:40:34 2015
=======
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Wed Nov  4 12:48:35 2015
>>>>>>> origin/pygame
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
<<<<<<< HEAD
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
=======
from psychopy import visual, core, data, event, logging, sound, gui
>>>>>>> origin/pygame
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
<<<<<<< HEAD
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
=======

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
>>>>>>> origin/pygame
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'test1'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
<<<<<<< HEAD
    originPath=u'/Users/Neuromancer/Documents/neuralcode/loquacious-octo-turtle/dist2.psyexp',
=======
    originPath=u'/Users/Brook/Documents/GoogleDrive/Code/notebooks/loquacious-octo-turtle/dist2.psyexp',
>>>>>>> origin/pygame
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
<<<<<<< HEAD
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
=======
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
>>>>>>> origin/pygame
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instruction = visual.TextStim(win=win, ori=0, name='instruction',
    text="This trail will begin with a fixation point marked with 'x' and be followed by a brief presentation of four different coloured squares. The squares will then disappear, and after a brief delay, one of the squares will reappear having changed location along one axis from its previous location in the group presentation.  \n\nYour task is to indicate the direction of that single square's move (from its previous location in the group presentation) by pressing either 'up', 'down', 'left', or 'right' arrow keys on the keyboard as soon as you can.  Repeat this process until the trail is complete.\n\nPress 'enter' to begin.",    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
fix2 = visual.Polygon(win=win, name='fix2',units='cm', 
    edges = 90, size=[0.3, 0.3],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
fix1 = visual.Polygon(win=win, name='fix1',units='cm', 
    edges = 90, size=[0.3, 0.3],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
fixate = visual.Polygon(win=win, name='fixate',units='cm', 
    edges = 90, size=[0.3, 0.3],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)
one = visual.Rect(win=win, name='one',units='cm', 
    width=[0.6, 0.6][0], height=[0.6, 0.6][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-3.0, 
interpolate=True)
two = visual.Rect(win=win, name='two',units='cm', 
    width=[0.6, 0.6][0], height=[0.6, 0.6][1],
    ori=1, pos=[0,0],
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
three = visual.Rect(win=win, name='three',units='cm', 
    width=[0.6, 0.6][0], height=[0.6, 0.6][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-5.0, 
interpolate=True)
four = visual.Rect(win=win, name='four',units='cm', 
    width=[0.6, 0.6][0], height=[0.6, 0.6][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-6.0, 
interpolate=True)
test = visual.Rect(win=win, name='test',units='cm', 
    width=[0.6, 0.6][0], height=[0.6, 0.6][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-7.0, 
interpolate=True)

# Initialize components for Routine "finish"
finishClock = core.Clock()
Thanks = visual.TextStim(win=win, ori=0, name='Thanks',
    text='Task complete.\nThank you for your time.',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instruct"-------
t = 0
instructClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
start = event.BuilderKeyResponse()  # create an object of type KeyResponse
start.status = NOT_STARTED
# keep track of which components have finished
instructComponents = []
instructComponents.append(instruction)
instructComponents.append(start)
for thisComponent in instructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instruct"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if t >= 0.0 and instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction.tStart = t  # underestimates by a little under one frame
        instruction.frameNStart = frameN  # exact frame index
        instruction.setAutoDraw(True)
    
    # *start* updates
    if t >= 0.0 and start.status == NOT_STARTED:
        # keep track of start time/frame for later
        start.tStart = t  # underestimates by a little under one frame
        start.frameNStart = frameN  # exact frame index
        start.status = STARTED
        # keyboard checking is just starting
<<<<<<< HEAD
        win.callOnFlip(start.clock.reset)  # t=0 on next screen flip
=======
        start.clock.reset()  # now t=0
>>>>>>> origin/pygame
        event.clearEvents(eventType='keyboard')
    if start.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            start.keys = theseKeys[-1]  # just the last key pressed
            start.rt = start.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start.keys in ['', [], None]:  # No response was made
   start.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('start.keys',start.keys)
if start.keys != None:  # we had a response
    thisExp.addData('start.rt', start.rt)
thisExp.nextEntry()
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
task = data.TrialHandler(nReps=1, method='random', 
<<<<<<< HEAD
    extraInfo=expInfo, originPath=-1,
=======
    extraInfo=expInfo, originPath=u'/Users/Brook/Documents/GoogleDrive/Code/notebooks/loquacious-octo-turtle/dist2.psyexp',
>>>>>>> origin/pygame
    trialList=data.importConditions('VWM_coordinates.xlsx'),
    seed=None, name='task')
thisExp.addLoop(task)  # add the loop to the experiment
thisTask = task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTask.rgb)
if thisTask != None:
    for paramName in thisTask.keys():
        exec(paramName + '= thisTask.' + paramName)

for thisTask in task:
    currentLoop = task
    # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
    if thisTask != None:
        for paramName in thisTask.keys():
            exec(paramName + '= thisTask.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(fix2)
    trialComponents.append(fix1)
    trialComponents.append(fixate)
    trialComponents.append(one)
    trialComponents.append(two)
    trialComponents.append(three)
    trialComponents.append(four)
    trialComponents.append(test)
    trialComponents.append(response)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix2* updates
        if t >= 2.75 and fix2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix2.tStart = t  # underestimates by a little under one frame
            fix2.frameNStart = frameN  # exact frame index
            fix2.setAutoDraw(True)
        if fix2.status == STARTED and t >= (2.75 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix2.setAutoDraw(False)
        if fix2.status == STARTED:  # only update if being drawn
            fix2.setPos(locfix2, log=False)
        
        # *fix1* updates
        if t >= 2 and fix1.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix1.tStart = t  # underestimates by a little under one frame
            fix1.frameNStart = frameN  # exact frame index
            fix1.setAutoDraw(True)
        if fix1.status == STARTED and t >= (2 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix1.setAutoDraw(False)
        if fix1.status == STARTED:  # only update if being drawn
            fix1.setPos(locfix1, log=False)
        
        # *fixate* updates
        if t >= 0.0 and fixate.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixate.tStart = t  # underestimates by a little under one frame
            fixate.frameNStart = frameN  # exact frame index
            fixate.setAutoDraw(True)
        if fixate.status == STARTED and t >= (0.0 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixate.setAutoDraw(False)
        
        # *one* updates
        if t >= .5 and one.status == NOT_STARTED:
            # keep track of start time/frame for later
            one.tStart = t  # underestimates by a little under one frame
            one.frameNStart = frameN  # exact frame index
            one.setAutoDraw(True)
        if one.status == STARTED and t >= (.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            one.setAutoDraw(False)
        if one.status == STARTED:  # only update if being drawn
            one.setFillColor(col1, log=False)
            one.setPos(loc1, log=False)
        
        # *two* updates
        if t >= .5 and two.status == NOT_STARTED:
            # keep track of start time/frame for later
            two.tStart = t  # underestimates by a little under one frame
            two.frameNStart = frameN  # exact frame index
            two.setAutoDraw(True)
        if two.status == STARTED and t >= (.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            two.setAutoDraw(False)
        if two.status == STARTED:  # only update if being drawn
            two.setFillColor(col2, log=False)
            two.setPos(loc2, log=False)
        
        # *three* updates
        if t >= .5 and three.status == NOT_STARTED:
            # keep track of start time/frame for later
            three.tStart = t  # underestimates by a little under one frame
            three.frameNStart = frameN  # exact frame index
            three.setAutoDraw(True)
        if three.status == STARTED and t >= (.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            three.setAutoDraw(False)
        if three.status == STARTED:  # only update if being drawn
            three.setFillColor(col3, log=False)
            three.setPos(loc3, log=False)
        
        # *four* updates
        if t >= .5 and four.status == NOT_STARTED:
            # keep track of start time/frame for later
            four.tStart = t  # underestimates by a little under one frame
            four.frameNStart = frameN  # exact frame index
            four.setAutoDraw(True)
        if four.status == STARTED and t >= (.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            four.setAutoDraw(False)
        if four.status == STARTED:  # only update if being drawn
            four.setFillColor(col4, log=False)
            four.setPos(loc4, log=False)
        
        # *test* updates
        if t >= 3.5 and test.status == NOT_STARTED:
            # keep track of start time/frame for later
            test.tStart = t  # underestimates by a little under one frame
            test.frameNStart = frameN  # exact frame index
            test.setAutoDraw(True)
        if test.status == STARTED:  # only update if being drawn
            test.setFillColor(testColour, log=False)
            test.setPos(testLocation, log=False)
        
        # *response* updates
        if t >= 3.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
<<<<<<< HEAD
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
=======
            response.clock.reset()  # now t=0
>>>>>>> origin/pygame
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', 'down', 'up'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
                # was this 'correct'?
                if (response.keys == str(corrAns)) or (response.keys == corrAns):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for task (TrialHandler)
    task.addData('response.keys',response.keys)
    task.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        task.addData('response.rt', response.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'task'


#------Prepare to start Routine "finish"-------
t = 0
finishClock.reset()  # clock 
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
finishComponents = []
finishComponents.append(Thanks)
for thisComponent in finishComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "finish"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finishClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thanks* updates
    if t >= 0.0 and Thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        Thanks.tStart = t  # underestimates by a little under one frame
        Thanks.frameNStart = frameN  # exact frame index
        Thanks.setAutoDraw(True)
    if Thanks.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        Thanks.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
