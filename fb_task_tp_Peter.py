from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, logging, sound, gui, parallel

#Pylink imports
from pylink import *
from pygame import *

from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'fb_task'  # from the Builder filename that created this script
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
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

#Makes vairable to pass to eyetracker EDF file
#NOTE: MAX 4 characters (including .edf)
subj=str(expInfo['participant'])

                    ####BEGIN EYELINK CODE####

#Makes an instance of the eyetracker to interact with
tracker = EyeLink()

#Gets display information so it doesn't need to be manually set 
#NOTE: Change this if specific resolution is required. 
disp = getDisplayInformation()

                ###START EYETRACKER CALIBRATION###

#Opens a window for the eyetracker to display graphics on. 
display.init()
#display.set_mode((disp.width, disp.height), FULLSCREEN |DOUBLEBUF,32)
display.set_mode((800,600), FULLSCREEN)
mouse.set_visible(False)
openGraphics()

#Opens the EDF file.
edfFileName = subj + ".EDF";
tracker.openDataFile(edfFileName)		
	
pylink.flushGetkeyQueue(); 
tracker.setOfflineMode();                          

#Gets the display surface and sends a message to EDF file;
surf = display.get_surface()
tracker.sendCommand("screen_pixel_coords =  0 0 %d %d" %(surf.get_rect().w - 1, surf.get_rect().h - 1))
tracker.sendMessage("DISPLAY_COORDS  0 0 %d %d" %(surf.get_rect().w - 1, surf.get_rect().h - 1))

tracker_software_ver = 0
eyelink_ver = tracker.getTrackerVersion()
if eyelink_ver == 3:
	tvstr = tracker.getTrackerVersionString()
	vindex = tvstr.find("EYELINK CL")
	tracker_software_ver = int(float(tvstr[(vindex + len("EYELINK CL")):].strip()))
	

if eyelink_ver>=2:
	tracker.sendCommand("select_parser_configuration 0")
	if eyelink_ver == 2: #turn off scenelink camera stuff
		tracker.sendCommand("scene_camera_gazemap = NO")
else:
	tracker.sendCommand("saccade_velocity_threshold = 35")
	tracker.sendCommand("saccade_acceleration_threshold = 9500")
 
tracker.sendCommand("file_sample_data  = LEFT,GAZE,AREA,GAZERES,STATUS,INPUT")
 
setCalibrationColors((255, 255, 255), (0, 0, 0));  	#Sets the calibration target and background color
setTargetSize(int(surf.get_rect().w/70), int(surf.get_rect().w/300));	#select best size for calibration target
setCalibrationSounds("", "", "");
setDriftCorrectSounds("", "off", "off");

tracker.doTrackerSetup()

closeGraphics()

msecDelay(1000)

                    ###PASTE PSYCHOPY SCRIPT BELOW###

# Setup the display window
#win = visual.Window(size=(1280, 960), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
win = visual.Window(size=(800,600), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

from psychopy import event


# Initialize components for Routine "intro"
introClock = core.Clock()
intro_scr = visual.TextStim(win=win, ori=0, name='intro_scr',
    text='Please watch the next series \nof images carefully.\n\nPress spacebar to begin. ',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fix_2"
fix_2Clock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.4, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()

#Sets up the paralell port object with the port address. 
#pport = parallel.ParallelPort(address=0x0378)
stim_p_port = parallel.ParallelPort(address=0x0378)
fb_team = visual.TextStim(win=win, ori=0, name='fb_team',
    text='',    font=u'Arial',
    pos=[0, .7], height=0.0, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

fb_images = visual.ImageStim(win=win, name='fb_images',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[297*1.5,317*1.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=64, interpolate=True, depth=-1.0)

# Initialize components for Routine "outro"
outroClock = core.Clock()
outro_scr = visual.TextStim(win=win, ori=0, name='outro_scr',
    text='Thank you for your participation',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
space_start = event.BuilderKeyResponse()  # create an object of type KeyResponse
space_start.status = NOT_STARTED
# keep track of which components have finished
introComponents = []
introComponents.append(intro_scr)
introComponents.append(space_start)
for thisComponent in introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_scr* updates
    if t >= 0.0 and intro_scr.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_scr.tStart = t  # underestimates by a little under one frame
        intro_scr.frameNStart = frameN  # exact frame index
        intro_scr.setAutoDraw(True)
    
    # *space_start* updates
    if t >= 0.0 and space_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        space_start.tStart = t  # underestimates by a little under one frame
        space_start.frameNStart = frameN  # exact frame index
        space_start.status = STARTED
        # keyboard checking is just starting
        space_start.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if space_start.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            space_start.keys = theseKeys[-1]  # just the last key pressed
            space_start.rt = space_start.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_start.keys in ['', [], None]:  # No response was made
   space_start.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('space_start.keys',space_start.keys)
if space_start.keys != None:  # we had a response
    thisExp.addData('space_start.rt', space_start.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('trialTypes_long.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "fix_2"-------
    t = 0
    fix_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fix_2Components = []
    fix_2Components.append(fix)
    for thisComponent in fix_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fix_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fix_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        if fix.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fix_2"-------
    for thisComponent in fix_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    fb_team.setText(teamText)
    fb_images.setImage(stimFile)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(stim_p_port)    
    trialComponents.append(fb_team)
    trialComponents.append(fb_images)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    tracker.startRecording(1,1,1,1)  
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        #stim_p_port update  
        if t >= 0 and stim_p_port.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_p_port.tStart = t  # underestimates by a little under one frame
            stim_p_port.frameNStart = frameN  # exact frame index
            stim_p_port.status = STARTED
            stim_p_port.setData(int(stimTrig))
        if stim_p_port.status == STARTED and t >= (.5 + (.51-win.monitorFramePeriod*0.75)): #most of one frame period left
            stim_p_port.status = STOPPED
            stim_p_port.setData(int(0))           
        
        
        # *fb_team* updates
        if t >= 0 and fb_team.status == NOT_STARTED:
            # keep track of start time/frame for later
            fb_team.tStart = t  # underestimates by a little under one frame
            fb_team.frameNStart = frameN  # exact frame index
            fb_team.setAutoDraw(True)
            #Writes team name & current image to edf.             
            tracker.sendMessage("TRIALID " + str(fb_team.text))
            tracker.sendMessage("Current image = " + fb_images.image)
            tracker.sendMessage("!V IMGLOAD " + fb_images.image)
        if fb_team.status == STARTED and t >= (0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            fb_team.setAutoDraw(False)
                
        # *fb_images* updates
        if t >= 0 and fb_images.status == NOT_STARTED:
            # keep track of start time/frame for later
            fb_images.tStart = t  # underestimates by a little under one frame
            fb_images.frameNStart = frameN  # exact frame index
            fb_images.setAutoDraw(True)
        if fb_images.status == STARTED and t >= (0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            fb_images.setAutoDraw(False)
        
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
    thisExp.nextEntry()
    #Stops recording at the end of the trial (misses fixation cross)
    tracker.sendMessage("TRIAL_RESULT " + fb_images.image + " completed")   
    tracker.stopRecording()
#------Prepare to start Routine "outro"-------
t = 0
outroClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
outroComponents = []
outroComponents.append(outro_scr)
for thisComponent in outroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#------Prepare to start Routine "outro"-------  

t = 0
outroClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
space_end = event.BuilderKeyResponse()  # create an object of type KeyResponse
space_end.status = NOT_STARTED
# keep track of which components have finished
outroComponents = []
outroComponents.append(outro_scr)
outroComponents.append(space_end)
for thisComponent in outroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "outro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = outroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *outro_scr* updates
    if t >= 0.0 and outro_scr.status == NOT_STARTED:
        # keep track of start time/frame for later
        outro_scr.tStart = t  # underestimates by a little under one frame
        outro_scr.frameNStart = frameN  # exact frame index
        outro_scr.setAutoDraw(True)
    if outro_scr.status == STARTED and (0):
        outro_scr.setAutoDraw(False)
    
    # *space_end* updates
    if t >= 0.0 and space_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        space_end.tStart = t  # underestimates by a little under one frame
        space_end.frameNStart = frameN  # exact frame index
        space_end.status = STARTED
        # keyboard checking is just starting
        space_end.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if space_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])    
      
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in outroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit:
    if "escape" in theseKeys:
        endExpNow = True
    if len(theseKeys) > 0:  # at least one key was pressed
        space_end.keys = theseKeys[-1]  # just the last key pressed
        space_end.rt = space_start.clock.getTime()
        # a response ends the routine
        continueRoutine = False    

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "outro"-------
for thisComponent in outroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "outro" was not non-slip safe, so reset the non-slip timer


#Ends eyetracker mode, sends data to stim pc.    
msecDelay(10)
tracker.closeDataFile
tracker.receiveDataFile(edfFileName, edfFileName)
tracker.close() 
 
routineTimer.reset()
win.close()
core.quit()