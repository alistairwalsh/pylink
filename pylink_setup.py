# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, logging, sound, gui, parallel

#Pylink imports
import pylink
import pygame

from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

import os  # handy system and path functions


                   ####BEGIN EYELINK CODE####

#Makes an instance of the eyetracker to interact with
tracker = EyeLink()

#Gets display information so it doesn't need to be manually set 
#NOTE: Change this if specific resolution is required. 
disp = getDisplayInformation()