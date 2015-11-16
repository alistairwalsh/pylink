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
 
setCalibrationColors((255, 255, 255), (0, 0, 0));   #Sets the calibration target and background color
setTargetSize(int(surf.get_rect().w/70), int(surf.get_rect().w/300));   #select best size for calibration target
setCalibrationSounds("", "", "");
setDriftCorrectSounds("", "off", "off");

tracker.doTrackerSetup()

closeGraphics()

msecDelay(1000)

                    ###PASTE PSYCHOPY SCRIPT BELOW###

#the window set up below is accurate for the eyelink setup in ATC level 4 labs, so leave as is and insert the rest of the task code below it.

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

                    #insert psychopy task code here



#Ends eyetracker mode, sends data to stim pc.    
msecDelay(10)
tracker.closeDataFile
tracker.receiveDataFile(edfFileName, edfFileName)
tracker.close() 
#the above lines are required to close the tracker file. make sure there are no win.close and core.quit lines before the tracker closing. 

routineTimer.reset()
win.close()
core.quit()