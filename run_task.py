#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Mon Nov  2 19:27:54 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'run_task'  # from the Builder filename that created this script
expInfo = {'Please enter your email below to recieve credit for this task:': '', 'test': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Please enter your email below to recieve credit for this task:'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/benmuzekari/Desktop/neuroperfect_task/run_task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-.9,-.9,-.9], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "initialize_stim_and_key_variables"
initialize_stim_and_key_variablesClock = core.Clock()
# skip subject id
participant = 'n/a'

# intizalize quiz and attention check count
quiz_and_attention_check_fails

# initialize custom instructions

instructions_slide_one = visual.ImageStim(win=win,
                        image='instructions/Slide_01_instructions.png',
                        size = (1,.75))

instructions_slide_two = visual.ImageStim(win=win,
                        image='instructions/Slide_02.1_instructions.png',
                        size = (1,.75))
                        
instructions_slide_two_second = visual.ImageStim(win=win,
                        image='instructions/Slide_02.2_instructions.png',
                        size = (1,.75))

instructions_slide_three = visual.ImageStim(win=win,
                        image='instructions/Slide_03_instructions.png',
                        size = (1,.75))

instructions_slide_four = visual.ImageStim(win=win,
                        image='instructions/Slide_04_instructions.png',
                        size = (1,.75))
                        
instructions_slide_five = visual.ImageStim(win=win,
                        image='instructions/Slide_05_instructions.png',
                        size = (1,.75))
                        
instructions_slide_six = visual.ImageStim(win=win,
                        image='instructions/Slide_06_instructions.png',
                        size = (1,.75))
                        
instructions_slide_seven = visual.ImageStim(win=win,
                        image='instructions/Slide_07.jpg',
                        size = (1,.75))                        
                        
instructions_slide_8_01 = visual.ImageStim(win=win,
                        image='instructions/Slide_08.1_instructions.png',
                        size = (1,.75))
                        
instructions_slide_8_02 = visual.ImageStim(win=win,
                        image='instructions/Slide_08.2_instructions.png',
                        size = (1,.75))
                        
instructions_slide_8_03 = visual.ImageStim(win=win,
                        image='instructions/Slide_08.3_instructions.png',
                        size = (1,.75))
                        
instructions_slide_09_01 = visual.ImageStim(win=win,
                        image='instructions/Slide_09.1_instructions.png',
                        size = (1,.75))
                        
instructions_slide_09_02 = visual.ImageStim(win=win,
                        image='instructions/Slide_09.2_instructions.png',
                        size = (1,.75))
                        
instructions_slide_10_01 = visual.ImageStim(win=win,
                        image='instructions/Slide_10.1_instructions.png',
                        size = (1.0,.75))
                        
instructions_slide_10_02 = visual.ImageStim(win=win,
                        image='instructions/Slide_10.2_instructions.png',
                        size = (1.0,.75))
                        
instructions_slide_eleven = visual.ImageStim(win=win,
                        image='instructions/Slide_11_instructions.png',
                        size = (1,.75))                        

instructions_slide_twelve = visual.ImageStim(win=win,
                        image='instructions/Slide_12_instructions.png',
                        size = (1,.75))

instructions_slide_thirteen = visual.ImageStim(win=win,
                        image='instructions/Slide_13_instructions.png',
                        size = (1,.75))

instructions_slide_fourteen = visual.ImageStim(win=win,
                        image='instructions/Slide_14_instructions.png',
                        size = (1,.75))
                        
max_points = visual.ImageStim(win=win,
                        image='instructions/maximize_points.png',
                        size = (1,.75))    
                        
intro_to_kb = visual.ImageStim(win=win,
                        image='instructions/introduce_keyboard.png',
                        size = (1,.75))
                        
intro_to_kb_old = visual.ImageStim(win=win,
                        image='instructions/introduce_kb.png',
                        size = (1,.75))

# initialize feedback stimuli
horizontal_feedback_stim = visual.ImageStim(win=win,
                        image='stimuli/horizontal_feedback.png',
                        size = (0.15, 0.15))

vertical_feedback_stim = visual.ImageStim(win=win,
                        image='stimuli/vertical_feedback.png',
                        size = (0.15, 0.15))

grey_no_feedback_stim = visual.ImageStim(win=win,
                        image='stimuli/noninformative_feedback.png',
                        size = (0.15, 0.15))
                        
# initialize feedback choice stimuli
feedback_choice_screen = visual.ImageStim(win=win,
                        image='feedback_choice/feedback_choice.png',
                        size = (1,.75))
                        
feedback_no_screen = visual.ImageStim(win=win,
                        image='feedback_choice/feedback_no.png',
                        size = (1,.75))
                        
feedback_yes_screen = visual.ImageStim(win=win,
                        image='feedback_choice/feedback_yes.png',
                        size = (1,.75))
                        
# initalize fractals
fractal_blossom = visual.ImageStim(win=win,
                        image='stimuli/fractal_blossom.png',
                        size = (0.15, 0.15))

fractal_octopus = visual.ImageStim(win=win,
                        image='stimuli/fractal_octopus.png',
                        size = (0.15, 0.15))

# initialize calibration slides
calibration_slide_1 = visual.ImageStim(win=win,
                        image='calibration/slide1.png',
                        size = (1,.75))
                        
calibration_slide_2 = visual.ImageStim(win=win,
                        image='calibration/slide2.png',
                        size = (1,.75))
                        
calibration_slide_3 = visual.ImageStim(win=win,
                        image='calibration/slide3.png',
                        size = (1,.75))
                        
calibration_slide_4 = visual.ImageStim(win=win,
                        image='calibration/slide4.png',
                        size = (1,.75))
                        
calibration_slide_5 = visual.ImageStim(win=win,
                        image='calibration/slide5.png',
                        size = (1,.75))
                        
calibration_slide_6 = visual.ImageStim(win=win,
                        image='calibration/slide6.png',
                        size = (1,.75))
                        
calibration_slide_7 = visual.ImageStim(win=win,
                        image='calibration/slide7.png',
                        size = (1,.75))
                        
calibration_slide_8 = visual.ImageStim(win=win,
                        image='calibration/slide8.png',
                        size = (1,.75))
                        
calibration_slide_9 = visual.ImageStim(win=win,
                        image='calibration/slide9.png',
                        size = (1,.75))
                        
calibration_slide_10 = visual.ImageStim(win=win,
                        image='calibration/slide10.png',
                        size = (1,.75))
                        
calibration_slide_11 = visual.ImageStim(win=win,
                        image='calibration/slide11.png',
                        size = (1,.75))
                        
calibration_slide_12 = visual.ImageStim(win=win,
                        image='calibration/slide12.png',
                        size = (1,.75))
                        
calibration_slide_13 = visual.ImageStim(win=win,
                        image='calibration/slide13.png',
                        size = (1,.75))
                        
                        
# initialize post task slides
post_task_completion_slide = visual.ImageStim(win=win,
                        image='post_task/Slide_15.jpg',
                        size = (1,.75))
                        
post_task_continue_slide = visual.ImageStim(win=win,
                        image='post_task/Slide_16.jpg',
                        size = (1,.75))
                        
post_task_fractal_slide = visual.ImageStim(win=win,
                        image='post_task/Slide_17.jpg',
                        size = (1,.75))
                        
post_task_fractal_1_selected_slide = visual.ImageStim(win=win,
                        image='post_task/Slide_18.jpg',
                        size = (1,.75))
                        
post_task_fractal_2_selected_slide = visual.ImageStim(win=win,
                        image='post_task/Slide_19.jpg',
                        size = (1,.75))
                        
# initialize comprehension check slides

correct_feedback_reminder = visual.ImageStim(win=win,
                        image='comprehension_checks/correct_feedback_reminder.png',
                        size = (1,.75))

correct_fractal_reminder = visual.ImageStim(win=win,
                        image='comprehension_checks/correct_fractal_reminder.png',
                        size = (1,.75))

correct_result_no_feedback = visual.ImageStim(win=win,
                        image='comprehension_checks/correct_result_no_feedback.png',
                        size = (1,.75))

correct_result_plus_one = visual.ImageStim(win=win,
                        image='comprehension_checks/correct_result_plus_one.png',
                        size = (1.0,.75))
                        
correct_result_plus_zero = visual.ImageStim(win=win,
                        image='comprehension_checks/correct_result_plus_zero.png',
                        size = (1,.75))
                        
correct_shape = visual.ImageStim(win=win,
                        image='comprehension_checks/correct_shape.png',
                        size = (1,.75))
                        
incorrect_feedback_reminder = visual.ImageStim(win=win,
                        image='comprehension_checks/incorrect_feedback_reminder.png',
                        size = (1,.75))
                        
incorrect_fractal_reminder = visual.ImageStim(win=win,
                        image='comprehension_checks/incorrect_fractal_reminder.png',
                        size = (1,.75))
                        
incorrect_result_no_feedback = visual.ImageStim(win=win,
                        image='comprehension_checks/incorrect_result_no_feedback.png',
                        size = (1,.75))
                        
incorrect_result_plus_one = visual.ImageStim(win=win,
                        image='comprehension_checks/incorrect_result_plus_one.png',
                        size = (1,.75))
                        
incorrect_result_plus_zero = visual.ImageStim(win=win,
                        image='comprehension_checks/incorrect_result_plus_zero.png',
                        size = (1,.75))
                        
incorrect_shape = visual.ImageStim(win=win,
                        image='comprehension_checks/incorrect_shape.png',
                        size = (1,.75))
                        
press_fractal_left = visual.ImageStim(win=win,
                        image='comprehension_checks/press_fractal_left.png',
                        size = (1,.75))
                        
press_fractal_right = visual.ImageStim(win=win,
                        image='comprehension_checks/press_fractal_right.png',
                        size = (1,.75))
                        
press_no_feedback = visual.ImageStim(win=win,
                        image='comprehension_checks/press_no_feedback.png',
                        size = (1,.75))
                        
press_yes_feedback = visual.ImageStim(win=win,
                        image='comprehension_checks/press_yes_feedback.png',
                        size = (1,.75))
                        
result_final_reminder = visual.ImageStim(win=win,
                        image='comprehension_checks/result_final_reminder.png',
                        size = (1,.75))
                        
shapes_question = visual.ImageStim(win=win,
                        image='comprehension_checks/attention_check_shapes.png',
                        size = (1,.75))
                        
# initialize blank screen
blank_screen_image_black = visual.ImageStim(win=win,
                        image='stimuli/blank_screen.png',
                        size = (1,.75))
# add data about conditions
psychoJS.experiment.addData('condition', condition)
psychoJS.experiment.addData('excel_sheet_choice_practice', excel_sheet_choice_practice)
psychoJS.experiment.addData('excel_sheet_choice_main', excel_sheet_choice_main)
psychoJS.experiment.addData('instruction_slide_2_selection', instruction_slide_2_selection)
psychoJS.experiment.addData('select_key_to_press', select_key_to_press)
psychoJS.experiment.addData('select_feedback_to_press', select_feedback_to_press)
psychoJS.experiment.addData('random_feedback_stim', random_feedback_stim)
psychoJS.experiment.addData('post_task_fractal_selection', post_task_fractal_selection)

# Initialize components for Routine "welcome_slide"
welcome_slideClock = core.Clock()
slide_1_inst = visual.ImageStim(
    win=win,
    name='slide_1_inst', 
    image='instructions/Slide_01_instructions.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
welcome_slide_key_resp = keyboard.Keyboard()

# Initialize components for Routine "SAM_hu_directions"
SAM_hu_directionsClock = core.Clock()
SAM_hu_instructions = visual.ImageStim(
    win=win,
    name='SAM_hu_instructions', 
    image='SAM/SAM_hu_ins.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
SAM_hu_instructions_key_resp = keyboard.Keyboard()

# Initialize components for Routine "SAM_hu_question"
SAM_hu_questionClock = core.Clock()
SAM_hu = visual.ImageStim(
    win=win,
    name='SAM_hu', 
    image='SAM/SAM_hu.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
choice_1 = visual.Polygon(
    win=win, name='choice_1',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.30, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
choice_2 = visual.Polygon(
    win=win, name='choice_2',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.22, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
choice_3 = visual.Polygon(
    win=win, name='choice_3',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.15, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
choice_4 = visual.Polygon(
    win=win, name='choice_4',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.07, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
choice_5 = visual.Polygon(
    win=win, name='choice_5',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(0, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
choice_6 = visual.Polygon(
    win=win, name='choice_6',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.07, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
choice_7 = visual.Polygon(
    win=win, name='choice_7',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.15, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
choice_8 = visual.Polygon(
    win=win, name='choice_8',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.22, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
choice_9 = visual.Polygon(
    win=win, name='choice_9',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.3, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
select_answer_mouse_sam_hu = event.Mouse(win=win)
x, y = [None, None]
select_answer_mouse_sam_hu.mouseClock = core.Clock()

# Initialize components for Routine "highlight_sam_hu_pre_choice"
highlight_sam_hu_pre_choiceClock = core.Clock()
Sam_hu_highlight_pre = visual.ImageStim(
    win=win,
    name='Sam_hu_highlight_pre', 
    image='SAM/SAM_hu.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "SAM_ec_directions"
SAM_ec_directionsClock = core.Clock()
SAM_ec_instructions = visual.ImageStim(
    win=win,
    name='SAM_ec_instructions', 
    image='SAM/SAM_ec_ins.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
SAM_ec_instructions_key_resp = keyboard.Keyboard()

# Initialize components for Routine "SAM_ec_question"
SAM_ec_questionClock = core.Clock()
SAM_ec = visual.ImageStim(
    win=win,
    name='SAM_ec', 
    image='SAM/SAM_ec.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
choice_num_1 = visual.Polygon(
    win=win, name='choice_num_1',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.30, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
choice_num_2 = visual.Polygon(
    win=win, name='choice_num_2',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.22, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
choice_num_3 = visual.Polygon(
    win=win, name='choice_num_3',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.15, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
choice_num_4 = visual.Polygon(
    win=win, name='choice_num_4',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.07, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
choice_num_5 = visual.Polygon(
    win=win, name='choice_num_5',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(0, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
choice_num_6 = visual.Polygon(
    win=win, name='choice_num_6',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.07, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
choice_num_7 = visual.Polygon(
    win=win, name='choice_num_7',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.15, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
choice_num_8 = visual.Polygon(
    win=win, name='choice_num_8',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.22, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
choice_num_9 = visual.Polygon(
    win=win, name='choice_num_9',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.3, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
select_answer_mouse_sam_ec = event.Mouse(win=win)
x, y = [None, None]
select_answer_mouse_sam_ec.mouseClock = core.Clock()

# Initialize components for Routine "highlight_sam_ec_pre_choice"
highlight_sam_ec_pre_choiceClock = core.Clock()
sam_ec_pre_highlight = visual.ImageStim(
    win=win,
    name='sam_ec_pre_highlight', 
    image='SAM/SAM_ec.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "introduce_keyboard_hand_positioning"
introduce_keyboard_hand_positioningClock = core.Clock()
draw_kb_key_resp = keyboard.Keyboard()

# Initialize components for Routine "begin_instructions"
begin_instructionsClock = core.Clock()
begin_task_instructions_key_resp = keyboard.Keyboard()

# Initialize components for Routine "continue_begin"
continue_beginClock = core.Clock()
slide_two_key_response = keyboard.Keyboard()

# Initialize components for Routine "slide_max_points"
slide_max_pointsClock = core.Clock()
max_points_slide_key_resp = keyboard.Keyboard()

# Initialize components for Routine "fractal_selection_quiz"
fractal_selection_quizClock = core.Clock()
# initialize empty lists
select_key_to_press_slide = []
key_to_press_outcome = [] 

# set stim to draw
if select_key_to_press == 1:
    select_key_to_press_slide = press_fractal_left
elif select_key_to_press == 2:
    select_key_to_press_slide = press_fractal_right

fractal_selection_quiz_key_resp = keyboard.Keyboard()

# Initialize components for Routine "fractal_reminder_show"
fractal_reminder_showClock = core.Clock()
fractal_reminder_show_key_resp = keyboard.Keyboard()

# Initialize components for Routine "draw_slide_3"
draw_slide_3Clock = core.Clock()
slide_3_key_resp = keyboard.Keyboard()

# Initialize components for Routine "display_feedback_meanings"
display_feedback_meaningsClock = core.Clock()
display_feedback_meanings_key_resp = keyboard.Keyboard()

# Initialize components for Routine "first_quiz_first_question"
first_quiz_first_questionClock = core.Clock()
# initialize empty lists so we can add data
first_stim_quiz_first_question_result = []
first_stim_quiz_second_question_result = []
first_stim_quiz_third_question_result = []
first_quiz_first_question_key_resp = keyboard.Keyboard()

# Initialize components for Routine "first_quiz_first_question_reminder"
first_quiz_first_question_reminderClock = core.Clock()
first_quiz_first_q_reminder_key_resp = keyboard.Keyboard()

# Initialize components for Routine "first_quiz_second_question"
first_quiz_second_questionClock = core.Clock()
first_quiz_second_question_key_resp = keyboard.Keyboard()

# Initialize components for Routine "first_quiz_second_question_reminder"
first_quiz_second_question_reminderClock = core.Clock()
first_quiz_second_question_reminder_key_resp = keyboard.Keyboard()

# Initialize components for Routine "first_quiz_third_question"
first_quiz_third_questionClock = core.Clock()
last_q_first_quiz_key_resp = keyboard.Keyboard()

# Initialize components for Routine "first_quiz_third_question_reminder"
first_quiz_third_question_reminderClock = core.Clock()
first_quiz_third_question_reminder_key_resp = keyboard.Keyboard()

# Initialize components for Routine "total_reminder_one"
total_reminder_oneClock = core.Clock()
first_reminder_key_resp = keyboard.Keyboard()

# Initialize components for Routine "continue_instructions_8_01"
continue_instructions_8_01Clock = core.Clock()
slide_8_01_key_resp = keyboard.Keyboard()

# Initialize components for Routine "continue_instructions_8_02"
continue_instructions_8_02Clock = core.Clock()
slide_8_02_key_resp = keyboard.Keyboard()

# Initialize components for Routine "continue_instructions_8_03"
continue_instructions_8_03Clock = core.Clock()
slide_8_03_key_resp = keyboard.Keyboard()

# Initialize components for Routine "feedback_selection_quiz"
feedback_selection_quizClock = core.Clock()
# initialize empty lists so we can add outcome
select_feedback_to_press_slide = []
feedback_to_press_outcome = [] 

# set stim to draw
if select_feedback_to_press == 1:
    select_feedback_to_press_slide = press_no_feedback
elif select_feedback_to_press == 2:
    select_feedback_to_press_slide = press_yes_feedback
feedback_selection_quiz_key_resp = keyboard.Keyboard()

# Initialize components for Routine "feedback_post_quiz_reminder"
feedback_post_quiz_reminderClock = core.Clock()
feedback_post_quiz_reminder_key_resp = keyboard.Keyboard()

# Initialize components for Routine "continue_slide_09_01"
continue_slide_09_01Clock = core.Clock()
slide_09_01_key_resp = keyboard.Keyboard()

# Initialize components for Routine "continue_slide_09_02"
continue_slide_09_02Clock = core.Clock()
slide_09_02_key_resp = keyboard.Keyboard()

# Initialize components for Routine "continue_slide_10_01"
continue_slide_10_01Clock = core.Clock()
slide_10_01_key_resp = keyboard.Keyboard()

# Initialize components for Routine "continue_slide_10_02"
continue_slide_10_02Clock = core.Clock()
slide_10_02_key_resp = keyboard.Keyboard()

# Initialize components for Routine "attention_shape_check"
attention_shape_checkClock = core.Clock()
# initialize empty lists so we can add data
shape_quiz_result = []
get_shape_response = keyboard.Keyboard()

# Initialize components for Routine "attention_reminder"
attention_reminderClock = core.Clock()
attention_reminder_key_resp = keyboard.Keyboard()

# Initialize components for Routine "continue_instructions_even_further_11"
continue_instructions_even_further_11Clock = core.Clock()
slide_11_key_resp = keyboard.Keyboard()

# Initialize components for Routine "calib_one"
calib_oneClock = core.Clock()
calib_one_space = keyboard.Keyboard()

# Initialize components for Routine "calib_last"
calib_lastClock = core.Clock()
calibration_space_bar_press = keyboard.Keyboard()

# Initialize components for Routine "advance_to_practice_session"
advance_to_practice_sessionClock = core.Clock()
enter_to_practice_session = keyboard.Keyboard()

# Initialize components for Routine "practice_task"
practice_taskClock = core.Clock()
# initalize so we can add data to these variables
prac_trial_num = 0
prac_total_points = 0

iti_prac = visual.ShapeStim(
    win=win, name='iti_prac', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=.01, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
fractal_one_prac = visual.ImageStim(
    win=win,
    name='fractal_one_prac', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
fractal_two_prac = visual.ImageStim(
    win=win,
    name='fractal_two_prac', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
key_resp_prac = keyboard.Keyboard()

# Initialize components for Routine "isi_screen"
isi_screenClock = core.Clock()
isi_stim = visual.ShapeStim(
    win=win, name='isi_stim', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=.01, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "missed_trial_logic"
missed_trial_logicClock = core.Clock()
missed_trial_practice = visual.TextStim(win=win, name='missed_trial_practice',
    text='No response recorded',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "no_feedback_work_logic"
no_feedback_work_logicClock = core.Clock()
no_feedback_work_image = visual.ImageStim(
    win=win,
    name='no_feedback_work_image', 
    image=load_feedback_stim_to_draw, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "grey_work_for_fb"
grey_work_for_fbClock = core.Clock()
grey_stim_work_for_fb = visual.ImageStim(
    win=win,
    name='grey_stim_work_for_fb', 
    image=load_feedback_stim_to_draw, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "ask_want_to_work_for_feedback"
ask_want_to_work_for_feedbackClock = core.Clock()
feedback_choice_key_resp = keyboard.Keyboard()
feedback_choice_slide = visual.ImageStim(
    win=win,
    name='feedback_choice_slide', 
    image='feedback_choice/feedback_choice.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "no_fb_highlight"
no_fb_highlightClock = core.Clock()
no_fb_slide = visual.ImageStim(
    win=win,
    name='no_fb_slide', 
    image='feedback_choice/feedback_no.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "yes_fb_highlight"
yes_fb_highlightClock = core.Clock()
yes_fb_slide = visual.ImageStim(
    win=win,
    name='yes_fb_slide', 
    image='feedback_choice/feedback_yes.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "fb_work_time"
fb_work_timeClock = core.Clock()

# Initialize components for Routine "draw_feedback_to_screen"
draw_feedback_to_screenClock = core.Clock()
work_for_feedback_space_bar_press = keyboard.Keyboard()

# Initialize components for Routine "post_work_blank"
post_work_blankClock = core.Clock()
blank_image = visual.ImageStim(
    win=win,
    name='blank_image', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
post_work_space_presses = keyboard.Keyboard()

# Initialize components for Routine "end_loop_data_log"
end_loop_data_logClock = core.Clock()

# Initialize components for Routine "blank_screen_2"
blank_screen_2Clock = core.Clock()
blank_slide_2 = visual.TextStim(win=win, name='blank_slide_2',
    text='       ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "second_quiz"
second_quizClock = core.Clock()
# initialize empty lists so we can add data
second_stim_quiz_first_question_result = []
second_stim_quiz_second_question_result = []
second_stim_quiz_third_question_result = []
start_second_quiz = keyboard.Keyboard()

# Initialize components for Routine "second_quiz_first_question"
second_quiz_first_questionClock = core.Clock()
first_q_second_quiz_resp = keyboard.Keyboard()

# Initialize components for Routine "second_quiz_first_question_reminder"
second_quiz_first_question_reminderClock = core.Clock()
advance_q_2_quiz_2 = keyboard.Keyboard()

# Initialize components for Routine "second_quiz_second_question"
second_quiz_second_questionClock = core.Clock()
resp_q_2_q_2 = keyboard.Keyboard()

# Initialize components for Routine "second_quiz_second_question_reminder"
second_quiz_second_question_reminderClock = core.Clock()
advance_q_3_quiz_2 = keyboard.Keyboard()

# Initialize components for Routine "second_quiz_third_question"
second_quiz_third_questionClock = core.Clock()
resp_quiz_2_q_3 = keyboard.Keyboard()

# Initialize components for Routine "second_quiz_third_question_reminder"
second_quiz_third_question_reminderClock = core.Clock()
advance_from_second_quiz = keyboard.Keyboard()

# Initialize components for Routine "last_stim_reminder"
last_stim_reminderClock = core.Clock()
advance_from_last_reminder = keyboard.Keyboard()

# Initialize components for Routine "advance_to_main_task"
advance_to_main_taskClock = core.Clock()
enter_main_game = keyboard.Keyboard()

# Initialize components for Routine "main_task"
main_taskClock = core.Clock()
# initalize so we can add data to these variables
main_trial_num = 0
main_total_points = 0
iti_main = visual.ShapeStim(
    win=win, name='iti_main', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=.01, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
fractal_one_main = visual.ImageStim(
    win=win,
    name='fractal_one_main', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
fractal_two_main = visual.ImageStim(
    win=win,
    name='fractal_two_main', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
key_resp_main = keyboard.Keyboard()

# Initialize components for Routine "isi_screen"
isi_screenClock = core.Clock()
isi_stim = visual.ShapeStim(
    win=win, name='isi_stim', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=.01, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "missed_trial_logic"
missed_trial_logicClock = core.Clock()
missed_trial_practice = visual.TextStim(win=win, name='missed_trial_practice',
    text='No response recorded',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "no_feedback_work_logic"
no_feedback_work_logicClock = core.Clock()
no_feedback_work_image = visual.ImageStim(
    win=win,
    name='no_feedback_work_image', 
    image=load_feedback_stim_to_draw, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "grey_work_for_fb"
grey_work_for_fbClock = core.Clock()
grey_stim_work_for_fb = visual.ImageStim(
    win=win,
    name='grey_stim_work_for_fb', 
    image=load_feedback_stim_to_draw, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "ask_want_to_work_for_feedback"
ask_want_to_work_for_feedbackClock = core.Clock()
feedback_choice_key_resp = keyboard.Keyboard()
feedback_choice_slide = visual.ImageStim(
    win=win,
    name='feedback_choice_slide', 
    image='feedback_choice/feedback_choice.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "no_fb_highlight"
no_fb_highlightClock = core.Clock()
no_fb_slide = visual.ImageStim(
    win=win,
    name='no_fb_slide', 
    image='feedback_choice/feedback_no.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "yes_fb_highlight"
yes_fb_highlightClock = core.Clock()
yes_fb_slide = visual.ImageStim(
    win=win,
    name='yes_fb_slide', 
    image='feedback_choice/feedback_yes.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "fb_work_time"
fb_work_timeClock = core.Clock()

# Initialize components for Routine "draw_feedback_to_screen"
draw_feedback_to_screenClock = core.Clock()
work_for_feedback_space_bar_press = keyboard.Keyboard()

# Initialize components for Routine "post_work_blank"
post_work_blankClock = core.Clock()
blank_image = visual.ImageStim(
    win=win,
    name='blank_image', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
post_work_space_presses = keyboard.Keyboard()

# Initialize components for Routine "end_loop_data_log"
end_loop_data_logClock = core.Clock()

# Initialize components for Routine "blank_screen_2"
blank_screen_2Clock = core.Clock()
blank_slide_2 = visual.TextStim(win=win, name='blank_slide_2',
    text='       ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "completed_main_task"
completed_main_taskClock = core.Clock()
post_task_image = visual.ImageStim(
    win=win,
    name='post_task_image', 
    image='post_task/Slide_15.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "continue_to_fractal_question"
continue_to_fractal_questionClock = core.Clock()
go_to_fractal_question = keyboard.Keyboard()

# Initialize components for Routine "post_task_fractal_question"
post_task_fractal_questionClock = core.Clock()
choose_fractal = keyboard.Keyboard()

# Initialize components for Routine "SAM_hu_directions"
SAM_hu_directionsClock = core.Clock()
SAM_hu_instructions = visual.ImageStim(
    win=win,
    name='SAM_hu_instructions', 
    image='SAM/SAM_hu_ins.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
SAM_hu_instructions_key_resp = keyboard.Keyboard()

# Initialize components for Routine "SAM_hu_question_2"
SAM_hu_question_2Clock = core.Clock()
SAM_hu_2 = visual.ImageStim(
    win=win,
    name='SAM_hu_2', 
    image='SAM/SAM_hu.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
choice_1_post = visual.Polygon(
    win=win, name='choice_1_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.30, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
choice_2_post = visual.Polygon(
    win=win, name='choice_2_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.22, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
choice_3_post = visual.Polygon(
    win=win, name='choice_3_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.15, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
choice_4_post = visual.Polygon(
    win=win, name='choice_4_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.07, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
choice_5_post = visual.Polygon(
    win=win, name='choice_5_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(0, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
choice_6_post = visual.Polygon(
    win=win, name='choice_6_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.07, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
choice_7_post = visual.Polygon(
    win=win, name='choice_7_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.15, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
choice_8_post = visual.Polygon(
    win=win, name='choice_8_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.22, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
choice_9_post = visual.Polygon(
    win=win, name='choice_9_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.3, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
select_answer_mouse_3 = event.Mouse(win=win)
x, y = [None, None]
select_answer_mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "highlight_post_sam_hu"
highlight_post_sam_huClock = core.Clock()
sam_hu_highlight_post = visual.ImageStim(
    win=win,
    name='sam_hu_highlight_post', 
    image='SAM/SAM_hu.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "SAM_ec_directions"
SAM_ec_directionsClock = core.Clock()
SAM_ec_instructions = visual.ImageStim(
    win=win,
    name='SAM_ec_instructions', 
    image='SAM/SAM_ec_ins.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
SAM_ec_instructions_key_resp = keyboard.Keyboard()

# Initialize components for Routine "SAM_ec_question_2"
SAM_ec_question_2Clock = core.Clock()
SAM_ec_2 = visual.ImageStim(
    win=win,
    name='SAM_ec_2', 
    image='SAM/SAM_ec.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
choice_num_1_post = visual.Polygon(
    win=win, name='choice_num_1_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.30, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
choice_num_2_post = visual.Polygon(
    win=win, name='choice_num_2_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.22, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
choice_num_3_post = visual.Polygon(
    win=win, name='choice_num_3_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.15, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
choice_num_4_post = visual.Polygon(
    win=win, name='choice_num_4_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(-.07, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
choice_num_5_post = visual.Polygon(
    win=win, name='choice_num_5_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(0, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
choice_num_6_post = visual.Polygon(
    win=win, name='choice_num_6_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.07, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
choice_num_7_post = visual.Polygon(
    win=win, name='choice_num_7_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.15, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
choice_num_8_post = visual.Polygon(
    win=win, name='choice_num_8_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.22, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
choice_num_9_post = visual.Polygon(
    win=win, name='choice_num_9_post',
    edges=100, size=(0.03, 0.03),
    ori=0, pos=(.3, -.18),
    lineWidth=1, lineColor=[-.9,-.9,-.9], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
select_answer_mouse_4 = event.Mouse(win=win)
x, y = [None, None]
select_answer_mouse_4.mouseClock = core.Clock()

# Initialize components for Routine "highlight_sam_ec_post_choice"
highlight_sam_ec_post_choiceClock = core.Clock()
sam_ec_post_highlight = visual.ImageStim(
    win=win,
    name='sam_ec_post_highlight', 
    image='SAM/SAM_ec.png', mask=None,
    ori=0, pos=(0, 0), size=(1,.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "total_points_end_experiment"
total_points_end_experimentClock = core.Clock()
final_total_points = visual.TextStim(win=win, name='final_total_points',
    text='default text',
    font='Arial',
    pos=(-.07, .03), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rest_of_text = visual.TextStim(win=win, name='rest_of_text',
    text='You have earned         out of a possible 160 points.\n\nPlease click any button to exit.',
    font='Arial',
    pos=(0, -.01), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
exit_task = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "initialize_stim_and_key_variables"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
initialize_stim_and_key_variablesComponents = []
for thisComponent in initialize_stim_and_key_variablesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initialize_stim_and_key_variablesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initialize_stim_and_key_variables"-------
while continueRoutine:
    # get current time
    t = initialize_stim_and_key_variablesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initialize_stim_and_key_variablesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initialize_stim_and_key_variablesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initialize_stim_and_key_variables"-------
for thisComponent in initialize_stim_and_key_variablesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initialize_stim_and_key_variables" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_slide"-------
continueRoutine = True
# update component parameters for each repeat
welcome_slide_key_resp.keys = []
welcome_slide_key_resp.rt = []
_welcome_slide_key_resp_allKeys = []
# keep track of which components have finished
welcome_slideComponents = [slide_1_inst, welcome_slide_key_resp]
for thisComponent in welcome_slideComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_slide"-------
while continueRoutine:
    # get current time
    t = welcome_slideClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_slideClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_1_inst* updates
    if slide_1_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_1_inst.frameNStart = frameN  # exact frame index
        slide_1_inst.tStart = t  # local t and not account for scr refresh
        slide_1_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_1_inst, 'tStartRefresh')  # time at next scr refresh
        slide_1_inst.setAutoDraw(True)
    
    # *welcome_slide_key_resp* updates
    waitOnFlip = False
    if welcome_slide_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_slide_key_resp.frameNStart = frameN  # exact frame index
        welcome_slide_key_resp.tStart = t  # local t and not account for scr refresh
        welcome_slide_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_slide_key_resp, 'tStartRefresh')  # time at next scr refresh
        welcome_slide_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_slide_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_slide_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_slide_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_slide_key_resp.getKeys(keyList=None, waitRelease=False)
        _welcome_slide_key_resp_allKeys.extend(theseKeys)
        if len(_welcome_slide_key_resp_allKeys):
            welcome_slide_key_resp.keys = _welcome_slide_key_resp_allKeys[-1].name  # just the last key pressed
            welcome_slide_key_resp.rt = _welcome_slide_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_slideComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_slide"-------
for thisComponent in welcome_slideComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slide_1_inst.started', slide_1_inst.tStartRefresh)
thisExp.addData('slide_1_inst.stopped', slide_1_inst.tStopRefresh)
# check responses
if welcome_slide_key_resp.keys in ['', [], None]:  # No response was made
    welcome_slide_key_resp.keys = None
thisExp.addData('welcome_slide_key_resp.keys',welcome_slide_key_resp.keys)
if welcome_slide_key_resp.keys != None:  # we had a response
    thisExp.addData('welcome_slide_key_resp.rt', welcome_slide_key_resp.rt)
thisExp.addData('welcome_slide_key_resp.started', welcome_slide_key_resp.tStartRefresh)
thisExp.addData('welcome_slide_key_resp.stopped', welcome_slide_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome_slide" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SAM_hu_directions"-------
continueRoutine = True
# update component parameters for each repeat
SAM_hu_instructions_key_resp.keys = []
SAM_hu_instructions_key_resp.rt = []
_SAM_hu_instructions_key_resp_allKeys = []
# keep track of which components have finished
SAM_hu_directionsComponents = [SAM_hu_instructions, SAM_hu_instructions_key_resp]
for thisComponent in SAM_hu_directionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SAM_hu_directionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SAM_hu_directions"-------
while continueRoutine:
    # get current time
    t = SAM_hu_directionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SAM_hu_directionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SAM_hu_instructions* updates
    if SAM_hu_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_hu_instructions.frameNStart = frameN  # exact frame index
        SAM_hu_instructions.tStart = t  # local t and not account for scr refresh
        SAM_hu_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_hu_instructions, 'tStartRefresh')  # time at next scr refresh
        SAM_hu_instructions.setAutoDraw(True)
    
    # *SAM_hu_instructions_key_resp* updates
    waitOnFlip = False
    if SAM_hu_instructions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_hu_instructions_key_resp.frameNStart = frameN  # exact frame index
        SAM_hu_instructions_key_resp.tStart = t  # local t and not account for scr refresh
        SAM_hu_instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_hu_instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
        SAM_hu_instructions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SAM_hu_instructions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SAM_hu_instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SAM_hu_instructions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = SAM_hu_instructions_key_resp.getKeys(keyList=None, waitRelease=False)
        _SAM_hu_instructions_key_resp_allKeys.extend(theseKeys)
        if len(_SAM_hu_instructions_key_resp_allKeys):
            SAM_hu_instructions_key_resp.keys = _SAM_hu_instructions_key_resp_allKeys[-1].name  # just the last key pressed
            SAM_hu_instructions_key_resp.rt = _SAM_hu_instructions_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SAM_hu_directionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SAM_hu_directions"-------
for thisComponent in SAM_hu_directionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SAM_hu_instructions.started', SAM_hu_instructions.tStartRefresh)
thisExp.addData('SAM_hu_instructions.stopped', SAM_hu_instructions.tStopRefresh)
# check responses
if SAM_hu_instructions_key_resp.keys in ['', [], None]:  # No response was made
    SAM_hu_instructions_key_resp.keys = None
thisExp.addData('SAM_hu_instructions_key_resp.keys',SAM_hu_instructions_key_resp.keys)
if SAM_hu_instructions_key_resp.keys != None:  # we had a response
    thisExp.addData('SAM_hu_instructions_key_resp.rt', SAM_hu_instructions_key_resp.rt)
thisExp.addData('SAM_hu_instructions_key_resp.started', SAM_hu_instructions_key_resp.tStartRefresh)
thisExp.addData('SAM_hu_instructions_key_resp.stopped', SAM_hu_instructions_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "SAM_hu_directions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SAM_hu_question"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the select_answer_mouse_sam_hu
select_answer_mouse_sam_hu.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
SAM_hu_questionComponents = [SAM_hu, choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7, choice_8, choice_9, select_answer_mouse_sam_hu]
for thisComponent in SAM_hu_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SAM_hu_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SAM_hu_question"-------
while continueRoutine:
    # get current time
    t = SAM_hu_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SAM_hu_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SAM_hu* updates
    if SAM_hu.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_hu.frameNStart = frameN  # exact frame index
        SAM_hu.tStart = t  # local t and not account for scr refresh
        SAM_hu.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_hu, 'tStartRefresh')  # time at next scr refresh
        SAM_hu.setAutoDraw(True)
    
    # *choice_1* updates
    if choice_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_1.frameNStart = frameN  # exact frame index
        choice_1.tStart = t  # local t and not account for scr refresh
        choice_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_1, 'tStartRefresh')  # time at next scr refresh
        choice_1.setAutoDraw(True)
    
    # *choice_2* updates
    if choice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_2.frameNStart = frameN  # exact frame index
        choice_2.tStart = t  # local t and not account for scr refresh
        choice_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_2, 'tStartRefresh')  # time at next scr refresh
        choice_2.setAutoDraw(True)
    
    # *choice_3* updates
    if choice_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_3.frameNStart = frameN  # exact frame index
        choice_3.tStart = t  # local t and not account for scr refresh
        choice_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_3, 'tStartRefresh')  # time at next scr refresh
        choice_3.setAutoDraw(True)
    
    # *choice_4* updates
    if choice_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_4.frameNStart = frameN  # exact frame index
        choice_4.tStart = t  # local t and not account for scr refresh
        choice_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_4, 'tStartRefresh')  # time at next scr refresh
        choice_4.setAutoDraw(True)
    
    # *choice_5* updates
    if choice_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_5.frameNStart = frameN  # exact frame index
        choice_5.tStart = t  # local t and not account for scr refresh
        choice_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_5, 'tStartRefresh')  # time at next scr refresh
        choice_5.setAutoDraw(True)
    
    # *choice_6* updates
    if choice_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_6.frameNStart = frameN  # exact frame index
        choice_6.tStart = t  # local t and not account for scr refresh
        choice_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_6, 'tStartRefresh')  # time at next scr refresh
        choice_6.setAutoDraw(True)
    
    # *choice_7* updates
    if choice_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_7.frameNStart = frameN  # exact frame index
        choice_7.tStart = t  # local t and not account for scr refresh
        choice_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_7, 'tStartRefresh')  # time at next scr refresh
        choice_7.setAutoDraw(True)
    
    # *choice_8* updates
    if choice_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_8.frameNStart = frameN  # exact frame index
        choice_8.tStart = t  # local t and not account for scr refresh
        choice_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_8, 'tStartRefresh')  # time at next scr refresh
        choice_8.setAutoDraw(True)
    
    # *choice_9* updates
    if choice_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_9.frameNStart = frameN  # exact frame index
        choice_9.tStart = t  # local t and not account for scr refresh
        choice_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_9, 'tStartRefresh')  # time at next scr refresh
        choice_9.setAutoDraw(True)
    # *select_answer_mouse_sam_hu* updates
    if select_answer_mouse_sam_hu.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        select_answer_mouse_sam_hu.frameNStart = frameN  # exact frame index
        select_answer_mouse_sam_hu.tStart = t  # local t and not account for scr refresh
        select_answer_mouse_sam_hu.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(select_answer_mouse_sam_hu, 'tStartRefresh')  # time at next scr refresh
        select_answer_mouse_sam_hu.status = STARTED
        select_answer_mouse_sam_hu.mouseClock.reset()
        prevButtonState = select_answer_mouse_sam_hu.getPressed()  # if button is down already this ISN'T a new click
    if select_answer_mouse_sam_hu.status == STARTED:  # only update if started and not finished!
        buttons = select_answer_mouse_sam_hu.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8,choice_9]:
                    if obj.contains(select_answer_mouse_sam_hu):
                        gotValidClick = True
                        select_answer_mouse_sam_hu.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SAM_hu_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SAM_hu_question"-------
for thisComponent in SAM_hu_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SAM_hu.started', SAM_hu.tStartRefresh)
thisExp.addData('SAM_hu.stopped', SAM_hu.tStopRefresh)
thisExp.addData('choice_1.started', choice_1.tStartRefresh)
thisExp.addData('choice_1.stopped', choice_1.tStopRefresh)
thisExp.addData('choice_2.started', choice_2.tStartRefresh)
thisExp.addData('choice_2.stopped', choice_2.tStopRefresh)
thisExp.addData('choice_3.started', choice_3.tStartRefresh)
thisExp.addData('choice_3.stopped', choice_3.tStopRefresh)
thisExp.addData('choice_4.started', choice_4.tStartRefresh)
thisExp.addData('choice_4.stopped', choice_4.tStopRefresh)
thisExp.addData('choice_5.started', choice_5.tStartRefresh)
thisExp.addData('choice_5.stopped', choice_5.tStopRefresh)
thisExp.addData('choice_6.started', choice_6.tStartRefresh)
thisExp.addData('choice_6.stopped', choice_6.tStopRefresh)
thisExp.addData('choice_7.started', choice_7.tStartRefresh)
thisExp.addData('choice_7.stopped', choice_7.tStopRefresh)
thisExp.addData('choice_8.started', choice_8.tStartRefresh)
thisExp.addData('choice_8.stopped', choice_8.tStopRefresh)
thisExp.addData('choice_9.started', choice_9.tStartRefresh)
thisExp.addData('choice_9.stopped', choice_9.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = select_answer_mouse_sam_hu.getPos()
buttons = select_answer_mouse_sam_hu.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8,choice_9]:
        if obj.contains(select_answer_mouse_sam_hu):
            gotValidClick = True
            select_answer_mouse_sam_hu.clicked_name.append(obj.name)
thisExp.addData('select_answer_mouse_sam_hu.x', x)
thisExp.addData('select_answer_mouse_sam_hu.y', y)
thisExp.addData('select_answer_mouse_sam_hu.leftButton', buttons[0])
thisExp.addData('select_answer_mouse_sam_hu.midButton', buttons[1])
thisExp.addData('select_answer_mouse_sam_hu.rightButton', buttons[2])
if len(select_answer_mouse_sam_hu.clicked_name):
    thisExp.addData('select_answer_mouse_sam_hu.clicked_name', select_answer_mouse_sam_hu.clicked_name[0])
thisExp.addData('select_answer_mouse_sam_hu.started', select_answer_mouse_sam_hu.tStart)
thisExp.addData('select_answer_mouse_sam_hu.stopped', select_answer_mouse_sam_hu.tStop)
thisExp.nextEntry()
answer_to_draw = []
for answer in [choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8,choice_9]:
    if select_answer_mouse_sam_hu.isPressedIn(answer):
        answer_to_draw = answer
# the Routine "SAM_hu_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "highlight_sam_hu_pre_choice"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
highlight_sam_hu_pre_choiceComponents = [Sam_hu_highlight_pre]
for thisComponent in highlight_sam_hu_pre_choiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
highlight_sam_hu_pre_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "highlight_sam_hu_pre_choice"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = highlight_sam_hu_pre_choiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=highlight_sam_hu_pre_choiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Sam_hu_highlight_pre* updates
    if Sam_hu_highlight_pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Sam_hu_highlight_pre.frameNStart = frameN  # exact frame index
        Sam_hu_highlight_pre.tStart = t  # local t and not account for scr refresh
        Sam_hu_highlight_pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Sam_hu_highlight_pre, 'tStartRefresh')  # time at next scr refresh
        Sam_hu_highlight_pre.setAutoDraw(True)
    if Sam_hu_highlight_pre.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Sam_hu_highlight_pre.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            Sam_hu_highlight_pre.tStop = t  # not accounting for scr refresh
            Sam_hu_highlight_pre.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Sam_hu_highlight_pre, 'tStopRefresh')  # time at next scr refresh
            Sam_hu_highlight_pre.setAutoDraw(False)
    answer_to_draw.fillColor=[.3,.5,.7]
    answer_to_draw.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in highlight_sam_hu_pre_choiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "highlight_sam_hu_pre_choice"-------
for thisComponent in highlight_sam_hu_pre_choiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Sam_hu_highlight_pre.started', Sam_hu_highlight_pre.tStartRefresh)
thisExp.addData('Sam_hu_highlight_pre.stopped', Sam_hu_highlight_pre.tStopRefresh)
answer_to_draw.setAutoDraw(False)

# ------Prepare to start Routine "SAM_ec_directions"-------
continueRoutine = True
# update component parameters for each repeat
SAM_ec_instructions_key_resp.keys = []
SAM_ec_instructions_key_resp.rt = []
_SAM_ec_instructions_key_resp_allKeys = []
# keep track of which components have finished
SAM_ec_directionsComponents = [SAM_ec_instructions, SAM_ec_instructions_key_resp]
for thisComponent in SAM_ec_directionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SAM_ec_directionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SAM_ec_directions"-------
while continueRoutine:
    # get current time
    t = SAM_ec_directionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SAM_ec_directionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SAM_ec_instructions* updates
    if SAM_ec_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_ec_instructions.frameNStart = frameN  # exact frame index
        SAM_ec_instructions.tStart = t  # local t and not account for scr refresh
        SAM_ec_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_ec_instructions, 'tStartRefresh')  # time at next scr refresh
        SAM_ec_instructions.setAutoDraw(True)
    
    # *SAM_ec_instructions_key_resp* updates
    waitOnFlip = False
    if SAM_ec_instructions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_ec_instructions_key_resp.frameNStart = frameN  # exact frame index
        SAM_ec_instructions_key_resp.tStart = t  # local t and not account for scr refresh
        SAM_ec_instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_ec_instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
        SAM_ec_instructions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SAM_ec_instructions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SAM_ec_instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SAM_ec_instructions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = SAM_ec_instructions_key_resp.getKeys(keyList=None, waitRelease=False)
        _SAM_ec_instructions_key_resp_allKeys.extend(theseKeys)
        if len(_SAM_ec_instructions_key_resp_allKeys):
            SAM_ec_instructions_key_resp.keys = _SAM_ec_instructions_key_resp_allKeys[-1].name  # just the last key pressed
            SAM_ec_instructions_key_resp.rt = _SAM_ec_instructions_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SAM_ec_directionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SAM_ec_directions"-------
for thisComponent in SAM_ec_directionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SAM_ec_instructions.started', SAM_ec_instructions.tStartRefresh)
thisExp.addData('SAM_ec_instructions.stopped', SAM_ec_instructions.tStopRefresh)
# check responses
if SAM_ec_instructions_key_resp.keys in ['', [], None]:  # No response was made
    SAM_ec_instructions_key_resp.keys = None
thisExp.addData('SAM_ec_instructions_key_resp.keys',SAM_ec_instructions_key_resp.keys)
if SAM_ec_instructions_key_resp.keys != None:  # we had a response
    thisExp.addData('SAM_ec_instructions_key_resp.rt', SAM_ec_instructions_key_resp.rt)
thisExp.addData('SAM_ec_instructions_key_resp.started', SAM_ec_instructions_key_resp.tStartRefresh)
thisExp.addData('SAM_ec_instructions_key_resp.stopped', SAM_ec_instructions_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "SAM_ec_directions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SAM_ec_question"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the select_answer_mouse_sam_ec
select_answer_mouse_sam_ec.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
SAM_ec_questionComponents = [SAM_ec, choice_num_1, choice_num_2, choice_num_3, choice_num_4, choice_num_5, choice_num_6, choice_num_7, choice_num_8, choice_num_9, select_answer_mouse_sam_ec]
for thisComponent in SAM_ec_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SAM_ec_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SAM_ec_question"-------
while continueRoutine:
    # get current time
    t = SAM_ec_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SAM_ec_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SAM_ec* updates
    if SAM_ec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_ec.frameNStart = frameN  # exact frame index
        SAM_ec.tStart = t  # local t and not account for scr refresh
        SAM_ec.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_ec, 'tStartRefresh')  # time at next scr refresh
        SAM_ec.setAutoDraw(True)
    
    # *choice_num_1* updates
    if choice_num_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_1.frameNStart = frameN  # exact frame index
        choice_num_1.tStart = t  # local t and not account for scr refresh
        choice_num_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_1, 'tStartRefresh')  # time at next scr refresh
        choice_num_1.setAutoDraw(True)
    
    # *choice_num_2* updates
    if choice_num_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_2.frameNStart = frameN  # exact frame index
        choice_num_2.tStart = t  # local t and not account for scr refresh
        choice_num_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_2, 'tStartRefresh')  # time at next scr refresh
        choice_num_2.setAutoDraw(True)
    
    # *choice_num_3* updates
    if choice_num_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_3.frameNStart = frameN  # exact frame index
        choice_num_3.tStart = t  # local t and not account for scr refresh
        choice_num_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_3, 'tStartRefresh')  # time at next scr refresh
        choice_num_3.setAutoDraw(True)
    
    # *choice_num_4* updates
    if choice_num_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_4.frameNStart = frameN  # exact frame index
        choice_num_4.tStart = t  # local t and not account for scr refresh
        choice_num_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_4, 'tStartRefresh')  # time at next scr refresh
        choice_num_4.setAutoDraw(True)
    
    # *choice_num_5* updates
    if choice_num_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_5.frameNStart = frameN  # exact frame index
        choice_num_5.tStart = t  # local t and not account for scr refresh
        choice_num_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_5, 'tStartRefresh')  # time at next scr refresh
        choice_num_5.setAutoDraw(True)
    
    # *choice_num_6* updates
    if choice_num_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_6.frameNStart = frameN  # exact frame index
        choice_num_6.tStart = t  # local t and not account for scr refresh
        choice_num_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_6, 'tStartRefresh')  # time at next scr refresh
        choice_num_6.setAutoDraw(True)
    
    # *choice_num_7* updates
    if choice_num_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_7.frameNStart = frameN  # exact frame index
        choice_num_7.tStart = t  # local t and not account for scr refresh
        choice_num_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_7, 'tStartRefresh')  # time at next scr refresh
        choice_num_7.setAutoDraw(True)
    
    # *choice_num_8* updates
    if choice_num_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_8.frameNStart = frameN  # exact frame index
        choice_num_8.tStart = t  # local t and not account for scr refresh
        choice_num_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_8, 'tStartRefresh')  # time at next scr refresh
        choice_num_8.setAutoDraw(True)
    
    # *choice_num_9* updates
    if choice_num_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_9.frameNStart = frameN  # exact frame index
        choice_num_9.tStart = t  # local t and not account for scr refresh
        choice_num_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_9, 'tStartRefresh')  # time at next scr refresh
        choice_num_9.setAutoDraw(True)
    # *select_answer_mouse_sam_ec* updates
    if select_answer_mouse_sam_ec.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        select_answer_mouse_sam_ec.frameNStart = frameN  # exact frame index
        select_answer_mouse_sam_ec.tStart = t  # local t and not account for scr refresh
        select_answer_mouse_sam_ec.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(select_answer_mouse_sam_ec, 'tStartRefresh')  # time at next scr refresh
        select_answer_mouse_sam_ec.status = STARTED
        select_answer_mouse_sam_ec.mouseClock.reset()
        prevButtonState = select_answer_mouse_sam_ec.getPressed()  # if button is down already this ISN'T a new click
    if select_answer_mouse_sam_ec.status == STARTED:  # only update if started and not finished!
        buttons = select_answer_mouse_sam_ec.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [choice_num_1,choice_num_2,choice_num_3,choice_num_4,choice_num_5,choice_num_6,choice_num_7,choice_num_8,choice_num_9]:
                    if obj.contains(select_answer_mouse_sam_ec):
                        gotValidClick = True
                        select_answer_mouse_sam_ec.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SAM_ec_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SAM_ec_question"-------
for thisComponent in SAM_ec_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SAM_ec.started', SAM_ec.tStartRefresh)
thisExp.addData('SAM_ec.stopped', SAM_ec.tStopRefresh)
thisExp.addData('choice_num_1.started', choice_num_1.tStartRefresh)
thisExp.addData('choice_num_1.stopped', choice_num_1.tStopRefresh)
thisExp.addData('choice_num_2.started', choice_num_2.tStartRefresh)
thisExp.addData('choice_num_2.stopped', choice_num_2.tStopRefresh)
thisExp.addData('choice_num_3.started', choice_num_3.tStartRefresh)
thisExp.addData('choice_num_3.stopped', choice_num_3.tStopRefresh)
thisExp.addData('choice_num_4.started', choice_num_4.tStartRefresh)
thisExp.addData('choice_num_4.stopped', choice_num_4.tStopRefresh)
thisExp.addData('choice_num_5.started', choice_num_5.tStartRefresh)
thisExp.addData('choice_num_5.stopped', choice_num_5.tStopRefresh)
thisExp.addData('choice_num_6.started', choice_num_6.tStartRefresh)
thisExp.addData('choice_num_6.stopped', choice_num_6.tStopRefresh)
thisExp.addData('choice_num_7.started', choice_num_7.tStartRefresh)
thisExp.addData('choice_num_7.stopped', choice_num_7.tStopRefresh)
thisExp.addData('choice_num_8.started', choice_num_8.tStartRefresh)
thisExp.addData('choice_num_8.stopped', choice_num_8.tStopRefresh)
thisExp.addData('choice_num_9.started', choice_num_9.tStartRefresh)
thisExp.addData('choice_num_9.stopped', choice_num_9.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = select_answer_mouse_sam_ec.getPos()
buttons = select_answer_mouse_sam_ec.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [choice_num_1,choice_num_2,choice_num_3,choice_num_4,choice_num_5,choice_num_6,choice_num_7,choice_num_8,choice_num_9]:
        if obj.contains(select_answer_mouse_sam_ec):
            gotValidClick = True
            select_answer_mouse_sam_ec.clicked_name.append(obj.name)
thisExp.addData('select_answer_mouse_sam_ec.x', x)
thisExp.addData('select_answer_mouse_sam_ec.y', y)
thisExp.addData('select_answer_mouse_sam_ec.leftButton', buttons[0])
thisExp.addData('select_answer_mouse_sam_ec.midButton', buttons[1])
thisExp.addData('select_answer_mouse_sam_ec.rightButton', buttons[2])
if len(select_answer_mouse_sam_ec.clicked_name):
    thisExp.addData('select_answer_mouse_sam_ec.clicked_name', select_answer_mouse_sam_ec.clicked_name[0])
thisExp.addData('select_answer_mouse_sam_ec.started', select_answer_mouse_sam_ec.tStart)
thisExp.addData('select_answer_mouse_sam_ec.stopped', select_answer_mouse_sam_ec.tStop)
thisExp.nextEntry()
answer_to_draw = []
for answer in [choice_num_1,choice_num_2,choice_num_3,choice_num_4,choice_num_5,choice_num_6,choice_num_7,choice_num_8,choice_num_9]:
    if select_answer_mouse_sam_ec.isPressedIn(answer):
        answer_to_draw = answer
# the Routine "SAM_ec_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "highlight_sam_ec_pre_choice"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
highlight_sam_ec_pre_choiceComponents = [sam_ec_pre_highlight]
for thisComponent in highlight_sam_ec_pre_choiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
highlight_sam_ec_pre_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "highlight_sam_ec_pre_choice"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = highlight_sam_ec_pre_choiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=highlight_sam_ec_pre_choiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sam_ec_pre_highlight* updates
    if sam_ec_pre_highlight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sam_ec_pre_highlight.frameNStart = frameN  # exact frame index
        sam_ec_pre_highlight.tStart = t  # local t and not account for scr refresh
        sam_ec_pre_highlight.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sam_ec_pre_highlight, 'tStartRefresh')  # time at next scr refresh
        sam_ec_pre_highlight.setAutoDraw(True)
    if sam_ec_pre_highlight.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sam_ec_pre_highlight.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            sam_ec_pre_highlight.tStop = t  # not accounting for scr refresh
            sam_ec_pre_highlight.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sam_ec_pre_highlight, 'tStopRefresh')  # time at next scr refresh
            sam_ec_pre_highlight.setAutoDraw(False)
    answer_to_draw.fillColor=[.3,.5,.7]
    answer_to_draw.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in highlight_sam_ec_pre_choiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "highlight_sam_ec_pre_choice"-------
for thisComponent in highlight_sam_ec_pre_choiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sam_ec_pre_highlight.started', sam_ec_pre_highlight.tStartRefresh)
thisExp.addData('sam_ec_pre_highlight.stopped', sam_ec_pre_highlight.tStopRefresh)
answer_to_draw.setAutoDraw(False)

# ------Prepare to start Routine "introduce_keyboard_hand_positioning"-------
continueRoutine = True
# update component parameters for each repeat
intro_to_kb.setAutoDraw(True)
draw_kb_key_resp.keys = []
draw_kb_key_resp.rt = []
_draw_kb_key_resp_allKeys = []
# keep track of which components have finished
introduce_keyboard_hand_positioningComponents = [draw_kb_key_resp]
for thisComponent in introduce_keyboard_hand_positioningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduce_keyboard_hand_positioningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduce_keyboard_hand_positioning"-------
while continueRoutine:
    # get current time
    t = introduce_keyboard_hand_positioningClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduce_keyboard_hand_positioningClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *draw_kb_key_resp* updates
    waitOnFlip = False
    if draw_kb_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        draw_kb_key_resp.frameNStart = frameN  # exact frame index
        draw_kb_key_resp.tStart = t  # local t and not account for scr refresh
        draw_kb_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(draw_kb_key_resp, 'tStartRefresh')  # time at next scr refresh
        draw_kb_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(draw_kb_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(draw_kb_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if draw_kb_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = draw_kb_key_resp.getKeys(keyList=None, waitRelease=False)
        _draw_kb_key_resp_allKeys.extend(theseKeys)
        if len(_draw_kb_key_resp_allKeys):
            draw_kb_key_resp.keys = _draw_kb_key_resp_allKeys[-1].name  # just the last key pressed
            draw_kb_key_resp.rt = _draw_kb_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduce_keyboard_hand_positioningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduce_keyboard_hand_positioning"-------
for thisComponent in introduce_keyboard_hand_positioningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
intro_to_kb.setAutoDraw(False)
# check responses
if draw_kb_key_resp.keys in ['', [], None]:  # No response was made
    draw_kb_key_resp.keys = None
thisExp.addData('draw_kb_key_resp.keys',draw_kb_key_resp.keys)
if draw_kb_key_resp.keys != None:  # we had a response
    thisExp.addData('draw_kb_key_resp.rt', draw_kb_key_resp.rt)
thisExp.addData('draw_kb_key_resp.started', draw_kb_key_resp.tStartRefresh)
thisExp.addData('draw_kb_key_resp.stopped', draw_kb_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "introduce_keyboard_hand_positioning" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "begin_instructions"-------
continueRoutine = True
# update component parameters for each repeat
# draw slide based on condition
if instruction_slide_2_selection == 1:
    
    fractal_blossom.pos = [-.12, .13]
    fractal_octopus.pos = [.12, .13]
    
    instructions_slide_two.setAutoDraw(True)
    fractal_blossom.setAutoDraw(True)
    fractal_octopus.setAutoDraw(True)

elif instruction_slide_2_selection == 2:
    
    fractal_blossom.pos = [.12, .13]
    fractal_octopus.pos = [-.12, .13]
    
    instructions_slide_two.setAutoDraw(True)
    fractal_blossom.setAutoDraw(True)
    fractal_octopus.setAutoDraw(True)
begin_task_instructions_key_resp.keys = []
begin_task_instructions_key_resp.rt = []
_begin_task_instructions_key_resp_allKeys = []
# keep track of which components have finished
begin_instructionsComponents = [begin_task_instructions_key_resp]
for thisComponent in begin_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
begin_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "begin_instructions"-------
while continueRoutine:
    # get current time
    t = begin_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=begin_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_task_instructions_key_resp* updates
    waitOnFlip = False
    if begin_task_instructions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_task_instructions_key_resp.frameNStart = frameN  # exact frame index
        begin_task_instructions_key_resp.tStart = t  # local t and not account for scr refresh
        begin_task_instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_task_instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
        begin_task_instructions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_task_instructions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_task_instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_task_instructions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = begin_task_instructions_key_resp.getKeys(keyList=None, waitRelease=False)
        _begin_task_instructions_key_resp_allKeys.extend(theseKeys)
        if len(_begin_task_instructions_key_resp_allKeys):
            begin_task_instructions_key_resp.keys = _begin_task_instructions_key_resp_allKeys[-1].name  # just the last key pressed
            begin_task_instructions_key_resp.rt = _begin_task_instructions_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in begin_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin_instructions"-------
for thisComponent in begin_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# draw slide based on condition
if instruction_slide_2_selection == 1:
    
    fractal_blossom.pos = [-.12, .13]
    fractal_octopus.pos = [.12, .13]
    
    instructions_slide_two.setAutoDraw(False)
    fractal_blossom.setAutoDraw(False)
    fractal_octopus.setAutoDraw(False)

elif instruction_slide_2_selection == 2:
    
    fractal_blossom.pos = [.12, .13]
    fractal_octopus.pos = [-.12, .13]
    
    instructions_slide_two.setAutoDraw(False)
    fractal_blossom.setAutoDraw(False)
    fractal_octopus.setAutoDraw(False)
# check responses
if begin_task_instructions_key_resp.keys in ['', [], None]:  # No response was made
    begin_task_instructions_key_resp.keys = None
thisExp.addData('begin_task_instructions_key_resp.keys',begin_task_instructions_key_resp.keys)
if begin_task_instructions_key_resp.keys != None:  # we had a response
    thisExp.addData('begin_task_instructions_key_resp.rt', begin_task_instructions_key_resp.rt)
thisExp.addData('begin_task_instructions_key_resp.started', begin_task_instructions_key_resp.tStartRefresh)
thisExp.addData('begin_task_instructions_key_resp.stopped', begin_task_instructions_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "begin_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "continue_begin"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_two_second.setAutoDraw(True)
slide_two_key_response.keys = []
slide_two_key_response.rt = []
_slide_two_key_response_allKeys = []
# keep track of which components have finished
continue_beginComponents = [slide_two_key_response]
for thisComponent in continue_beginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_begin"-------
while continueRoutine:
    # get current time
    t = continue_beginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_beginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_two_key_response* updates
    waitOnFlip = False
    if slide_two_key_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_two_key_response.frameNStart = frameN  # exact frame index
        slide_two_key_response.tStart = t  # local t and not account for scr refresh
        slide_two_key_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_two_key_response, 'tStartRefresh')  # time at next scr refresh
        slide_two_key_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_two_key_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_two_key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_two_key_response.status == STARTED and not waitOnFlip:
        theseKeys = slide_two_key_response.getKeys(keyList=None, waitRelease=False)
        _slide_two_key_response_allKeys.extend(theseKeys)
        if len(_slide_two_key_response_allKeys):
            slide_two_key_response.keys = _slide_two_key_response_allKeys[-1].name  # just the last key pressed
            slide_two_key_response.rt = _slide_two_key_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_begin"-------
for thisComponent in continue_beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_two_second.setAutoDraw(False)
# check responses
if slide_two_key_response.keys in ['', [], None]:  # No response was made
    slide_two_key_response.keys = None
thisExp.addData('slide_two_key_response.keys',slide_two_key_response.keys)
if slide_two_key_response.keys != None:  # we had a response
    thisExp.addData('slide_two_key_response.rt', slide_two_key_response.rt)
thisExp.addData('slide_two_key_response.started', slide_two_key_response.tStartRefresh)
thisExp.addData('slide_two_key_response.stopped', slide_two_key_response.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "slide_max_points"-------
continueRoutine = True
# update component parameters for each repeat
max_points.setAutoDraw(True)
max_points_slide_key_resp.keys = []
max_points_slide_key_resp.rt = []
_max_points_slide_key_resp_allKeys = []
# keep track of which components have finished
slide_max_pointsComponents = [max_points_slide_key_resp]
for thisComponent in slide_max_pointsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
slide_max_pointsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "slide_max_points"-------
while continueRoutine:
    # get current time
    t = slide_max_pointsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=slide_max_pointsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *max_points_slide_key_resp* updates
    waitOnFlip = False
    if max_points_slide_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        max_points_slide_key_resp.frameNStart = frameN  # exact frame index
        max_points_slide_key_resp.tStart = t  # local t and not account for scr refresh
        max_points_slide_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(max_points_slide_key_resp, 'tStartRefresh')  # time at next scr refresh
        max_points_slide_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(max_points_slide_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(max_points_slide_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if max_points_slide_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = max_points_slide_key_resp.getKeys(keyList=None, waitRelease=False)
        _max_points_slide_key_resp_allKeys.extend(theseKeys)
        if len(_max_points_slide_key_resp_allKeys):
            max_points_slide_key_resp.keys = _max_points_slide_key_resp_allKeys[-1].name  # just the last key pressed
            max_points_slide_key_resp.rt = _max_points_slide_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in slide_max_pointsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "slide_max_points"-------
for thisComponent in slide_max_pointsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
max_points.setAutoDraw(False)
# check responses
if max_points_slide_key_resp.keys in ['', [], None]:  # No response was made
    max_points_slide_key_resp.keys = None
thisExp.addData('max_points_slide_key_resp.keys',max_points_slide_key_resp.keys)
if max_points_slide_key_resp.keys != None:  # we had a response
    thisExp.addData('max_points_slide_key_resp.rt', max_points_slide_key_resp.rt)
thisExp.addData('max_points_slide_key_resp.started', max_points_slide_key_resp.tStartRefresh)
thisExp.addData('max_points_slide_key_resp.stopped', max_points_slide_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "slide_max_points" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fractal_selection_quiz"-------
continueRoutine = True
# update component parameters for each repeat
select_key_to_press_slide.setAutoDraw(True)




fractal_selection_quiz_key_resp.keys = []
fractal_selection_quiz_key_resp.rt = []
_fractal_selection_quiz_key_resp_allKeys = []
# keep track of which components have finished
fractal_selection_quizComponents = [fractal_selection_quiz_key_resp]
for thisComponent in fractal_selection_quizComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fractal_selection_quizClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fractal_selection_quiz"-------
while continueRoutine:
    # get current time
    t = fractal_selection_quizClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fractal_selection_quizClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fractal_selection_quiz_key_resp* updates
    waitOnFlip = False
    if fractal_selection_quiz_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fractal_selection_quiz_key_resp.frameNStart = frameN  # exact frame index
        fractal_selection_quiz_key_resp.tStart = t  # local t and not account for scr refresh
        fractal_selection_quiz_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fractal_selection_quiz_key_resp, 'tStartRefresh')  # time at next scr refresh
        fractal_selection_quiz_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fractal_selection_quiz_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fractal_selection_quiz_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fractal_selection_quiz_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = fractal_selection_quiz_key_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
        _fractal_selection_quiz_key_resp_allKeys.extend(theseKeys)
        if len(_fractal_selection_quiz_key_resp_allKeys):
            fractal_selection_quiz_key_resp.keys = _fractal_selection_quiz_key_resp_allKeys[-1].name  # just the last key pressed
            fractal_selection_quiz_key_resp.rt = _fractal_selection_quiz_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fractal_selection_quizComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fractal_selection_quiz"-------
for thisComponent in fractal_selection_quizComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# get response
if fractal_selection_quiz_key_resp.keys == 'f' and select_key_to_press == 1:   # correct
    key_to_press_outcome = 'correct'
    quiz_and_attention_check_fails = quiz_and_attention_check_fails

elif fractal_selection_quiz_key_resp.keys == 'j' and select_key_to_press == 1: # incorrect
    key_to_press_outcome = 'incorrect'
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1

elif fractal_selection_quiz_key_resp.keys == 'f' and select_key_to_press == 2: # incorrect
    key_to_press_outcome = 'incorrect'
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1

elif fractal_selection_quiz_key_resp.keys == 'j' and select_key_to_press == 2:  # correct
    key_to_press_outcome = 'correct'
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    
select_key_to_press_slide.setAutoDraw(False)
# check responses
if fractal_selection_quiz_key_resp.keys in ['', [], None]:  # No response was made
    fractal_selection_quiz_key_resp.keys = None
thisExp.addData('fractal_selection_quiz_key_resp.keys',fractal_selection_quiz_key_resp.keys)
if fractal_selection_quiz_key_resp.keys != None:  # we had a response
    thisExp.addData('fractal_selection_quiz_key_resp.rt', fractal_selection_quiz_key_resp.rt)
thisExp.addData('fractal_selection_quiz_key_resp.started', fractal_selection_quiz_key_resp.tStartRefresh)
thisExp.addData('fractal_selection_quiz_key_resp.stopped', fractal_selection_quiz_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "fractal_selection_quiz" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fractal_reminder_show"-------
continueRoutine = True
# update component parameters for each repeat
# draw reminder
if key_to_press_outcome == 'correct':
    correct_fractal_reminder.setAutoDraw(True)
elif key_to_press_outcome == 'incorrect':
    incorrect_fractal_reminder.setAutoDraw(True)
fractal_reminder_show_key_resp.keys = []
fractal_reminder_show_key_resp.rt = []
_fractal_reminder_show_key_resp_allKeys = []
# keep track of which components have finished
fractal_reminder_showComponents = [fractal_reminder_show_key_resp]
for thisComponent in fractal_reminder_showComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fractal_reminder_showClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fractal_reminder_show"-------
while continueRoutine:
    # get current time
    t = fractal_reminder_showClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fractal_reminder_showClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fractal_reminder_show_key_resp* updates
    waitOnFlip = False
    if fractal_reminder_show_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fractal_reminder_show_key_resp.frameNStart = frameN  # exact frame index
        fractal_reminder_show_key_resp.tStart = t  # local t and not account for scr refresh
        fractal_reminder_show_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fractal_reminder_show_key_resp, 'tStartRefresh')  # time at next scr refresh
        fractal_reminder_show_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fractal_reminder_show_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fractal_reminder_show_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fractal_reminder_show_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = fractal_reminder_show_key_resp.getKeys(keyList=None, waitRelease=False)
        _fractal_reminder_show_key_resp_allKeys.extend(theseKeys)
        if len(_fractal_reminder_show_key_resp_allKeys):
            fractal_reminder_show_key_resp.keys = _fractal_reminder_show_key_resp_allKeys[-1].name  # just the last key pressed
            fractal_reminder_show_key_resp.rt = _fractal_reminder_show_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fractal_reminder_showComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fractal_reminder_show"-------
for thisComponent in fractal_reminder_showComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# draw reminder
if key_to_press_outcome == 'correct':
    correct_fractal_reminder.setAutoDraw(False)
elif key_to_press_outcome == 'incorrect':
    incorrect_fractal_reminder.setAutoDraw(False)
    
# add quiz data
psychoJS.experiment.addData('key_to_press_outcome', key_to_press_outcome)

# check responses
if fractal_reminder_show_key_resp.keys in ['', [], None]:  # No response was made
    fractal_reminder_show_key_resp.keys = None
thisExp.addData('fractal_reminder_show_key_resp.keys',fractal_reminder_show_key_resp.keys)
if fractal_reminder_show_key_resp.keys != None:  # we had a response
    thisExp.addData('fractal_reminder_show_key_resp.rt', fractal_reminder_show_key_resp.rt)
thisExp.addData('fractal_reminder_show_key_resp.started', fractal_reminder_show_key_resp.tStartRefresh)
thisExp.addData('fractal_reminder_show_key_resp.stopped', fractal_reminder_show_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "fractal_reminder_show" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "draw_slide_3"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_three.setAutoDraw(True)

slide_3_key_resp.keys = []
slide_3_key_resp.rt = []
_slide_3_key_resp_allKeys = []
# keep track of which components have finished
draw_slide_3Components = [slide_3_key_resp]
for thisComponent in draw_slide_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
draw_slide_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "draw_slide_3"-------
while continueRoutine:
    # get current time
    t = draw_slide_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=draw_slide_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_3_key_resp* updates
    waitOnFlip = False
    if slide_3_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_3_key_resp.frameNStart = frameN  # exact frame index
        slide_3_key_resp.tStart = t  # local t and not account for scr refresh
        slide_3_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_3_key_resp, 'tStartRefresh')  # time at next scr refresh
        slide_3_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_3_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_3_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_3_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = slide_3_key_resp.getKeys(keyList=None, waitRelease=False)
        _slide_3_key_resp_allKeys.extend(theseKeys)
        if len(_slide_3_key_resp_allKeys):
            slide_3_key_resp.keys = _slide_3_key_resp_allKeys[-1].name  # just the last key pressed
            slide_3_key_resp.rt = _slide_3_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in draw_slide_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "draw_slide_3"-------
for thisComponent in draw_slide_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_three.setAutoDraw(False)
# check responses
if slide_3_key_resp.keys in ['', [], None]:  # No response was made
    slide_3_key_resp.keys = None
thisExp.addData('slide_3_key_resp.keys',slide_3_key_resp.keys)
if slide_3_key_resp.keys != None:  # we had a response
    thisExp.addData('slide_3_key_resp.rt', slide_3_key_resp.rt)
thisExp.addData('slide_3_key_resp.started', slide_3_key_resp.tStartRefresh)
thisExp.addData('slide_3_key_resp.stopped', slide_3_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "draw_slide_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "display_feedback_meanings"-------
continueRoutine = True
# update component parameters for each repeat
# display pairings between feedback stim and outcome meanings

# in condition 1, the vertical stim means reward

if condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.pos = [-.17, 0.12]
    grey_no_feedback_stim.pos = [.17, 0.12]
    
    horizontal_feedback_stim.size = (0.10, 0.12)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    instructions_slide_four.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True)

# in condition 2, the horizontal stim means reward

elif condition == 2:
    
    horizontal_feedback_stim.pos = [-.17, 0.12]
    vertical_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.pos = [.17, 0.12]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    instructions_slide_four.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True)

display_feedback_meanings_key_resp.keys = []
display_feedback_meanings_key_resp.rt = []
_display_feedback_meanings_key_resp_allKeys = []
# keep track of which components have finished
display_feedback_meaningsComponents = [display_feedback_meanings_key_resp]
for thisComponent in display_feedback_meaningsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
display_feedback_meaningsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "display_feedback_meanings"-------
while continueRoutine:
    # get current time
    t = display_feedback_meaningsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=display_feedback_meaningsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *display_feedback_meanings_key_resp* updates
    waitOnFlip = False
    if display_feedback_meanings_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        display_feedback_meanings_key_resp.frameNStart = frameN  # exact frame index
        display_feedback_meanings_key_resp.tStart = t  # local t and not account for scr refresh
        display_feedback_meanings_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(display_feedback_meanings_key_resp, 'tStartRefresh')  # time at next scr refresh
        display_feedback_meanings_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(display_feedback_meanings_key_resp.clock.reset)  # t=0 on next screen flip
    if display_feedback_meanings_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = display_feedback_meanings_key_resp.getKeys(keyList=None, waitRelease=False)
        _display_feedback_meanings_key_resp_allKeys.extend(theseKeys)
        if len(_display_feedback_meanings_key_resp_allKeys):
            display_feedback_meanings_key_resp.keys = _display_feedback_meanings_key_resp_allKeys[-1].name  # just the last key pressed
            display_feedback_meanings_key_resp.rt = _display_feedback_meanings_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in display_feedback_meaningsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "display_feedback_meanings"-------
for thisComponent in display_feedback_meaningsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# display pairings between feedback stim and outcome meanings

# in condition 1, the vertical stim means reward

if condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.pos = [-.17, 0.12]
    grey_no_feedback_stim.pos = [.17, 0.12]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    instructions_slide_four.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False)

# in condition 2, the horizontal stim means reward

elif condition == 2:
    
    horizontal_feedback_stim.pos = [-.17, 0.12]
    vertical_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.pos = [.17, 0.12]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    instructions_slide_four.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False)
# check responses
if display_feedback_meanings_key_resp.keys in ['', [], None]:  # No response was made
    display_feedback_meanings_key_resp.keys = None
thisExp.addData('display_feedback_meanings_key_resp.keys',display_feedback_meanings_key_resp.keys)
if display_feedback_meanings_key_resp.keys != None:  # we had a response
    thisExp.addData('display_feedback_meanings_key_resp.rt', display_feedback_meanings_key_resp.rt)
thisExp.addData('display_feedback_meanings_key_resp.started', display_feedback_meanings_key_resp.tStartRefresh)
thisExp.addData('display_feedback_meanings_key_resp.stopped', display_feedback_meanings_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "display_feedback_meanings" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "first_quiz_first_question"-------
continueRoutine = True
# update component parameters for each repeat
# draw first part of quiz
horizontal_feedback_stim.pos = [0, 0.12]
horizontal_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(True)
horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim

first_quiz_first_question_key_resp.keys = []
first_quiz_first_question_key_resp.rt = []
_first_quiz_first_question_key_resp_allKeys = []
# keep track of which components have finished
first_quiz_first_questionComponents = [first_quiz_first_question_key_resp]
for thisComponent in first_quiz_first_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
first_quiz_first_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "first_quiz_first_question"-------
while continueRoutine:
    # get current time
    t = first_quiz_first_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=first_quiz_first_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *first_quiz_first_question_key_resp* updates
    waitOnFlip = False
    if first_quiz_first_question_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        first_quiz_first_question_key_resp.frameNStart = frameN  # exact frame index
        first_quiz_first_question_key_resp.tStart = t  # local t and not account for scr refresh
        first_quiz_first_question_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(first_quiz_first_question_key_resp, 'tStartRefresh')  # time at next scr refresh
        first_quiz_first_question_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(first_quiz_first_question_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(first_quiz_first_question_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if first_quiz_first_question_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = first_quiz_first_question_key_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _first_quiz_first_question_key_resp_allKeys.extend(theseKeys)
        if len(_first_quiz_first_question_key_resp_allKeys):
            first_quiz_first_question_key_resp.keys = _first_quiz_first_question_key_resp_allKeys[-1].name  # just the last key pressed
            first_quiz_first_question_key_resp.rt = _first_quiz_first_question_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in first_quiz_first_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "first_quiz_first_question"-------
for thisComponent in first_quiz_first_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if first_quiz_first_question_key_resp.keys == '1' and condition == 1:   # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_first_question_result = 'incorrect'
        
elif first_quiz_first_question_key_resp.keys == '2' and condition == 1: # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    first_stim_quiz_first_question_result = 'correct'
        
elif first_quiz_first_question_key_resp.keys == '3' and condition == 1: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_first_question_result = 'incorrect'
    
elif first_quiz_first_question_key_resp.keys == '1' and condition == 2: # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    first_stim_quiz_first_question_result = 'correct'
        
elif first_quiz_first_question_key_resp.keys == '2' and condition == 2: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_first_question_result = 'incorrect'
        
elif first_quiz_first_question_key_resp.keys == '3' and condition == 2: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_first_question_result = 'incorrect'

# draw first part of quiz
horizontal_feedback_stim.pos = [0, 0.12]
horizontal_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(False)
horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim
# check responses
if first_quiz_first_question_key_resp.keys in ['', [], None]:  # No response was made
    first_quiz_first_question_key_resp.keys = None
thisExp.addData('first_quiz_first_question_key_resp.keys',first_quiz_first_question_key_resp.keys)
if first_quiz_first_question_key_resp.keys != None:  # we had a response
    thisExp.addData('first_quiz_first_question_key_resp.rt', first_quiz_first_question_key_resp.rt)
thisExp.addData('first_quiz_first_question_key_resp.started', first_quiz_first_question_key_resp.tStartRefresh)
thisExp.addData('first_quiz_first_question_key_resp.stopped', first_quiz_first_question_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "first_quiz_first_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "first_quiz_first_question_reminder"-------
continueRoutine = True
# update component parameters for each repeat
# draw reminder
if first_stim_quiz_first_question_result == 'correct' and condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_zero.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim

elif first_stim_quiz_first_question_result == 'incorrect' and condition == 1:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_zero.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim

elif first_stim_quiz_first_question_result == 'correct' and condition == 2:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_one.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim

elif first_stim_quiz_first_question_result == 'incorrect' and condition == 2:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_one.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim
first_quiz_first_q_reminder_key_resp.keys = []
first_quiz_first_q_reminder_key_resp.rt = []
_first_quiz_first_q_reminder_key_resp_allKeys = []
# keep track of which components have finished
first_quiz_first_question_reminderComponents = [first_quiz_first_q_reminder_key_resp]
for thisComponent in first_quiz_first_question_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
first_quiz_first_question_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "first_quiz_first_question_reminder"-------
while continueRoutine:
    # get current time
    t = first_quiz_first_question_reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=first_quiz_first_question_reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *first_quiz_first_q_reminder_key_resp* updates
    waitOnFlip = False
    if first_quiz_first_q_reminder_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        first_quiz_first_q_reminder_key_resp.frameNStart = frameN  # exact frame index
        first_quiz_first_q_reminder_key_resp.tStart = t  # local t and not account for scr refresh
        first_quiz_first_q_reminder_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(first_quiz_first_q_reminder_key_resp, 'tStartRefresh')  # time at next scr refresh
        first_quiz_first_q_reminder_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(first_quiz_first_q_reminder_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(first_quiz_first_q_reminder_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if first_quiz_first_q_reminder_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = first_quiz_first_q_reminder_key_resp.getKeys(keyList=None, waitRelease=False)
        _first_quiz_first_q_reminder_key_resp_allKeys.extend(theseKeys)
        if len(_first_quiz_first_q_reminder_key_resp_allKeys):
            first_quiz_first_q_reminder_key_resp.keys = _first_quiz_first_q_reminder_key_resp_allKeys[-1].name  # just the last key pressed
            first_quiz_first_q_reminder_key_resp.rt = _first_quiz_first_q_reminder_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in first_quiz_first_question_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "first_quiz_first_question_reminder"-------
for thisComponent in first_quiz_first_question_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# draw reminder
if first_stim_quiz_first_question_result == 'correct' and condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_zero.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim

elif first_stim_quiz_first_question_result == 'incorrect' and condition == 1:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_zero.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim

elif first_stim_quiz_first_question_result == 'correct' and condition == 2:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_one.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim

elif first_stim_quiz_first_question_result == 'incorrect' and condition == 2:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_one.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim
# check responses
if first_quiz_first_q_reminder_key_resp.keys in ['', [], None]:  # No response was made
    first_quiz_first_q_reminder_key_resp.keys = None
thisExp.addData('first_quiz_first_q_reminder_key_resp.keys',first_quiz_first_q_reminder_key_resp.keys)
if first_quiz_first_q_reminder_key_resp.keys != None:  # we had a response
    thisExp.addData('first_quiz_first_q_reminder_key_resp.rt', first_quiz_first_q_reminder_key_resp.rt)
thisExp.addData('first_quiz_first_q_reminder_key_resp.started', first_quiz_first_q_reminder_key_resp.tStartRefresh)
thisExp.addData('first_quiz_first_q_reminder_key_resp.stopped', first_quiz_first_q_reminder_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "first_quiz_first_question_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "first_quiz_second_question"-------
continueRoutine = True
# update component parameters for each repeat
# draw second part of quiz
grey_no_feedback_stim.pos = [0, 0.12]
grey_no_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(True)
grey_no_feedback_stim.setAutoDraw(True) # draw grey stim
first_quiz_second_question_key_resp.keys = []
first_quiz_second_question_key_resp.rt = []
_first_quiz_second_question_key_resp_allKeys = []
# keep track of which components have finished
first_quiz_second_questionComponents = [first_quiz_second_question_key_resp]
for thisComponent in first_quiz_second_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
first_quiz_second_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "first_quiz_second_question"-------
while continueRoutine:
    # get current time
    t = first_quiz_second_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=first_quiz_second_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *first_quiz_second_question_key_resp* updates
    waitOnFlip = False
    if first_quiz_second_question_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        first_quiz_second_question_key_resp.frameNStart = frameN  # exact frame index
        first_quiz_second_question_key_resp.tStart = t  # local t and not account for scr refresh
        first_quiz_second_question_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(first_quiz_second_question_key_resp, 'tStartRefresh')  # time at next scr refresh
        first_quiz_second_question_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(first_quiz_second_question_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(first_quiz_second_question_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if first_quiz_second_question_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = first_quiz_second_question_key_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _first_quiz_second_question_key_resp_allKeys.extend(theseKeys)
        if len(_first_quiz_second_question_key_resp_allKeys):
            first_quiz_second_question_key_resp.keys = _first_quiz_second_question_key_resp_allKeys[-1].name  # just the last key pressed
            first_quiz_second_question_key_resp.rt = _first_quiz_second_question_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in first_quiz_second_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "first_quiz_second_question"-------
for thisComponent in first_quiz_second_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if first_quiz_second_question_key_resp.keys == '1':   # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_second_question_result = 'incorrect'
        
elif first_quiz_second_question_key_resp.keys == '2': # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_second_question_result = 'incorrect'
        
elif first_quiz_second_question_key_resp.keys == '3': # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    first_stim_quiz_second_question_result = 'correct'

# draw second part of quiz
grey_no_feedback_stim.pos = [0, 0.12]
grey_no_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(False)
grey_no_feedback_stim.setAutoDraw(False) # draw grey stim
# check responses
if first_quiz_second_question_key_resp.keys in ['', [], None]:  # No response was made
    first_quiz_second_question_key_resp.keys = None
thisExp.addData('first_quiz_second_question_key_resp.keys',first_quiz_second_question_key_resp.keys)
if first_quiz_second_question_key_resp.keys != None:  # we had a response
    thisExp.addData('first_quiz_second_question_key_resp.rt', first_quiz_second_question_key_resp.rt)
thisExp.addData('first_quiz_second_question_key_resp.started', first_quiz_second_question_key_resp.tStartRefresh)
thisExp.addData('first_quiz_second_question_key_resp.stopped', first_quiz_second_question_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "first_quiz_second_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "first_quiz_second_question_reminder"-------
continueRoutine = True
# update component parameters for each repeat
# draw reminder
if first_stim_quiz_second_question_result == 'correct':
    
    grey_no_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.size = (0.10, 0.10)

    correct_result_no_feedback.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True) # draw grey stim
    
elif first_stim_quiz_second_question_result == 'incorrect':

    grey_no_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.size = (0.10, 0.10)

    incorrect_result_no_feedback.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True) # draw grey stim
first_quiz_second_question_reminder_key_resp.keys = []
first_quiz_second_question_reminder_key_resp.rt = []
_first_quiz_second_question_reminder_key_resp_allKeys = []
# keep track of which components have finished
first_quiz_second_question_reminderComponents = [first_quiz_second_question_reminder_key_resp]
for thisComponent in first_quiz_second_question_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
first_quiz_second_question_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "first_quiz_second_question_reminder"-------
while continueRoutine:
    # get current time
    t = first_quiz_second_question_reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=first_quiz_second_question_reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *first_quiz_second_question_reminder_key_resp* updates
    waitOnFlip = False
    if first_quiz_second_question_reminder_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        first_quiz_second_question_reminder_key_resp.frameNStart = frameN  # exact frame index
        first_quiz_second_question_reminder_key_resp.tStart = t  # local t and not account for scr refresh
        first_quiz_second_question_reminder_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(first_quiz_second_question_reminder_key_resp, 'tStartRefresh')  # time at next scr refresh
        first_quiz_second_question_reminder_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(first_quiz_second_question_reminder_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(first_quiz_second_question_reminder_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if first_quiz_second_question_reminder_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = first_quiz_second_question_reminder_key_resp.getKeys(keyList=None, waitRelease=False)
        _first_quiz_second_question_reminder_key_resp_allKeys.extend(theseKeys)
        if len(_first_quiz_second_question_reminder_key_resp_allKeys):
            first_quiz_second_question_reminder_key_resp.keys = _first_quiz_second_question_reminder_key_resp_allKeys[-1].name  # just the last key pressed
            first_quiz_second_question_reminder_key_resp.rt = _first_quiz_second_question_reminder_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in first_quiz_second_question_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "first_quiz_second_question_reminder"-------
for thisComponent in first_quiz_second_question_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# draw reminder
if first_stim_quiz_second_question_result == 'correct':
    
    grey_no_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.size = (0.10, 0.10)

    correct_result_no_feedback.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False) # draw grey stim
    
elif first_stim_quiz_second_question_result == 'incorrect':

    grey_no_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.size = (0.10, 0.10)

    incorrect_result_no_feedback.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False) # draw grey stim
# check responses
if first_quiz_second_question_reminder_key_resp.keys in ['', [], None]:  # No response was made
    first_quiz_second_question_reminder_key_resp.keys = None
thisExp.addData('first_quiz_second_question_reminder_key_resp.keys',first_quiz_second_question_reminder_key_resp.keys)
if first_quiz_second_question_reminder_key_resp.keys != None:  # we had a response
    thisExp.addData('first_quiz_second_question_reminder_key_resp.rt', first_quiz_second_question_reminder_key_resp.rt)
thisExp.addData('first_quiz_second_question_reminder_key_resp.started', first_quiz_second_question_reminder_key_resp.tStartRefresh)
thisExp.addData('first_quiz_second_question_reminder_key_resp.stopped', first_quiz_second_question_reminder_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "first_quiz_second_question_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "first_quiz_third_question"-------
continueRoutine = True
# update component parameters for each repeat
last_q_first_quiz_key_resp.keys = []
last_q_first_quiz_key_resp.rt = []
_last_q_first_quiz_key_resp_allKeys = []
# draw third part of quiz
vertical_feedback_stim.pos = [0, 0.12]
vertical_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(True)
vertical_feedback_stim.setAutoDraw(True) # draw vertical stim
# keep track of which components have finished
first_quiz_third_questionComponents = [last_q_first_quiz_key_resp]
for thisComponent in first_quiz_third_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
first_quiz_third_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "first_quiz_third_question"-------
while continueRoutine:
    # get current time
    t = first_quiz_third_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=first_quiz_third_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *last_q_first_quiz_key_resp* updates
    waitOnFlip = False
    if last_q_first_quiz_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        last_q_first_quiz_key_resp.frameNStart = frameN  # exact frame index
        last_q_first_quiz_key_resp.tStart = t  # local t and not account for scr refresh
        last_q_first_quiz_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(last_q_first_quiz_key_resp, 'tStartRefresh')  # time at next scr refresh
        last_q_first_quiz_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(last_q_first_quiz_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(last_q_first_quiz_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if last_q_first_quiz_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = last_q_first_quiz_key_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _last_q_first_quiz_key_resp_allKeys.extend(theseKeys)
        if len(_last_q_first_quiz_key_resp_allKeys):
            last_q_first_quiz_key_resp.keys = _last_q_first_quiz_key_resp_allKeys[-1].name  # just the last key pressed
            last_q_first_quiz_key_resp.rt = _last_q_first_quiz_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in first_quiz_third_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "first_quiz_third_question"-------
for thisComponent in first_quiz_third_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if last_q_first_quiz_key_resp.keys in ['', [], None]:  # No response was made
    last_q_first_quiz_key_resp.keys = None
thisExp.addData('last_q_first_quiz_key_resp.keys',last_q_first_quiz_key_resp.keys)
if last_q_first_quiz_key_resp.keys != None:  # we had a response
    thisExp.addData('last_q_first_quiz_key_resp.rt', last_q_first_quiz_key_resp.rt)
thisExp.addData('last_q_first_quiz_key_resp.started', last_q_first_quiz_key_resp.tStartRefresh)
thisExp.addData('last_q_first_quiz_key_resp.stopped', last_q_first_quiz_key_resp.tStopRefresh)
thisExp.nextEntry()
if last_q_first_quiz_key_resp.keys == '1' and condition == 1:   # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    first_stim_quiz_third_question_result = 'correct'
        
elif last_q_first_quiz_key_resp.keys == '2' and condition == 1: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_third_question_result = 'incorrect'
        
elif last_q_first_quiz_key_resp.keys == '3' and condition == 1: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_third_question_result = 'incorrect'
    
elif last_q_first_quiz_key_resp.keys == '1' and condition == 2: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_third_question_result = 'incorrect'
        
elif last_q_first_quiz_key_resp.keys == '2' and condition == 2: # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    first_stim_quiz_third_question_result = 'correct'
        
elif last_q_first_quiz_key_resp.keys == '3' and condition == 2: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    first_stim_quiz_third_question_result = 'incorrect'

# draw third part of quiz
vertical_feedback_stim.pos = [0, 0.12]
vertical_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(False)
vertical_feedback_stim.setAutoDraw(False) # draw vertical stim
# the Routine "first_quiz_third_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "first_quiz_third_question_reminder"-------
continueRoutine = True
# update component parameters for each repeat
first_quiz_third_question_reminder_key_resp.keys = []
first_quiz_third_question_reminder_key_resp.rt = []
_first_quiz_third_question_reminder_key_resp_allKeys = []
# draw reminder
if first_stim_quiz_third_question_result == 'correct' and condition == 1:
    
    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_one.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True) # draw vertical stim

elif first_stim_quiz_third_question_result == 'incorrect' and condition == 1:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)
    
    incorrect_result_plus_one.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True) # draw vertical stim

elif first_stim_quiz_third_question_result == 'correct' and condition == 2:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_zero.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True) # draw vertical stim

elif first_stim_quiz_third_question_result == 'incorrect' and condition == 2:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_zero.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True) # draw vertical stim
# keep track of which components have finished
first_quiz_third_question_reminderComponents = [first_quiz_third_question_reminder_key_resp]
for thisComponent in first_quiz_third_question_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
first_quiz_third_question_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "first_quiz_third_question_reminder"-------
while continueRoutine:
    # get current time
    t = first_quiz_third_question_reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=first_quiz_third_question_reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *first_quiz_third_question_reminder_key_resp* updates
    waitOnFlip = False
    if first_quiz_third_question_reminder_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        first_quiz_third_question_reminder_key_resp.frameNStart = frameN  # exact frame index
        first_quiz_third_question_reminder_key_resp.tStart = t  # local t and not account for scr refresh
        first_quiz_third_question_reminder_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(first_quiz_third_question_reminder_key_resp, 'tStartRefresh')  # time at next scr refresh
        first_quiz_third_question_reminder_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(first_quiz_third_question_reminder_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(first_quiz_third_question_reminder_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if first_quiz_third_question_reminder_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = first_quiz_third_question_reminder_key_resp.getKeys(keyList=None, waitRelease=False)
        _first_quiz_third_question_reminder_key_resp_allKeys.extend(theseKeys)
        if len(_first_quiz_third_question_reminder_key_resp_allKeys):
            first_quiz_third_question_reminder_key_resp.keys = _first_quiz_third_question_reminder_key_resp_allKeys[-1].name  # just the last key pressed
            first_quiz_third_question_reminder_key_resp.rt = _first_quiz_third_question_reminder_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in first_quiz_third_question_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "first_quiz_third_question_reminder"-------
for thisComponent in first_quiz_third_question_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if first_quiz_third_question_reminder_key_resp.keys in ['', [], None]:  # No response was made
    first_quiz_third_question_reminder_key_resp.keys = None
thisExp.addData('first_quiz_third_question_reminder_key_resp.keys',first_quiz_third_question_reminder_key_resp.keys)
if first_quiz_third_question_reminder_key_resp.keys != None:  # we had a response
    thisExp.addData('first_quiz_third_question_reminder_key_resp.rt', first_quiz_third_question_reminder_key_resp.rt)
thisExp.addData('first_quiz_third_question_reminder_key_resp.started', first_quiz_third_question_reminder_key_resp.tStartRefresh)
thisExp.addData('first_quiz_third_question_reminder_key_resp.stopped', first_quiz_third_question_reminder_key_resp.tStopRefresh)
thisExp.nextEntry()
# draw reminder
if first_stim_quiz_third_question_result == 'correct' and condition == 1:
    
    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_one.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False) # draw vertical stim

elif first_stim_quiz_third_question_result == 'incorrect' and condition == 1:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)
    
    incorrect_result_plus_one.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False) # draw vertical stim

elif first_stim_quiz_third_question_result == 'correct' and condition == 2:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_zero.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False) # draw vertical stim

elif first_stim_quiz_third_question_result == 'incorrect' and condition == 2:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_zero.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False) # draw vertical stim
# the Routine "first_quiz_third_question_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "total_reminder_one"-------
continueRoutine = True
# update component parameters for each repeat
first_reminder_key_resp.keys = []
first_reminder_key_resp.rt = []
_first_reminder_key_resp_allKeys = []
# draw reminder
if condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.17]
    vertical_feedback_stim.pos = [-.17, 0.17]
    grey_no_feedback_stim.pos = [.17, 0.17]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    result_final_reminder.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True)

# in condition 2, the horizontal stim means reward

elif condition == 2:
    
    horizontal_feedback_stim.pos = [-.17, 0.17]
    vertical_feedback_stim.pos = [0, 0.17]
    grey_no_feedback_stim.pos = [.17, 0.17]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    result_final_reminder.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True)
# keep track of which components have finished
total_reminder_oneComponents = [first_reminder_key_resp]
for thisComponent in total_reminder_oneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
total_reminder_oneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "total_reminder_one"-------
while continueRoutine:
    # get current time
    t = total_reminder_oneClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=total_reminder_oneClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *first_reminder_key_resp* updates
    waitOnFlip = False
    if first_reminder_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        first_reminder_key_resp.frameNStart = frameN  # exact frame index
        first_reminder_key_resp.tStart = t  # local t and not account for scr refresh
        first_reminder_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(first_reminder_key_resp, 'tStartRefresh')  # time at next scr refresh
        first_reminder_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(first_reminder_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(first_reminder_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if first_reminder_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = first_reminder_key_resp.getKeys(keyList=None, waitRelease=False)
        _first_reminder_key_resp_allKeys.extend(theseKeys)
        if len(_first_reminder_key_resp_allKeys):
            first_reminder_key_resp.keys = _first_reminder_key_resp_allKeys[-1].name  # just the last key pressed
            first_reminder_key_resp.rt = _first_reminder_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in total_reminder_oneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "total_reminder_one"-------
for thisComponent in total_reminder_oneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if first_reminder_key_resp.keys in ['', [], None]:  # No response was made
    first_reminder_key_resp.keys = None
thisExp.addData('first_reminder_key_resp.keys',first_reminder_key_resp.keys)
if first_reminder_key_resp.keys != None:  # we had a response
    thisExp.addData('first_reminder_key_resp.rt', first_reminder_key_resp.rt)
thisExp.addData('first_reminder_key_resp.started', first_reminder_key_resp.tStartRefresh)
thisExp.addData('first_reminder_key_resp.stopped', first_reminder_key_resp.tStopRefresh)
thisExp.nextEntry()
# draw reminder
if condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.17]
    vertical_feedback_stim.pos = [-.17, 0.17]
    grey_no_feedback_stim.pos = [.17, 0.17]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    result_final_reminder.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False)

# in condition 2, the horizontal stim means reward

elif condition == 2:
    
    horizontal_feedback_stim.pos = [-.17, 0.17]
    vertical_feedback_stim.pos = [0, 0.17]
    grey_no_feedback_stim.pos = [.17, 0.17]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    result_final_reminder.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False)

# add quiz data
psychoJS.experiment.addData('first_stim_quiz_first_question_result', first_stim_quiz_first_question_result)
psychoJS.experiment.addData('first_stim_quiz_second_question_result', first_stim_quiz_second_question_result)
psychoJS.experiment.addData('first_stim_quiz_third_question_result', first_stim_quiz_third_question_result)
# the Routine "total_reminder_one" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "continue_instructions_8_01"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_8_01.setAutoDraw(True)
slide_8_01_key_resp.keys = []
slide_8_01_key_resp.rt = []
_slide_8_01_key_resp_allKeys = []
# keep track of which components have finished
continue_instructions_8_01Components = [slide_8_01_key_resp]
for thisComponent in continue_instructions_8_01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_instructions_8_01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_instructions_8_01"-------
while continueRoutine:
    # get current time
    t = continue_instructions_8_01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_instructions_8_01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_8_01_key_resp* updates
    waitOnFlip = False
    if slide_8_01_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_8_01_key_resp.frameNStart = frameN  # exact frame index
        slide_8_01_key_resp.tStart = t  # local t and not account for scr refresh
        slide_8_01_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_8_01_key_resp, 'tStartRefresh')  # time at next scr refresh
        slide_8_01_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_8_01_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_8_01_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_8_01_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = slide_8_01_key_resp.getKeys(keyList=None, waitRelease=False)
        _slide_8_01_key_resp_allKeys.extend(theseKeys)
        if len(_slide_8_01_key_resp_allKeys):
            slide_8_01_key_resp.keys = _slide_8_01_key_resp_allKeys[-1].name  # just the last key pressed
            slide_8_01_key_resp.rt = _slide_8_01_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_instructions_8_01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_instructions_8_01"-------
for thisComponent in continue_instructions_8_01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_8_01.setAutoDraw(False)
# check responses
if slide_8_01_key_resp.keys in ['', [], None]:  # No response was made
    slide_8_01_key_resp.keys = None
thisExp.addData('slide_8_01_key_resp.keys',slide_8_01_key_resp.keys)
if slide_8_01_key_resp.keys != None:  # we had a response
    thisExp.addData('slide_8_01_key_resp.rt', slide_8_01_key_resp.rt)
thisExp.addData('slide_8_01_key_resp.started', slide_8_01_key_resp.tStartRefresh)
thisExp.addData('slide_8_01_key_resp.stopped', slide_8_01_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_instructions_8_01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "continue_instructions_8_02"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_8_02.setAutoDraw(True)
slide_8_02_key_resp.keys = []
slide_8_02_key_resp.rt = []
_slide_8_02_key_resp_allKeys = []
# keep track of which components have finished
continue_instructions_8_02Components = [slide_8_02_key_resp]
for thisComponent in continue_instructions_8_02Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_instructions_8_02Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_instructions_8_02"-------
while continueRoutine:
    # get current time
    t = continue_instructions_8_02Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_instructions_8_02Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_8_02_key_resp* updates
    waitOnFlip = False
    if slide_8_02_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_8_02_key_resp.frameNStart = frameN  # exact frame index
        slide_8_02_key_resp.tStart = t  # local t and not account for scr refresh
        slide_8_02_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_8_02_key_resp, 'tStartRefresh')  # time at next scr refresh
        slide_8_02_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_8_02_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_8_02_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_8_02_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = slide_8_02_key_resp.getKeys(keyList=None, waitRelease=False)
        _slide_8_02_key_resp_allKeys.extend(theseKeys)
        if len(_slide_8_02_key_resp_allKeys):
            slide_8_02_key_resp.keys = _slide_8_02_key_resp_allKeys[-1].name  # just the last key pressed
            slide_8_02_key_resp.rt = _slide_8_02_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_instructions_8_02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_instructions_8_02"-------
for thisComponent in continue_instructions_8_02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_8_02.setAutoDraw(False)
# check responses
if slide_8_02_key_resp.keys in ['', [], None]:  # No response was made
    slide_8_02_key_resp.keys = None
thisExp.addData('slide_8_02_key_resp.keys',slide_8_02_key_resp.keys)
if slide_8_02_key_resp.keys != None:  # we had a response
    thisExp.addData('slide_8_02_key_resp.rt', slide_8_02_key_resp.rt)
thisExp.addData('slide_8_02_key_resp.started', slide_8_02_key_resp.tStartRefresh)
thisExp.addData('slide_8_02_key_resp.stopped', slide_8_02_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_instructions_8_02" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "continue_instructions_8_03"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_8_03.setAutoDraw(True)
slide_8_03_key_resp.keys = []
slide_8_03_key_resp.rt = []
_slide_8_03_key_resp_allKeys = []
# keep track of which components have finished
continue_instructions_8_03Components = [slide_8_03_key_resp]
for thisComponent in continue_instructions_8_03Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_instructions_8_03Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_instructions_8_03"-------
while continueRoutine:
    # get current time
    t = continue_instructions_8_03Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_instructions_8_03Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_8_03_key_resp* updates
    waitOnFlip = False
    if slide_8_03_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_8_03_key_resp.frameNStart = frameN  # exact frame index
        slide_8_03_key_resp.tStart = t  # local t and not account for scr refresh
        slide_8_03_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_8_03_key_resp, 'tStartRefresh')  # time at next scr refresh
        slide_8_03_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_8_03_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_8_03_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_8_03_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = slide_8_03_key_resp.getKeys(keyList=None, waitRelease=False)
        _slide_8_03_key_resp_allKeys.extend(theseKeys)
        if len(_slide_8_03_key_resp_allKeys):
            slide_8_03_key_resp.keys = _slide_8_03_key_resp_allKeys[-1].name  # just the last key pressed
            slide_8_03_key_resp.rt = _slide_8_03_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_instructions_8_03Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_instructions_8_03"-------
for thisComponent in continue_instructions_8_03Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_8_03.setAutoDraw(False)
# check responses
if slide_8_03_key_resp.keys in ['', [], None]:  # No response was made
    slide_8_03_key_resp.keys = None
thisExp.addData('slide_8_03_key_resp.keys',slide_8_03_key_resp.keys)
if slide_8_03_key_resp.keys != None:  # we had a response
    thisExp.addData('slide_8_03_key_resp.rt', slide_8_03_key_resp.rt)
thisExp.addData('slide_8_03_key_resp.started', slide_8_03_key_resp.tStartRefresh)
thisExp.addData('slide_8_03_key_resp.stopped', slide_8_03_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_instructions_8_03" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "feedback_selection_quiz"-------
continueRoutine = True
# update component parameters for each repeat
# test work for feedback knowledge
select_feedback_to_press_slide.setAutoDraw(True)



feedback_selection_quiz_key_resp.keys = []
feedback_selection_quiz_key_resp.rt = []
_feedback_selection_quiz_key_resp_allKeys = []
# keep track of which components have finished
feedback_selection_quizComponents = [feedback_selection_quiz_key_resp]
for thisComponent in feedback_selection_quizComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedback_selection_quizClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedback_selection_quiz"-------
while continueRoutine:
    # get current time
    t = feedback_selection_quizClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedback_selection_quizClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedback_selection_quiz_key_resp* updates
    if feedback_selection_quiz_key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_selection_quiz_key_resp.frameNStart = frameN  # exact frame index
        feedback_selection_quiz_key_resp.tStart = t  # local t and not account for scr refresh
        feedback_selection_quiz_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_selection_quiz_key_resp, 'tStartRefresh')  # time at next scr refresh
        feedback_selection_quiz_key_resp.status = STARTED
        # keyboard checking is just starting
        feedback_selection_quiz_key_resp.clock.reset()  # now t=0
        feedback_selection_quiz_key_resp.clearEvents(eventType='keyboard')
    if feedback_selection_quiz_key_resp.status == STARTED:
        theseKeys = feedback_selection_quiz_key_resp.getKeys(keyList=['w', 'o'], waitRelease=False)
        _feedback_selection_quiz_key_resp_allKeys.extend(theseKeys)
        if len(_feedback_selection_quiz_key_resp_allKeys):
            feedback_selection_quiz_key_resp.keys = _feedback_selection_quiz_key_resp_allKeys[-1].name  # just the last key pressed
            feedback_selection_quiz_key_resp.rt = _feedback_selection_quiz_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback_selection_quizComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback_selection_quiz"-------
for thisComponent in feedback_selection_quizComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if feedback_selection_quiz_key_resp.keys == 'o' and select_feedback_to_press == 1:   # correct
    feedback_to_press_outcome = 'correct'
    quiz_and_attention_check_fails = quiz_and_attention_check_fails

elif feedback_selection_quiz_key_resp.keys == 'w' and select_feedback_to_press == 1:   # incorrect
    feedback_to_press_outcome = 'incorrect'
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
        
elif feedback_selection_quiz_key_resp.keys == 'o' and select_feedback_to_press == 2: # incorrect
    feedback_to_press_outcome = 'incorrect'
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1

elif feedback_selection_quiz_key_resp.keys == 'w' and select_feedback_to_press == 2:   # correct
    feedback_to_press_outcome = 'correct'
    quiz_and_attention_check_fails = quiz_and_attention_check_fails

select_feedback_to_press_slide.setAutoDraw(False)
# check responses
if feedback_selection_quiz_key_resp.keys in ['', [], None]:  # No response was made
    feedback_selection_quiz_key_resp.keys = None
thisExp.addData('feedback_selection_quiz_key_resp.keys',feedback_selection_quiz_key_resp.keys)
if feedback_selection_quiz_key_resp.keys != None:  # we had a response
    thisExp.addData('feedback_selection_quiz_key_resp.rt', feedback_selection_quiz_key_resp.rt)
thisExp.addData('feedback_selection_quiz_key_resp.started', feedback_selection_quiz_key_resp.tStart)
thisExp.addData('feedback_selection_quiz_key_resp.stopped', feedback_selection_quiz_key_resp.tStop)
thisExp.nextEntry()
# the Routine "feedback_selection_quiz" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "feedback_post_quiz_reminder"-------
continueRoutine = True
# update component parameters for each repeat
# draw reminder
if feedback_to_press_outcome == 'correct':
    correct_feedback_reminder.setAutoDraw(True)
elif feedback_to_press_outcome == 'incorrect':
    incorrect_feedback_reminder.setAutoDraw(True)
feedback_post_quiz_reminder_key_resp.keys = []
feedback_post_quiz_reminder_key_resp.rt = []
_feedback_post_quiz_reminder_key_resp_allKeys = []
# keep track of which components have finished
feedback_post_quiz_reminderComponents = [feedback_post_quiz_reminder_key_resp]
for thisComponent in feedback_post_quiz_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedback_post_quiz_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedback_post_quiz_reminder"-------
while continueRoutine:
    # get current time
    t = feedback_post_quiz_reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedback_post_quiz_reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedback_post_quiz_reminder_key_resp* updates
    waitOnFlip = False
    if feedback_post_quiz_reminder_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedback_post_quiz_reminder_key_resp.frameNStart = frameN  # exact frame index
        feedback_post_quiz_reminder_key_resp.tStart = t  # local t and not account for scr refresh
        feedback_post_quiz_reminder_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_post_quiz_reminder_key_resp, 'tStartRefresh')  # time at next scr refresh
        feedback_post_quiz_reminder_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(feedback_post_quiz_reminder_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(feedback_post_quiz_reminder_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if feedback_post_quiz_reminder_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = feedback_post_quiz_reminder_key_resp.getKeys(keyList=None, waitRelease=False)
        _feedback_post_quiz_reminder_key_resp_allKeys.extend(theseKeys)
        if len(_feedback_post_quiz_reminder_key_resp_allKeys):
            feedback_post_quiz_reminder_key_resp.keys = _feedback_post_quiz_reminder_key_resp_allKeys[-1].name  # just the last key pressed
            feedback_post_quiz_reminder_key_resp.rt = _feedback_post_quiz_reminder_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback_post_quiz_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback_post_quiz_reminder"-------
for thisComponent in feedback_post_quiz_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# draw reminder
if feedback_to_press_outcome == 'correct':
    correct_feedback_reminder.setAutoDraw(False)
elif feedback_to_press_outcome == 'incorrect':
    incorrect_feedback_reminder.setAutoDraw(False)

# add data
psychoJS.experiment.addData('feedback_selection_quiz_result', feedback_to_press_outcome)
# check responses
if feedback_post_quiz_reminder_key_resp.keys in ['', [], None]:  # No response was made
    feedback_post_quiz_reminder_key_resp.keys = None
thisExp.addData('feedback_post_quiz_reminder_key_resp.keys',feedback_post_quiz_reminder_key_resp.keys)
if feedback_post_quiz_reminder_key_resp.keys != None:  # we had a response
    thisExp.addData('feedback_post_quiz_reminder_key_resp.rt', feedback_post_quiz_reminder_key_resp.rt)
thisExp.addData('feedback_post_quiz_reminder_key_resp.started', feedback_post_quiz_reminder_key_resp.tStartRefresh)
thisExp.addData('feedback_post_quiz_reminder_key_resp.stopped', feedback_post_quiz_reminder_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "feedback_post_quiz_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "continue_slide_09_01"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_09_01.setAutoDraw(True)
slide_09_01_key_resp.keys = []
slide_09_01_key_resp.rt = []
_slide_09_01_key_resp_allKeys = []
# keep track of which components have finished
continue_slide_09_01Components = [slide_09_01_key_resp]
for thisComponent in continue_slide_09_01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_slide_09_01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_slide_09_01"-------
while continueRoutine:
    # get current time
    t = continue_slide_09_01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_slide_09_01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_09_01_key_resp* updates
    waitOnFlip = False
    if slide_09_01_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_09_01_key_resp.frameNStart = frameN  # exact frame index
        slide_09_01_key_resp.tStart = t  # local t and not account for scr refresh
        slide_09_01_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_09_01_key_resp, 'tStartRefresh')  # time at next scr refresh
        slide_09_01_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_09_01_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_09_01_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_09_01_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = slide_09_01_key_resp.getKeys(keyList=None, waitRelease=False)
        _slide_09_01_key_resp_allKeys.extend(theseKeys)
        if len(_slide_09_01_key_resp_allKeys):
            slide_09_01_key_resp.keys = _slide_09_01_key_resp_allKeys[-1].name  # just the last key pressed
            slide_09_01_key_resp.rt = _slide_09_01_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_slide_09_01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_slide_09_01"-------
for thisComponent in continue_slide_09_01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_09_01.setAutoDraw(False)
# check responses
if slide_09_01_key_resp.keys in ['', [], None]:  # No response was made
    slide_09_01_key_resp.keys = None
thisExp.addData('slide_09_01_key_resp.keys',slide_09_01_key_resp.keys)
if slide_09_01_key_resp.keys != None:  # we had a response
    thisExp.addData('slide_09_01_key_resp.rt', slide_09_01_key_resp.rt)
thisExp.addData('slide_09_01_key_resp.started', slide_09_01_key_resp.tStartRefresh)
thisExp.addData('slide_09_01_key_resp.stopped', slide_09_01_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_slide_09_01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "continue_slide_09_02"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_09_02.setAutoDraw(True)
slide_09_02_key_resp.keys = []
slide_09_02_key_resp.rt = []
_slide_09_02_key_resp_allKeys = []
# keep track of which components have finished
continue_slide_09_02Components = [slide_09_02_key_resp]
for thisComponent in continue_slide_09_02Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_slide_09_02Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_slide_09_02"-------
while continueRoutine:
    # get current time
    t = continue_slide_09_02Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_slide_09_02Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_09_02_key_resp* updates
    waitOnFlip = False
    if slide_09_02_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_09_02_key_resp.frameNStart = frameN  # exact frame index
        slide_09_02_key_resp.tStart = t  # local t and not account for scr refresh
        slide_09_02_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_09_02_key_resp, 'tStartRefresh')  # time at next scr refresh
        slide_09_02_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_09_02_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_09_02_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_09_02_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = slide_09_02_key_resp.getKeys(keyList=None, waitRelease=False)
        _slide_09_02_key_resp_allKeys.extend(theseKeys)
        if len(_slide_09_02_key_resp_allKeys):
            slide_09_02_key_resp.keys = _slide_09_02_key_resp_allKeys[-1].name  # just the last key pressed
            slide_09_02_key_resp.rt = _slide_09_02_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_slide_09_02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_slide_09_02"-------
for thisComponent in continue_slide_09_02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_09_02.setAutoDraw(False)
# check responses
if slide_09_02_key_resp.keys in ['', [], None]:  # No response was made
    slide_09_02_key_resp.keys = None
thisExp.addData('slide_09_02_key_resp.keys',slide_09_02_key_resp.keys)
if slide_09_02_key_resp.keys != None:  # we had a response
    thisExp.addData('slide_09_02_key_resp.rt', slide_09_02_key_resp.rt)
thisExp.addData('slide_09_02_key_resp.started', slide_09_02_key_resp.tStartRefresh)
thisExp.addData('slide_09_02_key_resp.stopped', slide_09_02_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_slide_09_02" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "continue_slide_10_01"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_10_01.setAutoDraw(True)
slide_10_01_key_resp.keys = []
slide_10_01_key_resp.rt = []
_slide_10_01_key_resp_allKeys = []
# keep track of which components have finished
continue_slide_10_01Components = [slide_10_01_key_resp]
for thisComponent in continue_slide_10_01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_slide_10_01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_slide_10_01"-------
while continueRoutine:
    # get current time
    t = continue_slide_10_01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_slide_10_01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_10_01_key_resp* updates
    waitOnFlip = False
    if slide_10_01_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_10_01_key_resp.frameNStart = frameN  # exact frame index
        slide_10_01_key_resp.tStart = t  # local t and not account for scr refresh
        slide_10_01_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_10_01_key_resp, 'tStartRefresh')  # time at next scr refresh
        slide_10_01_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_10_01_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_10_01_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_10_01_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = slide_10_01_key_resp.getKeys(keyList=None, waitRelease=False)
        _slide_10_01_key_resp_allKeys.extend(theseKeys)
        if len(_slide_10_01_key_resp_allKeys):
            slide_10_01_key_resp.keys = _slide_10_01_key_resp_allKeys[-1].name  # just the last key pressed
            slide_10_01_key_resp.rt = _slide_10_01_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_slide_10_01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_slide_10_01"-------
for thisComponent in continue_slide_10_01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_10_01.setAutoDraw(False)
# check responses
if slide_10_01_key_resp.keys in ['', [], None]:  # No response was made
    slide_10_01_key_resp.keys = None
thisExp.addData('slide_10_01_key_resp.keys',slide_10_01_key_resp.keys)
if slide_10_01_key_resp.keys != None:  # we had a response
    thisExp.addData('slide_10_01_key_resp.rt', slide_10_01_key_resp.rt)
thisExp.addData('slide_10_01_key_resp.started', slide_10_01_key_resp.tStartRefresh)
thisExp.addData('slide_10_01_key_resp.stopped', slide_10_01_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_slide_10_01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "continue_slide_10_02"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_10_02.setAutoDraw(True)
slide_10_02_key_resp.keys = []
slide_10_02_key_resp.rt = []
_slide_10_02_key_resp_allKeys = []
# keep track of which components have finished
continue_slide_10_02Components = [slide_10_02_key_resp]
for thisComponent in continue_slide_10_02Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_slide_10_02Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_slide_10_02"-------
while continueRoutine:
    # get current time
    t = continue_slide_10_02Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_slide_10_02Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_10_02_key_resp* updates
    waitOnFlip = False
    if slide_10_02_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_10_02_key_resp.frameNStart = frameN  # exact frame index
        slide_10_02_key_resp.tStart = t  # local t and not account for scr refresh
        slide_10_02_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_10_02_key_resp, 'tStartRefresh')  # time at next scr refresh
        slide_10_02_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_10_02_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_10_02_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_10_02_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = slide_10_02_key_resp.getKeys(keyList=None, waitRelease=False)
        _slide_10_02_key_resp_allKeys.extend(theseKeys)
        if len(_slide_10_02_key_resp_allKeys):
            slide_10_02_key_resp.keys = _slide_10_02_key_resp_allKeys[-1].name  # just the last key pressed
            slide_10_02_key_resp.rt = _slide_10_02_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_slide_10_02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_slide_10_02"-------
for thisComponent in continue_slide_10_02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_10_02.setAutoDraw(False)
# check responses
if slide_10_02_key_resp.keys in ['', [], None]:  # No response was made
    slide_10_02_key_resp.keys = None
thisExp.addData('slide_10_02_key_resp.keys',slide_10_02_key_resp.keys)
if slide_10_02_key_resp.keys != None:  # we had a response
    thisExp.addData('slide_10_02_key_resp.rt', slide_10_02_key_resp.rt)
thisExp.addData('slide_10_02_key_resp.started', slide_10_02_key_resp.tStartRefresh)
thisExp.addData('slide_10_02_key_resp.stopped', slide_10_02_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_slide_10_02" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "attention_shape_check"-------
continueRoutine = True
# update component parameters for each repeat
get_shape_response.keys = []
get_shape_response.rt = []
_get_shape_response_allKeys = []
# keep track of which components have finished
attention_shape_checkComponents = [get_shape_response]
for thisComponent in attention_shape_checkComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
attention_shape_checkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "attention_shape_check"-------
while continueRoutine:
    # get current time
    t = attention_shape_checkClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=attention_shape_checkClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    shapes_question.setAutoDraw(True)
    
    # *get_shape_response* updates
    waitOnFlip = False
    if get_shape_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        get_shape_response.frameNStart = frameN  # exact frame index
        get_shape_response.tStart = t  # local t and not account for scr refresh
        get_shape_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(get_shape_response, 'tStartRefresh')  # time at next scr refresh
        get_shape_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(get_shape_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(get_shape_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if get_shape_response.status == STARTED and not waitOnFlip:
        theseKeys = get_shape_response.getKeys(keyList=['1', '2'], waitRelease=False)
        _get_shape_response_allKeys.extend(theseKeys)
        if len(_get_shape_response_allKeys):
            get_shape_response.keys = _get_shape_response_allKeys[-1].name  # just the last key pressed
            get_shape_response.rt = _get_shape_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in attention_shape_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "attention_shape_check"-------
for thisComponent in attention_shape_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check if correct and update count of fails
if get_shape_response.keys == '1':
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    shape_quiz_result = 'incorrect'
    
elif get_shape_response.keys == '2':
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    shape_quiz_result = 'correct'
    
shapes_question.setAutoDraw(False)
# check responses
if get_shape_response.keys in ['', [], None]:  # No response was made
    get_shape_response.keys = None
thisExp.addData('get_shape_response.keys',get_shape_response.keys)
if get_shape_response.keys != None:  # we had a response
    thisExp.addData('get_shape_response.rt', get_shape_response.rt)
thisExp.addData('get_shape_response.started', get_shape_response.tStartRefresh)
thisExp.addData('get_shape_response.stopped', get_shape_response.tStopRefresh)
thisExp.nextEntry()
# the Routine "attention_shape_check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "attention_reminder"-------
continueRoutine = True
# update component parameters for each repeat
attention_reminder_key_resp.keys = []
attention_reminder_key_resp.rt = []
_attention_reminder_key_resp_allKeys = []
if shape_quiz_result == 'correct':
    correct_shape.setAutoDraw(True)

elif shape_quiz_result == 'incorrect':
    incorrect_shape.setAutoDraw(True)
# keep track of which components have finished
attention_reminderComponents = [attention_reminder_key_resp]
for thisComponent in attention_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
attention_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "attention_reminder"-------
while continueRoutine:
    # get current time
    t = attention_reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=attention_reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *attention_reminder_key_resp* updates
    waitOnFlip = False
    if attention_reminder_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        attention_reminder_key_resp.frameNStart = frameN  # exact frame index
        attention_reminder_key_resp.tStart = t  # local t and not account for scr refresh
        attention_reminder_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(attention_reminder_key_resp, 'tStartRefresh')  # time at next scr refresh
        attention_reminder_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(attention_reminder_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(attention_reminder_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if attention_reminder_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = attention_reminder_key_resp.getKeys(keyList=None, waitRelease=False)
        _attention_reminder_key_resp_allKeys.extend(theseKeys)
        if len(_attention_reminder_key_resp_allKeys):
            attention_reminder_key_resp.keys = _attention_reminder_key_resp_allKeys[-1].name  # just the last key pressed
            attention_reminder_key_resp.rt = _attention_reminder_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in attention_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "attention_reminder"-------
for thisComponent in attention_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if attention_reminder_key_resp.keys in ['', [], None]:  # No response was made
    attention_reminder_key_resp.keys = None
thisExp.addData('attention_reminder_key_resp.keys',attention_reminder_key_resp.keys)
if attention_reminder_key_resp.keys != None:  # we had a response
    thisExp.addData('attention_reminder_key_resp.rt', attention_reminder_key_resp.rt)
thisExp.addData('attention_reminder_key_resp.started', attention_reminder_key_resp.tStartRefresh)
thisExp.addData('attention_reminder_key_resp.stopped', attention_reminder_key_resp.tStopRefresh)
thisExp.nextEntry()
if shape_quiz_result == 'correct':
    correct_shape.setAutoDraw(False)

elif shape_quiz_result == 'incorrect':
    incorrect_shape.setAutoDraw(False)

# add data
psychoJS.experiment.addData('shape_quiz_result', shape_quiz_result)
# the Routine "attention_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "continue_instructions_even_further_11"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_eleven.setAutoDraw(True)

slide_11_key_resp.keys = []
slide_11_key_resp.rt = []
_slide_11_key_resp_allKeys = []
# keep track of which components have finished
continue_instructions_even_further_11Components = [slide_11_key_resp]
for thisComponent in continue_instructions_even_further_11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_instructions_even_further_11Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_instructions_even_further_11"-------
while continueRoutine:
    # get current time
    t = continue_instructions_even_further_11Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_instructions_even_further_11Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slide_11_key_resp* updates
    waitOnFlip = False
    if slide_11_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slide_11_key_resp.frameNStart = frameN  # exact frame index
        slide_11_key_resp.tStart = t  # local t and not account for scr refresh
        slide_11_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slide_11_key_resp, 'tStartRefresh')  # time at next scr refresh
        slide_11_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(slide_11_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(slide_11_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if slide_11_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = slide_11_key_resp.getKeys(keyList=None, waitRelease=False)
        _slide_11_key_resp_allKeys.extend(theseKeys)
        if len(_slide_11_key_resp_allKeys):
            slide_11_key_resp.keys = _slide_11_key_resp_allKeys[-1].name  # just the last key pressed
            slide_11_key_resp.rt = _slide_11_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_instructions_even_further_11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_instructions_even_further_11"-------
for thisComponent in continue_instructions_even_further_11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_eleven.setAutoDraw(False)
# check responses
if slide_11_key_resp.keys in ['', [], None]:  # No response was made
    slide_11_key_resp.keys = None
thisExp.addData('slide_11_key_resp.keys',slide_11_key_resp.keys)
if slide_11_key_resp.keys != None:  # we had a response
    thisExp.addData('slide_11_key_resp.rt', slide_11_key_resp.rt)
thisExp.addData('slide_11_key_resp.started', slide_11_key_resp.tStartRefresh)
thisExp.addData('slide_11_key_resp.stopped', slide_11_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_instructions_even_further_11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "calib_one"-------
continueRoutine = True
# update component parameters for each repeat
calibration_slide_1.setAutoDraw(True)
calib_one_space.keys = []
calib_one_space.rt = []
_calib_one_space_allKeys = []
# keep track of which components have finished
calib_oneComponents = [calib_one_space]
for thisComponent in calib_oneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
calib_oneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "calib_one"-------
while continueRoutine:
    # get current time
    t = calib_oneClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=calib_oneClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *calib_one_space* updates
    waitOnFlip = False
    if calib_one_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calib_one_space.frameNStart = frameN  # exact frame index
        calib_one_space.tStart = t  # local t and not account for scr refresh
        calib_one_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calib_one_space, 'tStartRefresh')  # time at next scr refresh
        calib_one_space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(calib_one_space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(calib_one_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if calib_one_space.status == STARTED and not waitOnFlip:
        theseKeys = calib_one_space.getKeys(keyList=['space'], waitRelease=False)
        _calib_one_space_allKeys.extend(theseKeys)
        if len(_calib_one_space_allKeys):
            calib_one_space.keys = _calib_one_space_allKeys[-1].name  # just the last key pressed
            calib_one_space.rt = _calib_one_space_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calib_oneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "calib_one"-------
for thisComponent in calib_oneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
calibration_slide_1.setAutoDraw(False)
# check responses
if calib_one_space.keys in ['', [], None]:  # No response was made
    calib_one_space.keys = None
thisExp.addData('calib_one_space.keys',calib_one_space.keys)
if calib_one_space.keys != None:  # we had a response
    thisExp.addData('calib_one_space.rt', calib_one_space.rt)
thisExp.addData('calib_one_space.started', calib_one_space.tStartRefresh)
thisExp.addData('calib_one_space.stopped', calib_one_space.tStopRefresh)
thisExp.nextEntry()
# the Routine "calib_one" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "calib_last"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# set calibration parameters
calibration_update_duration = .25
calibration_total_presses = 0 
slide_number = 2
show_slide = visual.ImageStim(win=win,
                            image='calibration/slide' + str(slide_number) + '.png',
                            size = (1,.75))

calibration_update_duration = .25
calibration_total_presses = 0
calibration_time = 3
time_of_calibration_press = []
time_of_calibration_press_list = []
calibration_space_bar_press.keys = []
calibration_space_bar_press.rt = []
_calibration_space_bar_press_allKeys = []
# keep track of which components have finished
calib_lastComponents = [calibration_space_bar_press]
for thisComponent in calib_lastComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
calib_lastClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "calib_last"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = calib_lastClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=calib_lastClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    show_slide = visual.ImageStim(win=win,
                                image='calibration/slide' + str(slide_number) + '.png',
                                size = (1,.75))
    
    show_slide.setAutoDraw(True)
    
    calib_keys = psychoJS.eventManager.getKeys();
    if 'space' in calib_keys:
        
        time_of_calibration_press = calib_lastClock.getTime()
        time_of_calibration_press_list.push(time_of_calibration_press)
        calibration_total_presses = calibration_total_presses + 1
        
        if calib_lastClock.getTime() > calibration_update_duration:
            slide_number = slide_number + 1
            calibration_update_duration = calibration_update_duration + 0.25
    
    if calib_lastClock.getTime() > 3:
        show_slide.setAutoDraw(False)
    
    # *calibration_space_bar_press* updates
    waitOnFlip = False
    if calibration_space_bar_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calibration_space_bar_press.frameNStart = frameN  # exact frame index
        calibration_space_bar_press.tStart = t  # local t and not account for scr refresh
        calibration_space_bar_press.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calibration_space_bar_press, 'tStartRefresh')  # time at next scr refresh
        calibration_space_bar_press.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(calibration_space_bar_press.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(calibration_space_bar_press.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if calibration_space_bar_press.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 3.0-frameTolerance:
            # keep track of stop time/frame for later
            calibration_space_bar_press.tStop = t  # not accounting for scr refresh
            calibration_space_bar_press.frameNStop = frameN  # exact frame index
            win.timeOnFlip(calibration_space_bar_press, 'tStopRefresh')  # time at next scr refresh
            calibration_space_bar_press.status = FINISHED
    if calibration_space_bar_press.status == STARTED and not waitOnFlip:
        theseKeys = calibration_space_bar_press.getKeys(keyList=['space'], waitRelease=False)
        _calibration_space_bar_press_allKeys.extend(theseKeys)
        if len(_calibration_space_bar_press_allKeys):
            calibration_space_bar_press.keys = [key.name for key in _calibration_space_bar_press_allKeys]  # storing all keys
            calibration_space_bar_press.rt = [key.rt for key in _calibration_space_bar_press_allKeys]
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calib_lastComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "calib_last"-------
for thisComponent in calib_lastComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
show_slide.setAutoDraw(False)
blank_screen_image_black.setAutoDraw(True)

# calculate work for feedback threshold
maximum_work_for_feedback_threshold = calibration_total_presses / calibration_time
work_for_feedback_threshold_multiplier = .9
final_work_for_feedback_threshold = work_for_feedback_threshold_multiplier * maximum_work_for_feedback_threshold

# add data
psychoJS.experiment.addData('maximum_work_for_feedback_threshold', maximum_work_for_feedback_threshold)
psychoJS.experiment.addData('final_work_for_feedback_threshold', final_work_for_feedback_threshold)
# check responses
if calibration_space_bar_press.keys in ['', [], None]:  # No response was made
    calibration_space_bar_press.keys = None
thisExp.addData('calibration_space_bar_press.keys',calibration_space_bar_press.keys)
if calibration_space_bar_press.keys != None:  # we had a response
    thisExp.addData('calibration_space_bar_press.rt', calibration_space_bar_press.rt)
thisExp.addData('calibration_space_bar_press.started', calibration_space_bar_press.tStartRefresh)
thisExp.addData('calibration_space_bar_press.stopped', calibration_space_bar_press.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "advance_to_practice_session"-------
continueRoutine = True
# update component parameters for each repeat
enter_to_practice_session.keys = []
enter_to_practice_session.rt = []
_enter_to_practice_session_allKeys = []
instructions_slide_twelve.setAutoDraw(True)
# keep track of which components have finished
advance_to_practice_sessionComponents = [enter_to_practice_session]
for thisComponent in advance_to_practice_sessionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
advance_to_practice_sessionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "advance_to_practice_session"-------
while continueRoutine:
    # get current time
    t = advance_to_practice_sessionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=advance_to_practice_sessionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *enter_to_practice_session* updates
    waitOnFlip = False
    if enter_to_practice_session.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter_to_practice_session.frameNStart = frameN  # exact frame index
        enter_to_practice_session.tStart = t  # local t and not account for scr refresh
        enter_to_practice_session.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter_to_practice_session, 'tStartRefresh')  # time at next scr refresh
        enter_to_practice_session.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter_to_practice_session.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter_to_practice_session.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter_to_practice_session.status == STARTED and not waitOnFlip:
        theseKeys = enter_to_practice_session.getKeys(keyList=['return'], waitRelease=False)
        _enter_to_practice_session_allKeys.extend(theseKeys)
        if len(_enter_to_practice_session_allKeys):
            enter_to_practice_session.keys = _enter_to_practice_session_allKeys[-1].name  # just the last key pressed
            enter_to_practice_session.rt = _enter_to_practice_session_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in advance_to_practice_sessionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "advance_to_practice_session"-------
for thisComponent in advance_to_practice_sessionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if enter_to_practice_session.keys in ['', [], None]:  # No response was made
    enter_to_practice_session.keys = None
thisExp.addData('enter_to_practice_session.keys',enter_to_practice_session.keys)
if enter_to_practice_session.keys != None:  # we had a response
    thisExp.addData('enter_to_practice_session.rt', enter_to_practice_session.rt)
thisExp.addData('enter_to_practice_session.started', enter_to_practice_session.tStartRefresh)
thisExp.addData('enter_to_practice_session.stopped', enter_to_practice_session.tStopRefresh)
thisExp.nextEntry()
instructions_slide_twelve.setAutoDraw(False)
# the Routine "advance_to_practice_session" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/practice_task_option_' + excel_sheet_choice_practice + '.xlsx'),
    seed=None, name='prac_trials')
thisExp.addLoop(prac_trials)  # add the loop to the experiment
thisPrac_trial = prac_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
if thisPrac_trial != None:
    for paramName in thisPrac_trial:
        exec('{} = thisPrac_trial[paramName]'.format(paramName))

for thisPrac_trial in prac_trials:
    currentLoop = prac_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
    if thisPrac_trial != None:
        for paramName in thisPrac_trial:
            exec('{} = thisPrac_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_task"-------
    continueRoutine = True
    # update component parameters for each repeat
    # add data
    work_total_presses = 0
    prac_trial_num = prac_trial_num + 1
    psychoJS.experiment.addData('mode', 'practice')
    psychoJS.experiment.addData('prac_trial_num', prac_trial_num)
    psychoJS.experiment.addData('calibration_total_presses', calibration_total_presses)
    psychoJS.experiment.addData('maximum_work_for_feedback_threshold', maximum_work_for_feedback_threshold)
    psychoJS.experiment.addData('final_work_for_feedback_threshold', final_work_for_feedback_threshold)
    fractal_one_prac.setPos((fractal_60_x_pos, fractal_60_y_pos))
    fractal_one_prac.setImage(fractal_60_stim)
    fractal_two_prac.setPos((fractal_80_x_pos, fractal_80_y_pos))
    fractal_two_prac.setImage(fractal_80_stim)
    key_resp_prac.keys = []
    key_resp_prac.rt = []
    _key_resp_prac_allKeys = []
    # initialize empty lists so we can add data
    decision_to_work_for_feedback = []
    time_of_press_list = []
    current_work_rate_list = []
    current_opacity_level_list = []
    final_opacity_level = []
    # keep track of which components have finished
    practice_taskComponents = [iti_prac, fractal_one_prac, fractal_two_prac, key_resp_prac]
    for thisComponent in practice_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_task"-------
    while continueRoutine:
        # get current time
        t = practice_taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti_prac* updates
        if iti_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iti_prac.frameNStart = frameN  # exact frame index
            iti_prac.tStart = t  # local t and not account for scr refresh
            iti_prac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti_prac, 'tStartRefresh')  # time at next scr refresh
            iti_prac.setAutoDraw(True)
        if iti_prac.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti_prac.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                iti_prac.tStop = t  # not accounting for scr refresh
                iti_prac.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iti_prac, 'tStopRefresh')  # time at next scr refresh
                iti_prac.setAutoDraw(False)
        
        # *fractal_one_prac* updates
        if fractal_one_prac.status == NOT_STARTED and iti_prac.status==FINISHED:
            # keep track of start time/frame for later
            fractal_one_prac.frameNStart = frameN  # exact frame index
            fractal_one_prac.tStart = t  # local t and not account for scr refresh
            fractal_one_prac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fractal_one_prac, 'tStartRefresh')  # time at next scr refresh
            fractal_one_prac.setAutoDraw(True)
        if fractal_one_prac.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fractal_one_prac.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fractal_one_prac.tStop = t  # not accounting for scr refresh
                fractal_one_prac.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fractal_one_prac, 'tStopRefresh')  # time at next scr refresh
                fractal_one_prac.setAutoDraw(False)
        
        # *fractal_two_prac* updates
        if fractal_two_prac.status == NOT_STARTED and iti_prac.status==FINISHED:
            # keep track of start time/frame for later
            fractal_two_prac.frameNStart = frameN  # exact frame index
            fractal_two_prac.tStart = t  # local t and not account for scr refresh
            fractal_two_prac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fractal_two_prac, 'tStartRefresh')  # time at next scr refresh
            fractal_two_prac.setAutoDraw(True)
        if fractal_two_prac.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fractal_two_prac.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fractal_two_prac.tStop = t  # not accounting for scr refresh
                fractal_two_prac.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fractal_two_prac, 'tStopRefresh')  # time at next scr refresh
                fractal_two_prac.setAutoDraw(False)
        
        # *key_resp_prac* updates
        waitOnFlip = False
        if key_resp_prac.status == NOT_STARTED and iti_prac.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_prac.frameNStart = frameN  # exact frame index
            key_resp_prac.tStart = t  # local t and not account for scr refresh
            key_resp_prac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_prac, 'tStartRefresh')  # time at next scr refresh
            key_resp_prac.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_prac.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_prac.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_prac.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_prac.tStop = t  # not accounting for scr refresh
                key_resp_prac.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_prac, 'tStopRefresh')  # time at next scr refresh
                key_resp_prac.status = FINISHED
        if key_resp_prac.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_prac.getKeys(keyList=['f', 'j'], waitRelease=False)
            _key_resp_prac_allKeys.extend(theseKeys)
            if len(_key_resp_prac_allKeys):
                key_resp_prac.keys = _key_resp_prac_allKeys[-1].name  # just the last key pressed
                key_resp_prac.rt = _key_resp_prac_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_task"-------
    for thisComponent in practice_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_trials.addData('iti_prac.started', iti_prac.tStartRefresh)
    prac_trials.addData('iti_prac.stopped', iti_prac.tStopRefresh)
    prac_trials.addData('fractal_one_prac.started', fractal_one_prac.tStartRefresh)
    prac_trials.addData('fractal_one_prac.stopped', fractal_one_prac.tStopRefresh)
    prac_trials.addData('fractal_two_prac.started', fractal_two_prac.tStartRefresh)
    prac_trials.addData('fractal_two_prac.stopped', fractal_two_prac.tStopRefresh)
    # check responses
    if key_resp_prac.keys in ['', [], None]:  # No response was made
        key_resp_prac.keys = None
    prac_trials.addData('key_resp_prac.keys',key_resp_prac.keys)
    if key_resp_prac.keys != None:  # we had a response
        prac_trials.addData('key_resp_prac.rt', key_resp_prac.rt)
    prac_trials.addData('key_resp_prac.started', key_resp_prac.tStartRefresh)
    prac_trials.addData('key_resp_prac.stopped', key_resp_prac.tStopRefresh)
    # initialize empty lists for data
    outcome = []
    side_chosen = []
    fractal_chosen = []
    reward = []
    
    # outcome algorithm based on response and condition
    if condition == 1:
        if key_resp_prac.keys == 'f' and fractal_60_side == 'left' and fractal_60_reward == 1:
            outcome = 'good'
            side_chosen = 'left'
            fractal_chosen = 'fractal_60'
            reward = 1
            prac_total_points = prac_total_points + 1
    
        elif key_resp_prac.keys == 'f' and fractal_60_side == 'left' and fractal_60_reward == 0:
            outcome = 'bad'
            side_chosen = 'left'
            fractal_chosen = 'fractal_60'
            reward = 0
            prac_total_points = prac_total_points
            
        elif key_resp_prac.keys == 'j' and fractal_60_side == 'right' and fractal_60_reward == 1:
            outcome = 'good'
            side_chosen = 'right'
            fractal_chosen = 'fractal_60'
            reward = 1
            prac_total_points = prac_total_points + 1
            
        elif key_resp_prac.keys == 'j' and fractal_60_side == 'right' and fractal_60_reward == 0:
            outcome = 'bad'
            side_chosen = 'right'
            fractal_chosen = 'fractal_60'
            reward = 0
            prac_total_points = prac_total_points
    
        elif key_resp_prac.keys == 'f' and fractal_80_side == 'left' and fractal_80_reward == 1:
            outcome = 'good'
            side_chosen = 'left'
            fractal_chosen = 'fractal_80'
            reward = 1
            prac_total_points = prac_total_points + 1
        
        elif key_resp_prac.keys == 'f' and fractal_80_side == 'left' and fractal_80_reward == 0:
            outcome = 'bad'
            side_chosen = 'left'
            fractal_chosen = 'fractal_80'
            reward = 0
            prac_total_points = prac_total_points
        
        elif key_resp_prac.keys == 'j' and fractal_80_side == 'right' and fractal_80_reward == 1:
            outcome = 'good'
            side_chosen = 'right'
            fractal_chosen = 'fractal_80'
            reward = 1
            prac_total_points = prac_total_points + 1
        
        elif key_resp_prac.keys == 'j' and fractal_80_side == 'right' and fractal_80_reward == 0:
            outcome = 'bad'
            side_chosen = 'right'
            fractal_chosen = 'fractal_80'
            reward = 0
            prac_total_points = prac_total_points
        
        else:
            outcome = 'missed'
            side_chosen = 'n/a'
            fractal_chosen = 'n/a'
            reward = 0
            prac_total_points = prac_total_points
            
    elif condition == 2:
        if key_resp_prac.keys == 'f' and fractal_60_side == 'left' and fractal_60_reward == 1:
            outcome = 'good'
            side_chosen = 'left'
            fractal_chosen = 'fractal_60'
            reward = 1
            prac_total_points = prac_total_points + 1
            
        elif key_resp_prac.keys == 'f' and fractal_60_side == 'left' and fractal_60_reward == 0:
            outcome = 'bad'
            side_chosen = 'left'
            fractal_chosen = 'fractal_60'
            reward = 0
            prac_total_points = prac_total_points
    
        elif key_resp_prac.keys == 'j' and fractal_60_side == 'right' and fractal_60_reward == 1:
            outcome = 'good'
            side_chosen = 'right'
            fractal_chosen = 'fractal_60'
            reward = 1
            prac_total_points = prac_total_points + 1
            
        elif key_resp_prac.keys == 'j' and fractal_60_side == 'right' and fractal_60_reward == 0:
            outcome = 'bad'
            side_chosen = 'right'
            fractal_chosen = 'fractal_60'
            reward = 0
            prac_total_points = prac_total_points
        
        elif key_resp_prac.keys == 'f' and fractal_80_side == 'left' and fractal_80_reward == 1:
            outcome = 'good'
            side_chosen = 'left'
            fractal_chosen = 'fractal_80'
            reward = 1
            prac_total_points = prac_total_points + 1
            
        elif key_resp_prac.keys == 'f' and fractal_80_side == 'left' and fractal_80_reward == 0:
            outcome = 'bad'
            side_chosen = 'left'
            fractal_chosen = 'fractal_80'
            reward = 0
            prac_total_points = prac_total_points
        
        elif key_resp_prac.keys == 'j' and fractal_80_side == 'right' and fractal_80_reward == 1:
            outcome = 'good'
            side_chosen = 'right'
            fractal_chosen = 'fractal_80'
            reward = 1
            prac_total_points = prac_total_points + 1
            
        elif key_resp_prac.keys == 'j' and fractal_80_side == 'right' and fractal_80_reward == 0:
            outcome = 'bad'
            side_chosen = 'right'
            fractal_chosen = 'fractal_80'
            reward = 0
            prac_total_points = prac_total_points
            
        else:
            outcome = 'missed'
            side_chosen = 'n/a'
            fractal_chosen = 'n/a'
            reward = 0
            prac_total_points = prac_total_points
            
            
    # add data
    psychoJS.experiment.addData('side_chosen', side_chosen)
    psychoJS.experiment.addData('fractal_chosen', fractal_chosen)
    psychoJS.experiment.addData('reward', reward)
    psychoJS.experiment.addData('total_points', prac_total_points)
    
    
    
    
    
    
    # initialize feedback stim to draw 
    load_feedback_stim_to_draw = []
    
    # draw feedback logic
    if feedback_outcome == 'veridical_feedback' and outcome == 'good' and condition == 1:
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = vertical_feedback_stim
    
    elif feedback_outcome == 'veridical_feedback' and outcome == 'bad' and condition == 1:
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = horizontal_feedback_stim
        
    elif feedback_outcome == 'veridical_feedback' and outcome == 'good' and condition == 2:
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = horizontal_feedback_stim
        
    elif feedback_outcome == 'veridical_feedback' and outcome == 'bad' and condition == 2:
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = vertical_feedback_stim
        
    elif outcome == 'missed':
        decision_to_work_for_feedback = 'missed_trial'
    
    elif feedback_outcome == 'no_feedback':
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = grey_no_feedback_stim
    
    elif feedback_outcome == 'work_option':
        decision_to_work_for_feedback = 'probe'
        load_feedback_stim_to_draw = grey_no_feedback_stim
        
    # initalize empty lists to help branch experiment
    do_not_do_feedback = []
    do_feedback = []
    
    if decision_to_work_for_feedback == 'n/a':
        do_not_do_feedback = 1
        do_feedback = 0
        draw_miss = 0
        
    elif decision_to_work_for_feedback == 'probe':
        do_not_do_feedback = 0
        do_feedback = 1
        draw_miss = 0
        
    elif decision_to_work_for_feedback == 'missed_trial':
        do_not_do_feedback = 0
        do_feedback = 0
        draw_miss = 1
        
    # the Routine "practice_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "isi_screen"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isi_screenComponents = [isi_stim]
    for thisComponent in isi_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isi_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "isi_screen"-------
    while continueRoutine:
        # get current time
        t = isi_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isi_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi_stim* updates
        if isi_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi_stim.frameNStart = frameN  # exact frame index
            isi_stim.tStart = t  # local t and not account for scr refresh
            isi_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi_stim, 'tStartRefresh')  # time at next scr refresh
            isi_stim.setAutoDraw(True)
        if isi_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi_stim.tStartRefresh + isi-frameTolerance:
                # keep track of stop time/frame for later
                isi_stim.tStop = t  # not accounting for scr refresh
                isi_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi_stim, 'tStopRefresh')  # time at next scr refresh
                isi_stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isi_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "isi_screen"-------
    for thisComponent in isi_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_trials.addData('isi_stim.started', isi_stim.tStartRefresh)
    prac_trials.addData('isi_stim.stopped', isi_stim.tStopRefresh)
    # the Routine "isi_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    missed_trial = data.TrialHandler(nReps=draw_miss, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='missed_trial')
    thisExp.addLoop(missed_trial)  # add the loop to the experiment
    thisMissed_trial = missed_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMissed_trial.rgb)
    if thisMissed_trial != None:
        for paramName in thisMissed_trial:
            exec('{} = thisMissed_trial[paramName]'.format(paramName))
    
    for thisMissed_trial in missed_trial:
        currentLoop = missed_trial
        # abbreviate parameter names if possible (e.g. rgb = thisMissed_trial.rgb)
        if thisMissed_trial != None:
            for paramName in thisMissed_trial:
                exec('{} = thisMissed_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "missed_trial_logic"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        missed_trial_logicComponents = [missed_trial_practice]
        for thisComponent in missed_trial_logicComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        missed_trial_logicClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "missed_trial_logic"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = missed_trial_logicClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=missed_trial_logicClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *missed_trial_practice* updates
            if missed_trial_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                missed_trial_practice.frameNStart = frameN  # exact frame index
                missed_trial_practice.tStart = t  # local t and not account for scr refresh
                missed_trial_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(missed_trial_practice, 'tStartRefresh')  # time at next scr refresh
                missed_trial_practice.setAutoDraw(True)
            if missed_trial_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > missed_trial_practice.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    missed_trial_practice.tStop = t  # not accounting for scr refresh
                    missed_trial_practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(missed_trial_practice, 'tStopRefresh')  # time at next scr refresh
                    missed_trial_practice.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in missed_trial_logicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "missed_trial_logic"-------
        for thisComponent in missed_trial_logicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        missed_trial.addData('missed_trial_practice.started', missed_trial_practice.tStartRefresh)
        missed_trial.addData('missed_trial_practice.stopped', missed_trial_practice.tStopRefresh)
        thisExp.nextEntry()
        
    # completed draw_miss repeats of 'missed_trial'
    
    
    # set up handler to look after randomisation of conditions etc
    no_feedback_work_trial = data.TrialHandler(nReps=do_not_do_feedback, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='no_feedback_work_trial')
    thisExp.addLoop(no_feedback_work_trial)  # add the loop to the experiment
    thisNo_feedback_work_trial = no_feedback_work_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNo_feedback_work_trial.rgb)
    if thisNo_feedback_work_trial != None:
        for paramName in thisNo_feedback_work_trial:
            exec('{} = thisNo_feedback_work_trial[paramName]'.format(paramName))
    
    for thisNo_feedback_work_trial in no_feedback_work_trial:
        currentLoop = no_feedback_work_trial
        # abbreviate parameter names if possible (e.g. rgb = thisNo_feedback_work_trial.rgb)
        if thisNo_feedback_work_trial != None:
            for paramName in thisNo_feedback_work_trial:
                exec('{} = thisNo_feedback_work_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "no_feedback_work_logic"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        load_feedback_stim_to_draw.pos = (0,0)
        load_feedback_stim_to_draw.setAutoDraw(True)
        # keep track of which components have finished
        no_feedback_work_logicComponents = [no_feedback_work_image]
        for thisComponent in no_feedback_work_logicComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        no_feedback_work_logicClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "no_feedback_work_logic"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = no_feedback_work_logicClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=no_feedback_work_logicClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *no_feedback_work_image* updates
            if no_feedback_work_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                no_feedback_work_image.frameNStart = frameN  # exact frame index
                no_feedback_work_image.tStart = t  # local t and not account for scr refresh
                no_feedback_work_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no_feedback_work_image, 'tStartRefresh')  # time at next scr refresh
                no_feedback_work_image.setAutoDraw(True)
            if no_feedback_work_image.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    no_feedback_work_image.tStop = t  # not accounting for scr refresh
                    no_feedback_work_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(no_feedback_work_image, 'tStopRefresh')  # time at next scr refresh
                    no_feedback_work_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in no_feedback_work_logicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "no_feedback_work_logic"-------
        for thisComponent in no_feedback_work_logicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        no_feedback_work_trial.addData('no_feedback_work_image.started', no_feedback_work_image.tStartRefresh)
        no_feedback_work_trial.addData('no_feedback_work_image.stopped', no_feedback_work_image.tStopRefresh)
        load_feedback_stim_to_draw.pos = (0,0)
        
        load_feedback_stim_to_draw.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed do_not_do_feedback repeats of 'no_feedback_work_trial'
    
    
    # set up handler to look after randomisation of conditions etc
    feedback_work_trial = data.TrialHandler(nReps=do_feedback, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='feedback_work_trial')
    thisExp.addLoop(feedback_work_trial)  # add the loop to the experiment
    thisFeedback_work_trial = feedback_work_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFeedback_work_trial.rgb)
    if thisFeedback_work_trial != None:
        for paramName in thisFeedback_work_trial:
            exec('{} = thisFeedback_work_trial[paramName]'.format(paramName))
    
    for thisFeedback_work_trial in feedback_work_trial:
        currentLoop = feedback_work_trial
        # abbreviate parameter names if possible (e.g. rgb = thisFeedback_work_trial.rgb)
        if thisFeedback_work_trial != None:
            for paramName in thisFeedback_work_trial:
                exec('{} = thisFeedback_work_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "grey_work_for_fb"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        load_feedback_stim_to_draw.pos = (0,0)
        load_feedback_stim_to_draw.setAutoDraw(True)
        # keep track of which components have finished
        grey_work_for_fbComponents = [grey_stim_work_for_fb]
        for thisComponent in grey_work_for_fbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        grey_work_for_fbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "grey_work_for_fb"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = grey_work_for_fbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=grey_work_for_fbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *grey_stim_work_for_fb* updates
            if grey_stim_work_for_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grey_stim_work_for_fb.frameNStart = frameN  # exact frame index
                grey_stim_work_for_fb.tStart = t  # local t and not account for scr refresh
                grey_stim_work_for_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grey_stim_work_for_fb, 'tStartRefresh')  # time at next scr refresh
                grey_stim_work_for_fb.setAutoDraw(True)
            if grey_stim_work_for_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grey_stim_work_for_fb.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    grey_stim_work_for_fb.tStop = t  # not accounting for scr refresh
                    grey_stim_work_for_fb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(grey_stim_work_for_fb, 'tStopRefresh')  # time at next scr refresh
                    grey_stim_work_for_fb.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in grey_work_for_fbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "grey_work_for_fb"-------
        for thisComponent in grey_work_for_fbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedback_work_trial.addData('grey_stim_work_for_fb.started', grey_stim_work_for_fb.tStartRefresh)
        feedback_work_trial.addData('grey_stim_work_for_fb.stopped', grey_stim_work_for_fb.tStopRefresh)
        load_feedback_stim_to_draw.pos = (0,0)
        load_feedback_stim_to_draw.setAutoDraw(False)
        
        # ------Prepare to start Routine "ask_want_to_work_for_feedback"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        feedback_choice_key_resp.keys = []
        feedback_choice_key_resp.rt = []
        _feedback_choice_key_resp_allKeys = []
        # keep track of which components have finished
        ask_want_to_work_for_feedbackComponents = [feedback_choice_key_resp, feedback_choice_slide]
        for thisComponent in ask_want_to_work_for_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ask_want_to_work_for_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ask_want_to_work_for_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ask_want_to_work_for_feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ask_want_to_work_for_feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_choice_key_resp* updates
            waitOnFlip = False
            if feedback_choice_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_choice_key_resp.frameNStart = frameN  # exact frame index
                feedback_choice_key_resp.tStart = t  # local t and not account for scr refresh
                feedback_choice_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_choice_key_resp, 'tStartRefresh')  # time at next scr refresh
                feedback_choice_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(feedback_choice_key_resp.clock.reset)  # t=0 on next screen flip
            if feedback_choice_key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_choice_key_resp.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_choice_key_resp.tStop = t  # not accounting for scr refresh
                    feedback_choice_key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_choice_key_resp, 'tStopRefresh')  # time at next scr refresh
                    feedback_choice_key_resp.status = FINISHED
            if feedback_choice_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = feedback_choice_key_resp.getKeys(keyList=['o', 'w'], waitRelease=False)
                _feedback_choice_key_resp_allKeys.extend(theseKeys)
                if len(_feedback_choice_key_resp_allKeys):
                    feedback_choice_key_resp.keys = _feedback_choice_key_resp_allKeys[-1].name  # just the last key pressed
                    feedback_choice_key_resp.rt = _feedback_choice_key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *feedback_choice_slide* updates
            if feedback_choice_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_choice_slide.frameNStart = frameN  # exact frame index
                feedback_choice_slide.tStart = t  # local t and not account for scr refresh
                feedback_choice_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_choice_slide, 'tStartRefresh')  # time at next scr refresh
                feedback_choice_slide.setAutoDraw(True)
            if feedback_choice_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_choice_slide.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_choice_slide.tStop = t  # not accounting for scr refresh
                    feedback_choice_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_choice_slide, 'tStopRefresh')  # time at next scr refresh
                    feedback_choice_slide.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ask_want_to_work_for_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ask_want_to_work_for_feedback"-------
        for thisComponent in ask_want_to_work_for_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if feedback_choice_key_resp.keys in ['', [], None]:  # No response was made
            feedback_choice_key_resp.keys = None
        feedback_work_trial.addData('feedback_choice_key_resp.keys',feedback_choice_key_resp.keys)
        if feedback_choice_key_resp.keys != None:  # we had a response
            feedback_work_trial.addData('feedback_choice_key_resp.rt', feedback_choice_key_resp.rt)
        feedback_work_trial.addData('feedback_choice_key_resp.started', feedback_choice_key_resp.tStartRefresh)
        feedback_work_trial.addData('feedback_choice_key_resp.stopped', feedback_choice_key_resp.tStopRefresh)
        feedback_work_trial.addData('feedback_choice_slide.started', feedback_choice_slide.tStartRefresh)
        feedback_work_trial.addData('feedback_choice_slide.stopped', feedback_choice_slide.tStopRefresh)
        # intialize empty lists to branch experiment
        highlight_no = []
        highlight_yes = []
        
        # decide if we should draw yes or no highlighted slide
        if feedback_choice_key_resp.keys == 'w':     
            decision_to_work_for_feedback = 'yes'
            highlight_no = 0
            highlight_yes = 1
                
        elif feedback_choice_key_resp.keys == 'o':
            decision_to_work_for_feedback = 'no'       
            highlight_no = 1
            highlight_yes = 0
            
        else:
            decision_to_work_for_feedback = 'missed'       
            highlight_no = 0
            highlight_yes = 0
        
        # set up handler to look after randomisation of conditions etc
        no_loop_highlight = data.TrialHandler(nReps=highlight_no, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='no_loop_highlight')
        thisExp.addLoop(no_loop_highlight)  # add the loop to the experiment
        thisNo_loop_highlight = no_loop_highlight.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisNo_loop_highlight.rgb)
        if thisNo_loop_highlight != None:
            for paramName in thisNo_loop_highlight:
                exec('{} = thisNo_loop_highlight[paramName]'.format(paramName))
        
        for thisNo_loop_highlight in no_loop_highlight:
            currentLoop = no_loop_highlight
            # abbreviate parameter names if possible (e.g. rgb = thisNo_loop_highlight.rgb)
            if thisNo_loop_highlight != None:
                for paramName in thisNo_loop_highlight:
                    exec('{} = thisNo_loop_highlight[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "no_fb_highlight"-------
            continueRoutine = True
            routineTimer.add(0.300000)
            # update component parameters for each repeat
            # keep track of which components have finished
            no_fb_highlightComponents = [no_fb_slide]
            for thisComponent in no_fb_highlightComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            no_fb_highlightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "no_fb_highlight"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = no_fb_highlightClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=no_fb_highlightClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *no_fb_slide* updates
                if no_fb_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    no_fb_slide.frameNStart = frameN  # exact frame index
                    no_fb_slide.tStart = t  # local t and not account for scr refresh
                    no_fb_slide.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(no_fb_slide, 'tStartRefresh')  # time at next scr refresh
                    no_fb_slide.setAutoDraw(True)
                if no_fb_slide.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > .3-frameTolerance:
                        # keep track of stop time/frame for later
                        no_fb_slide.tStop = t  # not accounting for scr refresh
                        no_fb_slide.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(no_fb_slide, 'tStopRefresh')  # time at next scr refresh
                        no_fb_slide.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in no_fb_highlightComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "no_fb_highlight"-------
            for thisComponent in no_fb_highlightComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            no_loop_highlight.addData('no_fb_slide.started', no_fb_slide.tStartRefresh)
            no_loop_highlight.addData('no_fb_slide.stopped', no_fb_slide.tStopRefresh)
            thisExp.nextEntry()
            
        # completed highlight_no repeats of 'no_loop_highlight'
        
        
        # set up handler to look after randomisation of conditions etc
        yes_loop_highlight = data.TrialHandler(nReps=highlight_yes, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='yes_loop_highlight')
        thisExp.addLoop(yes_loop_highlight)  # add the loop to the experiment
        thisYes_loop_highlight = yes_loop_highlight.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisYes_loop_highlight.rgb)
        if thisYes_loop_highlight != None:
            for paramName in thisYes_loop_highlight:
                exec('{} = thisYes_loop_highlight[paramName]'.format(paramName))
        
        for thisYes_loop_highlight in yes_loop_highlight:
            currentLoop = yes_loop_highlight
            # abbreviate parameter names if possible (e.g. rgb = thisYes_loop_highlight.rgb)
            if thisYes_loop_highlight != None:
                for paramName in thisYes_loop_highlight:
                    exec('{} = thisYes_loop_highlight[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "yes_fb_highlight"-------
            continueRoutine = True
            routineTimer.add(0.300000)
            # update component parameters for each repeat
            # keep track of which components have finished
            yes_fb_highlightComponents = [yes_fb_slide]
            for thisComponent in yes_fb_highlightComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            yes_fb_highlightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "yes_fb_highlight"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = yes_fb_highlightClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=yes_fb_highlightClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *yes_fb_slide* updates
                if yes_fb_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    yes_fb_slide.frameNStart = frameN  # exact frame index
                    yes_fb_slide.tStart = t  # local t and not account for scr refresh
                    yes_fb_slide.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(yes_fb_slide, 'tStartRefresh')  # time at next scr refresh
                    yes_fb_slide.setAutoDraw(True)
                if yes_fb_slide.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > .3-frameTolerance:
                        # keep track of stop time/frame for later
                        yes_fb_slide.tStop = t  # not accounting for scr refresh
                        yes_fb_slide.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(yes_fb_slide, 'tStopRefresh')  # time at next scr refresh
                        yes_fb_slide.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in yes_fb_highlightComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "yes_fb_highlight"-------
            for thisComponent in yes_fb_highlightComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            yes_loop_highlight.addData('yes_fb_slide.started', yes_fb_slide.tStartRefresh)
            yes_loop_highlight.addData('yes_fb_slide.stopped', yes_fb_slide.tStopRefresh)
            
            # ------Prepare to start Routine "fb_work_time"-------
            continueRoutine = True
            # update component parameters for each repeat
            # lets set the stim to draw for feedback contingent on condition and outcome
            feedback_stim_to_draw = []
            
            # in condition 1, the vertical stim means reward
            if condition == 1:
                
                if outcome == 'good':
                    feedback_stim_to_draw = vertical_feedback_stim
                    
                elif outcome == 'bad':
                    feedback_stim_to_draw = horizontal_feedback_stim
                    
            # in condition 2, the horizontal stim means reward
            elif condition == 2:
                
                if outcome == 'good':
                    feedback_stim_to_draw = horizontal_feedback_stim
                    
                elif outcome == 'bad':
                    feedback_stim_to_draw = vertical_feedback_stim
            # keep track of which components have finished
            fb_work_timeComponents = []
            for thisComponent in fb_work_timeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            fb_work_timeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "fb_work_time"-------
            while continueRoutine:
                # get current time
                t = fb_work_timeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=fb_work_timeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fb_work_timeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "fb_work_time"-------
            for thisComponent in fb_work_timeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "fb_work_time" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "draw_feedback_to_screen"-------
            continueRoutine = True
            routineTimer.add(3.000000)
            # update component parameters for each repeat
            feedback_stim_to_draw.pos = (0,0)
            grey_no_feedback_stim.pos = (0,0)
            
            feedback_stim_to_draw.opacity = 1
            grey_no_feedback_stim.opacity = 1
            
            update_opacity = .0150
            
            time_of_press = []
            time_of_press_list = []
            
            work_total_presses = 0
            
            current_work_rate = []
            current_work_rate_list = []
            
            current_opacity_level_list = []
            final_opacity_level = []
            
            event.clearEvents()
            work_for_feedback_space_bar_press.keys = []
            work_for_feedback_space_bar_press.rt = []
            _work_for_feedback_space_bar_press_allKeys = []
            # keep track of which components have finished
            draw_feedback_to_screenComponents = [work_for_feedback_space_bar_press]
            for thisComponent in draw_feedback_to_screenComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            draw_feedback_to_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "draw_feedback_to_screen"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = draw_feedback_to_screenClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=draw_feedback_to_screenClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                feedback_stim_to_draw.setAutoDraw(True)
                grey_no_feedback_stim.setAutoDraw(True)
                
                keys = psychoJS.eventManager.getKeys();
                if 'space' in keys and draw_feedback_to_screenClock.getTime() < 3.0:
                #if 'space' in keys:
                    
                    time_of_press = draw_feedback_to_screenClock.getTime()
                    time_of_press_list.push(time_of_press)
                    work_total_presses = work_total_presses + 1
                    current_work_rate = work_total_presses / time_of_press
                    current_opacity_level_list.push(grey_no_feedback_stim.opacity)
                    
                    if current_work_rate > final_work_for_feedback_threshold:
                        
                        grey_no_feedback_stim.opacity = grey_no_feedback_stim.opacity - update_opacity
                
                # *work_for_feedback_space_bar_press* updates
                waitOnFlip = False
                if work_for_feedback_space_bar_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    work_for_feedback_space_bar_press.frameNStart = frameN  # exact frame index
                    work_for_feedback_space_bar_press.tStart = t  # local t and not account for scr refresh
                    work_for_feedback_space_bar_press.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(work_for_feedback_space_bar_press, 'tStartRefresh')  # time at next scr refresh
                    work_for_feedback_space_bar_press.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(work_for_feedback_space_bar_press.clock.reset)  # t=0 on next screen flip
                if work_for_feedback_space_bar_press.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 3.0-frameTolerance:
                        # keep track of stop time/frame for later
                        work_for_feedback_space_bar_press.tStop = t  # not accounting for scr refresh
                        work_for_feedback_space_bar_press.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(work_for_feedback_space_bar_press, 'tStopRefresh')  # time at next scr refresh
                        work_for_feedback_space_bar_press.status = FINISHED
                if work_for_feedback_space_bar_press.status == STARTED and not waitOnFlip:
                    theseKeys = work_for_feedback_space_bar_press.getKeys(keyList=['e'], waitRelease=False)
                    _work_for_feedback_space_bar_press_allKeys.extend(theseKeys)
                    if len(_work_for_feedback_space_bar_press_allKeys):
                        work_for_feedback_space_bar_press.keys = _work_for_feedback_space_bar_press_allKeys[-1].name  # just the last key pressed
                        work_for_feedback_space_bar_press.rt = _work_for_feedback_space_bar_press_allKeys[-1].rt
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in draw_feedback_to_screenComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "draw_feedback_to_screen"-------
            for thisComponent in draw_feedback_to_screenComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            feedback_stim_to_draw.setAutoDraw(False)
            grey_no_feedback_stim.setAutoDraw(False)
            final_opacity_level = grey_no_feedback_stim.opacity
            
            event.clearEvents()
            
            # ------Prepare to start Routine "post_work_blank"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            post_work_space_presses.keys = []
            post_work_space_presses.rt = []
            _post_work_space_presses_allKeys = []
            # keep track of which components have finished
            post_work_blankComponents = [blank_image, post_work_space_presses]
            for thisComponent in post_work_blankComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            post_work_blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "post_work_blank"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = post_work_blankClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=post_work_blankClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank_image* updates
                if blank_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blank_image.frameNStart = frameN  # exact frame index
                    blank_image.tStart = t  # local t and not account for scr refresh
                    blank_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blank_image, 'tStartRefresh')  # time at next scr refresh
                    blank_image.setAutoDraw(True)
                if blank_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blank_image.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        blank_image.tStop = t  # not accounting for scr refresh
                        blank_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(blank_image, 'tStopRefresh')  # time at next scr refresh
                        blank_image.setAutoDraw(False)
                
                # *post_work_space_presses* updates
                waitOnFlip = False
                if post_work_space_presses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    post_work_space_presses.frameNStart = frameN  # exact frame index
                    post_work_space_presses.tStart = t  # local t and not account for scr refresh
                    post_work_space_presses.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(post_work_space_presses, 'tStartRefresh')  # time at next scr refresh
                    post_work_space_presses.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(post_work_space_presses.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(post_work_space_presses.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if post_work_space_presses.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        post_work_space_presses.tStop = t  # not accounting for scr refresh
                        post_work_space_presses.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(post_work_space_presses, 'tStopRefresh')  # time at next scr refresh
                        post_work_space_presses.status = FINISHED
                if post_work_space_presses.status == STARTED and not waitOnFlip:
                    theseKeys = post_work_space_presses.getKeys(keyList=['space'], waitRelease=False)
                    _post_work_space_presses_allKeys.extend(theseKeys)
                    if len(_post_work_space_presses_allKeys):
                        post_work_space_presses.keys = [key.name for key in _post_work_space_presses_allKeys]  # storing all keys
                        post_work_space_presses.rt = [key.rt for key in _post_work_space_presses_allKeys]
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in post_work_blankComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "post_work_blank"-------
            for thisComponent in post_work_blankComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            yes_loop_highlight.addData('blank_image.started', blank_image.tStartRefresh)
            yes_loop_highlight.addData('blank_image.stopped', blank_image.tStopRefresh)
            # check responses
            if post_work_space_presses.keys in ['', [], None]:  # No response was made
                post_work_space_presses.keys = None
            yes_loop_highlight.addData('post_work_space_presses.keys',post_work_space_presses.keys)
            if post_work_space_presses.keys != None:  # we had a response
                yes_loop_highlight.addData('post_work_space_presses.rt', post_work_space_presses.rt)
            yes_loop_highlight.addData('post_work_space_presses.started', post_work_space_presses.tStartRefresh)
            yes_loop_highlight.addData('post_work_space_presses.stopped', post_work_space_presses.tStopRefresh)
            thisExp.nextEntry()
            
        # completed highlight_yes repeats of 'yes_loop_highlight'
        
        thisExp.nextEntry()
        
    # completed do_feedback repeats of 'feedback_work_trial'
    
    
    # ------Prepare to start Routine "end_loop_data_log"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    end_loop_data_logComponents = []
    for thisComponent in end_loop_data_logComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_loop_data_logClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_loop_data_log"-------
    while continueRoutine:
        # get current time
        t = end_loop_data_logClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_loop_data_logClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_loop_data_logComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_loop_data_log"-------
    for thisComponent in end_loop_data_logComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # add data
    psychoJS.experiment.addData('decision_to_work_for_feedback', decision_to_work_for_feedback)
    psychoJS.experiment.addData('time_of_press_list', time_of_press_list)
    psychoJS.experiment.addData('work_total_presses', work_total_presses)
    psychoJS.experiment.addData('current_work_rate_list', current_work_rate_list)
    psychoJS.experiment.addData('current_opacity_level_list', current_opacity_level_list)
    psychoJS.experiment.addData('final_opacity_level', final_opacity_level)
    
    # the Routine "end_loop_data_log" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'prac_trials'


# ------Prepare to start Routine "blank_screen_2"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
blank_screen_2Components = [blank_slide_2]
for thisComponent in blank_screen_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank_screen_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank_screen_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank_screen_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank_screen_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank_slide_2* updates
    if blank_slide_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank_slide_2.frameNStart = frameN  # exact frame index
        blank_slide_2.tStart = t  # local t and not account for scr refresh
        blank_slide_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_slide_2, 'tStartRefresh')  # time at next scr refresh
        blank_slide_2.setAutoDraw(True)
    if blank_slide_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_slide_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            blank_slide_2.tStop = t  # not accounting for scr refresh
            blank_slide_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank_slide_2, 'tStopRefresh')  # time at next scr refresh
            blank_slide_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank_screen_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank_screen_2"-------
for thisComponent in blank_screen_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blank_slide_2.started', blank_slide_2.tStartRefresh)
thisExp.addData('blank_slide_2.stopped', blank_slide_2.tStopRefresh)

# ------Prepare to start Routine "second_quiz"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_thirteen.setAutoDraw(True)
start_second_quiz.keys = []
start_second_quiz.rt = []
_start_second_quiz_allKeys = []
# keep track of which components have finished
second_quizComponents = [start_second_quiz]
for thisComponent in second_quizComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
second_quizClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "second_quiz"-------
while continueRoutine:
    # get current time
    t = second_quizClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=second_quizClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_second_quiz* updates
    waitOnFlip = False
    if start_second_quiz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_second_quiz.frameNStart = frameN  # exact frame index
        start_second_quiz.tStart = t  # local t and not account for scr refresh
        start_second_quiz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_second_quiz, 'tStartRefresh')  # time at next scr refresh
        start_second_quiz.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_second_quiz.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_second_quiz.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_second_quiz.status == STARTED and not waitOnFlip:
        theseKeys = start_second_quiz.getKeys(keyList=None, waitRelease=False)
        _start_second_quiz_allKeys.extend(theseKeys)
        if len(_start_second_quiz_allKeys):
            start_second_quiz.keys = _start_second_quiz_allKeys[-1].name  # just the last key pressed
            start_second_quiz.rt = _start_second_quiz_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in second_quizComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "second_quiz"-------
for thisComponent in second_quizComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_thirteen.setAutoDraw(False)
# check responses
if start_second_quiz.keys in ['', [], None]:  # No response was made
    start_second_quiz.keys = None
thisExp.addData('start_second_quiz.keys',start_second_quiz.keys)
if start_second_quiz.keys != None:  # we had a response
    thisExp.addData('start_second_quiz.rt', start_second_quiz.rt)
thisExp.addData('start_second_quiz.started', start_second_quiz.tStartRefresh)
thisExp.addData('start_second_quiz.stopped', start_second_quiz.tStopRefresh)
thisExp.nextEntry()
# the Routine "second_quiz" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "second_quiz_first_question"-------
continueRoutine = True
# update component parameters for each repeat
grey_no_feedback_stim.pos = [0, 0.12]
grey_no_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(True)
grey_no_feedback_stim.setAutoDraw(True) # draw grey stim
first_q_second_quiz_resp.keys = []
first_q_second_quiz_resp.rt = []
_first_q_second_quiz_resp_allKeys = []
# keep track of which components have finished
second_quiz_first_questionComponents = [first_q_second_quiz_resp]
for thisComponent in second_quiz_first_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
second_quiz_first_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "second_quiz_first_question"-------
while continueRoutine:
    # get current time
    t = second_quiz_first_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=second_quiz_first_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *first_q_second_quiz_resp* updates
    waitOnFlip = False
    if first_q_second_quiz_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        first_q_second_quiz_resp.frameNStart = frameN  # exact frame index
        first_q_second_quiz_resp.tStart = t  # local t and not account for scr refresh
        first_q_second_quiz_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(first_q_second_quiz_resp, 'tStartRefresh')  # time at next scr refresh
        first_q_second_quiz_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(first_q_second_quiz_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(first_q_second_quiz_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if first_q_second_quiz_resp.status == STARTED and not waitOnFlip:
        theseKeys = first_q_second_quiz_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _first_q_second_quiz_resp_allKeys.extend(theseKeys)
        if len(_first_q_second_quiz_resp_allKeys):
            first_q_second_quiz_resp.keys = _first_q_second_quiz_resp_allKeys[-1].name  # just the last key pressed
            first_q_second_quiz_resp.rt = _first_q_second_quiz_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in second_quiz_first_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "second_quiz_first_question"-------
for thisComponent in second_quiz_first_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if first_q_second_quiz_resp.keys == '1':   # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_first_question_result = 'incorrect'
        
elif first_q_second_quiz_resp.keys == '2': # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_first_question_result = 'incorrect'
        
elif first_q_second_quiz_resp.keys == '3': # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    second_stim_quiz_first_question_result = 'correct'

grey_no_feedback_stim.pos = [0, 0.12]
grey_no_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(False)
grey_no_feedback_stim.setAutoDraw(False) # draw grey stim
# check responses
if first_q_second_quiz_resp.keys in ['', [], None]:  # No response was made
    first_q_second_quiz_resp.keys = None
thisExp.addData('first_q_second_quiz_resp.keys',first_q_second_quiz_resp.keys)
if first_q_second_quiz_resp.keys != None:  # we had a response
    thisExp.addData('first_q_second_quiz_resp.rt', first_q_second_quiz_resp.rt)
thisExp.addData('first_q_second_quiz_resp.started', first_q_second_quiz_resp.tStartRefresh)
thisExp.addData('first_q_second_quiz_resp.stopped', first_q_second_quiz_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "second_quiz_first_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "second_quiz_first_question_reminder"-------
continueRoutine = True
# update component parameters for each repeat
if second_stim_quiz_first_question_result == 'correct':
    
    grey_no_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.size = (0.10, 0.10)

    correct_result_no_feedback.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True) # draw grey stim
    
elif second_stim_quiz_first_question_result == 'incorrect':

    grey_no_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.size = (0.10, 0.10)

    incorrect_result_no_feedback.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True) # draw grey stim
advance_q_2_quiz_2.keys = []
advance_q_2_quiz_2.rt = []
_advance_q_2_quiz_2_allKeys = []
# keep track of which components have finished
second_quiz_first_question_reminderComponents = [advance_q_2_quiz_2]
for thisComponent in second_quiz_first_question_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
second_quiz_first_question_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "second_quiz_first_question_reminder"-------
while continueRoutine:
    # get current time
    t = second_quiz_first_question_reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=second_quiz_first_question_reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *advance_q_2_quiz_2* updates
    waitOnFlip = False
    if advance_q_2_quiz_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        advance_q_2_quiz_2.frameNStart = frameN  # exact frame index
        advance_q_2_quiz_2.tStart = t  # local t and not account for scr refresh
        advance_q_2_quiz_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(advance_q_2_quiz_2, 'tStartRefresh')  # time at next scr refresh
        advance_q_2_quiz_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(advance_q_2_quiz_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(advance_q_2_quiz_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if advance_q_2_quiz_2.status == STARTED and not waitOnFlip:
        theseKeys = advance_q_2_quiz_2.getKeys(keyList=None, waitRelease=False)
        _advance_q_2_quiz_2_allKeys.extend(theseKeys)
        if len(_advance_q_2_quiz_2_allKeys):
            advance_q_2_quiz_2.keys = _advance_q_2_quiz_2_allKeys[-1].name  # just the last key pressed
            advance_q_2_quiz_2.rt = _advance_q_2_quiz_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in second_quiz_first_question_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "second_quiz_first_question_reminder"-------
for thisComponent in second_quiz_first_question_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if second_stim_quiz_first_question_result == 'correct':
    
    grey_no_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.size = (0.10, 0.10)

    correct_result_no_feedback.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False) # draw grey stim
    
elif second_stim_quiz_first_question_result == 'incorrect':

    grey_no_feedback_stim.pos = [0, 0.12]
    grey_no_feedback_stim.size = (0.10, 0.10)

    incorrect_result_no_feedback.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False) # draw grey stim
# check responses
if advance_q_2_quiz_2.keys in ['', [], None]:  # No response was made
    advance_q_2_quiz_2.keys = None
thisExp.addData('advance_q_2_quiz_2.keys',advance_q_2_quiz_2.keys)
if advance_q_2_quiz_2.keys != None:  # we had a response
    thisExp.addData('advance_q_2_quiz_2.rt', advance_q_2_quiz_2.rt)
thisExp.addData('advance_q_2_quiz_2.started', advance_q_2_quiz_2.tStartRefresh)
thisExp.addData('advance_q_2_quiz_2.stopped', advance_q_2_quiz_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "second_quiz_first_question_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "second_quiz_second_question"-------
continueRoutine = True
# update component parameters for each repeat
vertical_feedback_stim.pos = [0, 0.12]
vertical_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(True)
vertical_feedback_stim.setAutoDraw(True) # draw vertical stim
resp_q_2_q_2.keys = []
resp_q_2_q_2.rt = []
_resp_q_2_q_2_allKeys = []
# keep track of which components have finished
second_quiz_second_questionComponents = [resp_q_2_q_2]
for thisComponent in second_quiz_second_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
second_quiz_second_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "second_quiz_second_question"-------
while continueRoutine:
    # get current time
    t = second_quiz_second_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=second_quiz_second_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resp_q_2_q_2* updates
    waitOnFlip = False
    if resp_q_2_q_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_q_2_q_2.frameNStart = frameN  # exact frame index
        resp_q_2_q_2.tStart = t  # local t and not account for scr refresh
        resp_q_2_q_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_q_2_q_2, 'tStartRefresh')  # time at next scr refresh
        resp_q_2_q_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_q_2_q_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_q_2_q_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_q_2_q_2.status == STARTED and not waitOnFlip:
        theseKeys = resp_q_2_q_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _resp_q_2_q_2_allKeys.extend(theseKeys)
        if len(_resp_q_2_q_2_allKeys):
            resp_q_2_q_2.keys = _resp_q_2_q_2_allKeys[-1].name  # just the last key pressed
            resp_q_2_q_2.rt = _resp_q_2_q_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in second_quiz_second_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "second_quiz_second_question"-------
for thisComponent in second_quiz_second_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if resp_q_2_q_2.keys == '1' and condition == 1:   # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    second_stim_quiz_second_question_result = 'correct'
        
elif resp_q_2_q_2.keys == '2' and condition == 1: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_second_question_result = 'incorrect'
        
elif resp_q_2_q_2.keys == '3' and condition == 1: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_second_question_result = 'incorrect'
    
elif resp_q_2_q_2.keys == '1' and condition == 2: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_second_question_result = 'incorrect'
        
elif resp_q_2_q_2.keys == '2' and condition == 2: # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    second_stim_quiz_second_question_result = 'correct'
        
elif resp_q_2_q_2.keys == '3' and condition == 2: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_second_question_result = 'incorrect'

vertical_feedback_stim.pos = [0, 0.12]
vertical_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(False)
vertical_feedback_stim.setAutoDraw(False) # draw vertical stim
# check responses
if resp_q_2_q_2.keys in ['', [], None]:  # No response was made
    resp_q_2_q_2.keys = None
thisExp.addData('resp_q_2_q_2.keys',resp_q_2_q_2.keys)
if resp_q_2_q_2.keys != None:  # we had a response
    thisExp.addData('resp_q_2_q_2.rt', resp_q_2_q_2.rt)
thisExp.addData('resp_q_2_q_2.started', resp_q_2_q_2.tStartRefresh)
thisExp.addData('resp_q_2_q_2.stopped', resp_q_2_q_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "second_quiz_second_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "second_quiz_second_question_reminder"-------
continueRoutine = True
# update component parameters for each repeat
if second_stim_quiz_second_question_result == 'correct' and condition == 1:
    
    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_one.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True) # draw vertical stim
    
elif second_stim_quiz_second_question_result == 'incorrect' and condition == 1:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)
    
    incorrect_result_plus_one.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True) # draw vertical stim

elif second_stim_quiz_second_question_result == 'correct' and condition == 2:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_zero.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True) # draw vertical stim

elif second_stim_quiz_second_question_result == 'incorrect' and condition == 2:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_zero.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True) # draw vertical stim
advance_q_3_quiz_2.keys = []
advance_q_3_quiz_2.rt = []
_advance_q_3_quiz_2_allKeys = []
# keep track of which components have finished
second_quiz_second_question_reminderComponents = [advance_q_3_quiz_2]
for thisComponent in second_quiz_second_question_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
second_quiz_second_question_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "second_quiz_second_question_reminder"-------
while continueRoutine:
    # get current time
    t = second_quiz_second_question_reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=second_quiz_second_question_reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *advance_q_3_quiz_2* updates
    waitOnFlip = False
    if advance_q_3_quiz_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        advance_q_3_quiz_2.frameNStart = frameN  # exact frame index
        advance_q_3_quiz_2.tStart = t  # local t and not account for scr refresh
        advance_q_3_quiz_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(advance_q_3_quiz_2, 'tStartRefresh')  # time at next scr refresh
        advance_q_3_quiz_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(advance_q_3_quiz_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(advance_q_3_quiz_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if advance_q_3_quiz_2.status == STARTED and not waitOnFlip:
        theseKeys = advance_q_3_quiz_2.getKeys(keyList=None, waitRelease=False)
        _advance_q_3_quiz_2_allKeys.extend(theseKeys)
        if len(_advance_q_3_quiz_2_allKeys):
            advance_q_3_quiz_2.keys = _advance_q_3_quiz_2_allKeys[-1].name  # just the last key pressed
            advance_q_3_quiz_2.rt = _advance_q_3_quiz_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in second_quiz_second_question_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "second_quiz_second_question_reminder"-------
for thisComponent in second_quiz_second_question_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if second_stim_quiz_second_question_result == 'correct' and condition == 1:
    
    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_one.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False) # draw vertical stim
    
elif second_stim_quiz_second_question_result == 'incorrect' and condition == 1:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)
    
    incorrect_result_plus_one.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False) # draw vertical stim

elif second_stim_quiz_second_question_result == 'correct' and condition == 2:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_zero.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False) # draw vertical stim

elif second_stim_quiz_second_question_result == 'incorrect' and condition == 2:

    vertical_feedback_stim.pos = [0, 0.12]
    vertical_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_zero.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False) # draw vertical stim
# check responses
if advance_q_3_quiz_2.keys in ['', [], None]:  # No response was made
    advance_q_3_quiz_2.keys = None
thisExp.addData('advance_q_3_quiz_2.keys',advance_q_3_quiz_2.keys)
if advance_q_3_quiz_2.keys != None:  # we had a response
    thisExp.addData('advance_q_3_quiz_2.rt', advance_q_3_quiz_2.rt)
thisExp.addData('advance_q_3_quiz_2.started', advance_q_3_quiz_2.tStartRefresh)
thisExp.addData('advance_q_3_quiz_2.stopped', advance_q_3_quiz_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "second_quiz_second_question_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "second_quiz_third_question"-------
continueRoutine = True
# update component parameters for each repeat
horizontal_feedback_stim.pos = [0, 0.12]
horizontal_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(True)
horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim
resp_quiz_2_q_3.keys = []
resp_quiz_2_q_3.rt = []
_resp_quiz_2_q_3_allKeys = []
# keep track of which components have finished
second_quiz_third_questionComponents = [resp_quiz_2_q_3]
for thisComponent in second_quiz_third_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
second_quiz_third_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "second_quiz_third_question"-------
while continueRoutine:
    # get current time
    t = second_quiz_third_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=second_quiz_third_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resp_quiz_2_q_3* updates
    waitOnFlip = False
    if resp_quiz_2_q_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_quiz_2_q_3.frameNStart = frameN  # exact frame index
        resp_quiz_2_q_3.tStart = t  # local t and not account for scr refresh
        resp_quiz_2_q_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_quiz_2_q_3, 'tStartRefresh')  # time at next scr refresh
        resp_quiz_2_q_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_quiz_2_q_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_quiz_2_q_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_quiz_2_q_3.status == STARTED and not waitOnFlip:
        theseKeys = resp_quiz_2_q_3.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _resp_quiz_2_q_3_allKeys.extend(theseKeys)
        if len(_resp_quiz_2_q_3_allKeys):
            resp_quiz_2_q_3.keys = _resp_quiz_2_q_3_allKeys[-1].name  # just the last key pressed
            resp_quiz_2_q_3.rt = _resp_quiz_2_q_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in second_quiz_third_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "second_quiz_third_question"-------
for thisComponent in second_quiz_third_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if resp_quiz_2_q_3.keys == '1' and condition == 1:   # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_third_question_resultt = 'incorrect'
        
elif resp_quiz_2_q_3.keys == '2' and condition == 1: # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    second_stim_quiz_third_question_result = 'correct'
        
elif resp_quiz_2_q_3.keys == '3' and condition == 1: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_third_question_result = 'incorrect'
    
elif resp_quiz_2_q_3.keys == '1' and condition == 2: # correct
    quiz_and_attention_check_fails = quiz_and_attention_check_fails
    second_stim_quiz_third_question_result = 'correct'
        
elif resp_quiz_2_q_3.keys == '2' and condition == 2: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_third_question_result = 'incorrect'
        
elif resp_quiz_2_q_3.keys == '3' and condition == 2: # incorrect
    quiz_and_attention_check_fails = quiz_and_attention_check_fails + 1
    second_stim_quiz_third_question_result = 'incorrect'
    
horizontal_feedback_stim.pos = [0, 0.12]
horizontal_feedback_stim.size = (0.10, 0.10)

instructions_slide_six.setAutoDraw(False)
horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim
# check responses
if resp_quiz_2_q_3.keys in ['', [], None]:  # No response was made
    resp_quiz_2_q_3.keys = None
thisExp.addData('resp_quiz_2_q_3.keys',resp_quiz_2_q_3.keys)
if resp_quiz_2_q_3.keys != None:  # we had a response
    thisExp.addData('resp_quiz_2_q_3.rt', resp_quiz_2_q_3.rt)
thisExp.addData('resp_quiz_2_q_3.started', resp_quiz_2_q_3.tStartRefresh)
thisExp.addData('resp_quiz_2_q_3.stopped', resp_quiz_2_q_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "second_quiz_third_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "second_quiz_third_question_reminder"-------
continueRoutine = True
# update component parameters for each repeat
#reminder
if second_stim_quiz_third_question_result == 'correct' and condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_zero.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim
    
elif second_stim_quiz_third_question_result == 'incorrect' and condition == 1:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_zero.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim

elif second_stim_quiz_third_question_result == 'correct' and condition == 2:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_one.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim

elif second_stim_quiz_third_question_result == 'incorrect' and condition == 2:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_one.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True) # draw horizontal stim
advance_from_second_quiz.keys = []
advance_from_second_quiz.rt = []
_advance_from_second_quiz_allKeys = []
# keep track of which components have finished
second_quiz_third_question_reminderComponents = [advance_from_second_quiz]
for thisComponent in second_quiz_third_question_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
second_quiz_third_question_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "second_quiz_third_question_reminder"-------
while continueRoutine:
    # get current time
    t = second_quiz_third_question_reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=second_quiz_third_question_reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *advance_from_second_quiz* updates
    waitOnFlip = False
    if advance_from_second_quiz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        advance_from_second_quiz.frameNStart = frameN  # exact frame index
        advance_from_second_quiz.tStart = t  # local t and not account for scr refresh
        advance_from_second_quiz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(advance_from_second_quiz, 'tStartRefresh')  # time at next scr refresh
        advance_from_second_quiz.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(advance_from_second_quiz.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(advance_from_second_quiz.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if advance_from_second_quiz.status == STARTED and not waitOnFlip:
        theseKeys = advance_from_second_quiz.getKeys(keyList=None, waitRelease=False)
        _advance_from_second_quiz_allKeys.extend(theseKeys)
        if len(_advance_from_second_quiz_allKeys):
            advance_from_second_quiz.keys = _advance_from_second_quiz_allKeys[-1].name  # just the last key pressed
            advance_from_second_quiz.rt = _advance_from_second_quiz_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in second_quiz_third_question_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "second_quiz_third_question_reminder"-------
for thisComponent in second_quiz_third_question_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#reminder
if second_stim_quiz_third_question_result == 'correct' and condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_zero.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim
    
elif second_stim_quiz_third_question_result == 'incorrect' and condition == 1:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_zero.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim

elif second_stim_quiz_third_question_result == 'correct' and condition == 2:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    correct_result_plus_one.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim

elif second_stim_quiz_third_question_result == 'incorrect' and condition == 2:

    horizontal_feedback_stim.pos = [0, 0.12]
    horizontal_feedback_stim.size = (0.10, 0.10)

    incorrect_result_plus_one.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False) # draw horizontal stim
# check responses
if advance_from_second_quiz.keys in ['', [], None]:  # No response was made
    advance_from_second_quiz.keys = None
thisExp.addData('advance_from_second_quiz.keys',advance_from_second_quiz.keys)
if advance_from_second_quiz.keys != None:  # we had a response
    thisExp.addData('advance_from_second_quiz.rt', advance_from_second_quiz.rt)
thisExp.addData('advance_from_second_quiz.started', advance_from_second_quiz.tStartRefresh)
thisExp.addData('advance_from_second_quiz.stopped', advance_from_second_quiz.tStopRefresh)
thisExp.nextEntry()
# the Routine "second_quiz_third_question_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "last_stim_reminder"-------
continueRoutine = True
# update component parameters for each repeat
advance_from_last_reminder.keys = []
advance_from_last_reminder.rt = []
_advance_from_last_reminder_allKeys = []
# draw another reminder
if condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.17]
    vertical_feedback_stim.pos = [-.17, 0.17]
    grey_no_feedback_stim.pos = [.17, 0.17]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    result_final_reminder.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True)

# in condition 2, the horizontal stim means reward

elif condition == 2:
    
    horizontal_feedback_stim.pos = [-.17, 0.17]
    vertical_feedback_stim.pos = [0, 0.17]
    grey_no_feedback_stim.pos = [.17, 0.17]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    result_final_reminder.setAutoDraw(True)
    horizontal_feedback_stim.setAutoDraw(True)
    vertical_feedback_stim.setAutoDraw(True)
    grey_no_feedback_stim.setAutoDraw(True)
# keep track of which components have finished
last_stim_reminderComponents = [advance_from_last_reminder]
for thisComponent in last_stim_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
last_stim_reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "last_stim_reminder"-------
while continueRoutine:
    # get current time
    t = last_stim_reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=last_stim_reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *advance_from_last_reminder* updates
    waitOnFlip = False
    if advance_from_last_reminder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        advance_from_last_reminder.frameNStart = frameN  # exact frame index
        advance_from_last_reminder.tStart = t  # local t and not account for scr refresh
        advance_from_last_reminder.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(advance_from_last_reminder, 'tStartRefresh')  # time at next scr refresh
        advance_from_last_reminder.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(advance_from_last_reminder.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(advance_from_last_reminder.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if advance_from_last_reminder.status == STARTED and not waitOnFlip:
        theseKeys = advance_from_last_reminder.getKeys(keyList=None, waitRelease=False)
        _advance_from_last_reminder_allKeys.extend(theseKeys)
        if len(_advance_from_last_reminder_allKeys):
            advance_from_last_reminder.keys = _advance_from_last_reminder_allKeys[-1].name  # just the last key pressed
            advance_from_last_reminder.rt = _advance_from_last_reminder_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in last_stim_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "last_stim_reminder"-------
for thisComponent in last_stim_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if advance_from_last_reminder.keys in ['', [], None]:  # No response was made
    advance_from_last_reminder.keys = None
thisExp.addData('advance_from_last_reminder.keys',advance_from_last_reminder.keys)
if advance_from_last_reminder.keys != None:  # we had a response
    thisExp.addData('advance_from_last_reminder.rt', advance_from_last_reminder.rt)
thisExp.addData('advance_from_last_reminder.started', advance_from_last_reminder.tStartRefresh)
thisExp.addData('advance_from_last_reminder.stopped', advance_from_last_reminder.tStopRefresh)
thisExp.nextEntry()
# draw another reminder
if condition == 1:
    
    horizontal_feedback_stim.pos = [0, 0.17]
    vertical_feedback_stim.pos = [-.17, 0.17]
    grey_no_feedback_stim.pos = [.17, 0.17]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    result_final_reminder.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False)

# in condition 2, the horizontal stim means reward

elif condition == 2:
    
    horizontal_feedback_stim.pos = [-.17, 0.17]
    vertical_feedback_stim.pos = [0, 0.17]
    grey_no_feedback_stim.pos = [.17, 0.17]
    
    horizontal_feedback_stim.size = (0.10, 0.10)
    vertical_feedback_stim.size = (0.10, 0.10)
    grey_no_feedback_stim.size = (0.10, 0.10)
    
    result_final_reminder.setAutoDraw(False)
    horizontal_feedback_stim.setAutoDraw(False)
    vertical_feedback_stim.setAutoDraw(False)
    grey_no_feedback_stim.setAutoDraw(False)

# add data
psychoJS.experiment.addData('second_stim_quiz_first_question_result', second_stim_quiz_first_question_result)
psychoJS.experiment.addData('second_stim_quiz_second_question_result', second_stim_quiz_second_question_result)
psychoJS.experiment.addData('second_stim_quiz_third_question_result', second_stim_quiz_third_question_result)
# the Routine "last_stim_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "advance_to_main_task"-------
continueRoutine = True
# update component parameters for each repeat
instructions_slide_fourteen.setAutoDraw(True)
enter_main_game.keys = []
enter_main_game.rt = []
_enter_main_game_allKeys = []
# keep track of which components have finished
advance_to_main_taskComponents = [enter_main_game]
for thisComponent in advance_to_main_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
advance_to_main_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "advance_to_main_task"-------
while continueRoutine:
    # get current time
    t = advance_to_main_taskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=advance_to_main_taskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *enter_main_game* updates
    waitOnFlip = False
    if enter_main_game.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter_main_game.frameNStart = frameN  # exact frame index
        enter_main_game.tStart = t  # local t and not account for scr refresh
        enter_main_game.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter_main_game, 'tStartRefresh')  # time at next scr refresh
        enter_main_game.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter_main_game.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter_main_game.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter_main_game.status == STARTED and not waitOnFlip:
        theseKeys = enter_main_game.getKeys(keyList=['return'], waitRelease=False)
        _enter_main_game_allKeys.extend(theseKeys)
        if len(_enter_main_game_allKeys):
            enter_main_game.keys = _enter_main_game_allKeys[-1].name  # just the last key pressed
            enter_main_game.rt = _enter_main_game_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in advance_to_main_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "advance_to_main_task"-------
for thisComponent in advance_to_main_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instructions_slide_fourteen.setAutoDraw(False)
# check responses
if enter_main_game.keys in ['', [], None]:  # No response was made
    enter_main_game.keys = None
thisExp.addData('enter_main_game.keys',enter_main_game.keys)
if enter_main_game.keys != None:  # we had a response
    thisExp.addData('enter_main_game.rt', enter_main_game.rt)
thisExp.addData('enter_main_game.started', enter_main_game.tStartRefresh)
thisExp.addData('enter_main_game.stopped', enter_main_game.tStopRefresh)
thisExp.nextEntry()
# the Routine "advance_to_main_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
main_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/main_task_option_' + excel_sheet_choice_main + '.xlsx'),
    seed=None, name='main_trials')
thisExp.addLoop(main_trials)  # add the loop to the experiment
thisMain_trial = main_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
if thisMain_trial != None:
    for paramName in thisMain_trial:
        exec('{} = thisMain_trial[paramName]'.format(paramName))

for thisMain_trial in main_trials:
    currentLoop = main_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
    if thisMain_trial != None:
        for paramName in thisMain_trial:
            exec('{} = thisMain_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "main_task"-------
    continueRoutine = True
    # update component parameters for each repeat
    # add data
    work_total_presses = 0
    main_trial_num = main_trial_num + 1
    psychoJS.experiment.addData('mode', 'main')
    psychoJS.experiment.addData('main_trial_num', main_trial_num)
    psychoJS.experiment.addData('calibration_total_presses', calibration_total_presses)
    psychoJS.experiment.addData('maximum_work_for_feedback_threshold', maximum_work_for_feedback_threshold)
    psychoJS.experiment.addData('final_work_for_feedback_threshold', final_work_for_feedback_threshold)
    fractal_one_main.setPos((fractal_60_x_pos, fractal_60_y_pos))
    fractal_one_main.setImage(fractal_60_stim)
    fractal_two_main.setPos((fractal_80_x_pos, fractal_80_y_pos))
    fractal_two_main.setImage(fractal_80_stim)
    key_resp_main.keys = []
    key_resp_main.rt = []
    _key_resp_main_allKeys = []
    # initialize empty lists so we can add data
    decision_to_work_for_feedback = []
    time_of_press_list = []
    current_work_rate_list = []
    current_opacity_level_list = []
    final_opacity_level = []
    # keep track of which components have finished
    main_taskComponents = [iti_main, fractal_one_main, fractal_two_main, key_resp_main]
    for thisComponent in main_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    main_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "main_task"-------
    while continueRoutine:
        # get current time
        t = main_taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=main_taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti_main* updates
        if iti_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iti_main.frameNStart = frameN  # exact frame index
            iti_main.tStart = t  # local t and not account for scr refresh
            iti_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti_main, 'tStartRefresh')  # time at next scr refresh
            iti_main.setAutoDraw(True)
        if iti_main.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti_main.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                iti_main.tStop = t  # not accounting for scr refresh
                iti_main.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iti_main, 'tStopRefresh')  # time at next scr refresh
                iti_main.setAutoDraw(False)
        
        # *fractal_one_main* updates
        if fractal_one_main.status == NOT_STARTED and iti_main.status==FINISHED:
            # keep track of start time/frame for later
            fractal_one_main.frameNStart = frameN  # exact frame index
            fractal_one_main.tStart = t  # local t and not account for scr refresh
            fractal_one_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fractal_one_main, 'tStartRefresh')  # time at next scr refresh
            fractal_one_main.setAutoDraw(True)
        if fractal_one_main.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fractal_one_main.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fractal_one_main.tStop = t  # not accounting for scr refresh
                fractal_one_main.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fractal_one_main, 'tStopRefresh')  # time at next scr refresh
                fractal_one_main.setAutoDraw(False)
        
        # *fractal_two_main* updates
        if fractal_two_main.status == NOT_STARTED and iti_main.status==FINISHED:
            # keep track of start time/frame for later
            fractal_two_main.frameNStart = frameN  # exact frame index
            fractal_two_main.tStart = t  # local t and not account for scr refresh
            fractal_two_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fractal_two_main, 'tStartRefresh')  # time at next scr refresh
            fractal_two_main.setAutoDraw(True)
        if fractal_two_main.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fractal_two_main.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fractal_two_main.tStop = t  # not accounting for scr refresh
                fractal_two_main.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fractal_two_main, 'tStopRefresh')  # time at next scr refresh
                fractal_two_main.setAutoDraw(False)
        
        # *key_resp_main* updates
        waitOnFlip = False
        if key_resp_main.status == NOT_STARTED and iti_main.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_main.frameNStart = frameN  # exact frame index
            key_resp_main.tStart = t  # local t and not account for scr refresh
            key_resp_main.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_main, 'tStartRefresh')  # time at next scr refresh
            key_resp_main.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_main.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_main.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_main.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_main.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_main.tStop = t  # not accounting for scr refresh
                key_resp_main.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_main, 'tStopRefresh')  # time at next scr refresh
                key_resp_main.status = FINISHED
        if key_resp_main.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_main.getKeys(keyList=['f', 'j'], waitRelease=False)
            _key_resp_main_allKeys.extend(theseKeys)
            if len(_key_resp_main_allKeys):
                key_resp_main.keys = _key_resp_main_allKeys[-1].name  # just the last key pressed
                key_resp_main.rt = _key_resp_main_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in main_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "main_task"-------
    for thisComponent in main_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main_trials.addData('iti_main.started', iti_main.tStartRefresh)
    main_trials.addData('iti_main.stopped', iti_main.tStopRefresh)
    main_trials.addData('fractal_one_main.started', fractal_one_main.tStartRefresh)
    main_trials.addData('fractal_one_main.stopped', fractal_one_main.tStopRefresh)
    main_trials.addData('fractal_two_main.started', fractal_two_main.tStartRefresh)
    main_trials.addData('fractal_two_main.stopped', fractal_two_main.tStopRefresh)
    # check responses
    if key_resp_main.keys in ['', [], None]:  # No response was made
        key_resp_main.keys = None
    main_trials.addData('key_resp_main.keys',key_resp_main.keys)
    if key_resp_main.keys != None:  # we had a response
        main_trials.addData('key_resp_main.rt', key_resp_main.rt)
    main_trials.addData('key_resp_main.started', key_resp_main.tStartRefresh)
    main_trials.addData('key_resp_main.stopped', key_resp_main.tStopRefresh)
    # initialize empty lists for data
    outcome = []
    side_chosen = []
    fractal_chosen = []
    reward = []
    
    # algorithm based on response and condition
    if condition == 1:
        if key_resp_main.keys == 'f' and fractal_60_side == 'left' and fractal_60_reward == 1:
            outcome = 'good'
            side_chosen = 'left'
            fractal_chosen = 'fractal_60'
            reward = 1
            main_total_points = main_total_points + 1
    
        elif key_resp_main.keys == 'f' and fractal_60_side == 'left' and fractal_60_reward == 0:
            outcome = 'bad'
            side_chosen = 'left'
            fractal_chosen = 'fractal_60'
            reward = 0
            main_total_points = main_total_points
            
        elif key_resp_main.keys == 'j' and fractal_60_side == 'right' and fractal_60_reward == 1:
            outcome = 'good'
            side_chosen = 'right'
            fractal_chosen = 'fractal_60'
            reward = 1
            main_total_points = main_total_points + 1
            
        elif key_resp_main.keys == 'j' and fractal_60_side == 'right' and fractal_60_reward == 0:
            outcome = 'bad'
            side_chosen = 'right'
            fractal_chosen = 'fractal_60'
            reward = 0
            main_total_points = main_total_points
    
        elif key_resp_main.keys == 'f' and fractal_80_side == 'left' and fractal_80_reward == 1:
            outcome = 'good'
            side_chosen = 'left'
            fractal_chosen = 'fractal_80'
            reward = 1
            main_total_points = main_total_points + 1
        
        elif key_resp_main.keys == 'f' and fractal_80_side == 'left' and fractal_80_reward == 0:
            outcome = 'bad'
            side_chosen = 'left'
            fractal_chosen = 'fractal_80'
            reward = 0
            main_total_points = main_total_points
        
        elif key_resp_main.keys == 'j' and fractal_80_side == 'right' and fractal_80_reward == 1:
            outcome = 'good'
            side_chosen = 'right'
            fractal_chosen = 'fractal_80'
            reward = 1
            main_total_points = main_total_points + 1
        
        elif key_resp_main.keys == 'j' and fractal_80_side == 'right' and fractal_80_reward == 0:
            outcome = 'bad'
            side_chosen = 'right'
            fractal_chosen = 'fractal_80'
            reward = 0
            main_total_points = main_total_points
            
        else:
            outcome = 'missed'
            side_chosen = 'n/a'
            fractal_chosen = 'n/a'
            reward = 0
            main_total_points = main_total_points
            
    elif condition == 2:
        if key_resp_main.keys == 'f' and fractal_60_side == 'left' and fractal_60_reward == 1:
            outcome = 'good'
            side_chosen = 'left'
            fractal_chosen = 'fractal_60'
            reward = 1
            main_total_points = main_total_points + 1
            
        elif key_resp_main.keys == 'f' and fractal_60_side == 'left' and fractal_60_reward == 0:
            outcome = 'bad'
            side_chosen = 'left'
            fractal_chosen = 'fractal_60'
            reward = 0
            main_total_points = main_total_points
    
        elif key_resp_main.keys == 'j' and fractal_60_side == 'right' and fractal_60_reward == 1:
            outcome = 'good'
            side_chosen = 'right'
            fractal_chosen = 'fractal_60'
            reward = 1
            main_total_points = main_total_points + 1
            
        elif key_resp_main.keys == 'j' and fractal_60_side == 'right' and fractal_60_reward == 0:
            outcome = 'bad'
            side_chosen = 'right'
            fractal_chosen = 'fractal_60'
            reward = 0
            main_total_points = main_total_points
        
        elif key_resp_main.keys == 'f' and fractal_80_side == 'left' and fractal_80_reward == 1:
            outcome = 'good'
            side_chosen = 'left'
            fractal_chosen = 'fractal_80'
            reward = 1
            main_total_points = main_total_points + 1
            
        elif key_resp_main.keys == 'f' and fractal_80_side == 'left' and fractal_80_reward == 0:
            outcome = 'bad'
            side_chosen = 'left'
            fractal_chosen = 'fractal_80'
            reward = 0
            main_total_points = main_total_points
        
        elif key_resp_main.keys == 'j' and fractal_80_side == 'right' and fractal_80_reward == 1:
            outcome = 'good'
            side_chosen = 'right'
            fractal_chosen = 'fractal_80'
            reward = 1
            main_total_points = main_total_points + 1
            
        elif key_resp_main.keys == 'j' and fractal_80_side == 'right' and fractal_80_reward == 0:
            outcome = 'bad'
            side_chosen = 'right'
            fractal_chosen = 'fractal_80'
            reward = 0
            main_total_points = main_total_points
            
        else:
            outcome = 'missed'
            side_chosen = 'n/a'
            fractal_chosen = 'n/a'
            reward = 0
            main_total_points = main_total_points
            
    # add data
    psychoJS.experiment.addData('side_chosen', side_chosen)
    psychoJS.experiment.addData('fractal_chosen', fractal_chosen)
    psychoJS.experiment.addData('reward', reward)
    psychoJS.experiment.addData('total_points', main_total_points)
    # initialize feedback stim to draw 
    load_feedback_stim_to_draw = []
    
    # draw feedback logic
    if feedback_outcome == 'veridical_feedback' and outcome == 'good' and condition == 1:
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = vertical_feedback_stim
    
    elif feedback_outcome == 'veridical_feedback' and outcome == 'bad' and condition == 1:
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = horizontal_feedback_stim
        
    elif feedback_outcome == 'veridical_feedback' and outcome == 'good' and condition == 2:
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = horizontal_feedback_stim
        
    elif feedback_outcome == 'veridical_feedback' and outcome == 'bad' and condition == 2:
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = vertical_feedback_stim
    
    elif outcome == 'missed':
        decision_to_work_for_feedback = 'missed_trial'
    
    elif feedback_outcome == 'no_feedback':
        decision_to_work_for_feedback = 'n/a'
        load_feedback_stim_to_draw = grey_no_feedback_stim
    
    elif feedback_outcome == 'work_option':
        decision_to_work_for_feedback = 'probe'
        load_feedback_stim_to_draw = grey_no_feedback_stim
        
    # initalize empty lists to help branch experiment
    do_not_do_feedback = []
    do_feedback = []
    
    if decision_to_work_for_feedback == 'n/a':
        do_not_do_feedback = 1
        do_feedback = 0
        draw_miss = 0
        
    elif decision_to_work_for_feedback == 'probe':
        do_not_do_feedback = 0
        do_feedback = 1
        draw_miss = 0
        
    elif decision_to_work_for_feedback == 'missed_trial':
        do_not_do_feedback = 0
        do_feedback = 0
        draw_miss = 1
    
        
    # the Routine "main_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "isi_screen"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    isi_screenComponents = [isi_stim]
    for thisComponent in isi_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isi_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "isi_screen"-------
    while continueRoutine:
        # get current time
        t = isi_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isi_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi_stim* updates
        if isi_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi_stim.frameNStart = frameN  # exact frame index
            isi_stim.tStart = t  # local t and not account for scr refresh
            isi_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi_stim, 'tStartRefresh')  # time at next scr refresh
            isi_stim.setAutoDraw(True)
        if isi_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi_stim.tStartRefresh + isi-frameTolerance:
                # keep track of stop time/frame for later
                isi_stim.tStop = t  # not accounting for scr refresh
                isi_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(isi_stim, 'tStopRefresh')  # time at next scr refresh
                isi_stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isi_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "isi_screen"-------
    for thisComponent in isi_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main_trials.addData('isi_stim.started', isi_stim.tStartRefresh)
    main_trials.addData('isi_stim.stopped', isi_stim.tStopRefresh)
    # the Routine "isi_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    missed_trial_main_task = data.TrialHandler(nReps=draw_miss, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='missed_trial_main_task')
    thisExp.addLoop(missed_trial_main_task)  # add the loop to the experiment
    thisMissed_trial_main_task = missed_trial_main_task.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMissed_trial_main_task.rgb)
    if thisMissed_trial_main_task != None:
        for paramName in thisMissed_trial_main_task:
            exec('{} = thisMissed_trial_main_task[paramName]'.format(paramName))
    
    for thisMissed_trial_main_task in missed_trial_main_task:
        currentLoop = missed_trial_main_task
        # abbreviate parameter names if possible (e.g. rgb = thisMissed_trial_main_task.rgb)
        if thisMissed_trial_main_task != None:
            for paramName in thisMissed_trial_main_task:
                exec('{} = thisMissed_trial_main_task[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "missed_trial_logic"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        missed_trial_logicComponents = [missed_trial_practice]
        for thisComponent in missed_trial_logicComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        missed_trial_logicClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "missed_trial_logic"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = missed_trial_logicClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=missed_trial_logicClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *missed_trial_practice* updates
            if missed_trial_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                missed_trial_practice.frameNStart = frameN  # exact frame index
                missed_trial_practice.tStart = t  # local t and not account for scr refresh
                missed_trial_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(missed_trial_practice, 'tStartRefresh')  # time at next scr refresh
                missed_trial_practice.setAutoDraw(True)
            if missed_trial_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > missed_trial_practice.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    missed_trial_practice.tStop = t  # not accounting for scr refresh
                    missed_trial_practice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(missed_trial_practice, 'tStopRefresh')  # time at next scr refresh
                    missed_trial_practice.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in missed_trial_logicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "missed_trial_logic"-------
        for thisComponent in missed_trial_logicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        missed_trial_main_task.addData('missed_trial_practice.started', missed_trial_practice.tStartRefresh)
        missed_trial_main_task.addData('missed_trial_practice.stopped', missed_trial_practice.tStopRefresh)
        thisExp.nextEntry()
        
    # completed draw_miss repeats of 'missed_trial_main_task'
    
    
    # set up handler to look after randomisation of conditions etc
    no_feedback_work_trial_main = data.TrialHandler(nReps=do_not_do_feedback, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='no_feedback_work_trial_main')
    thisExp.addLoop(no_feedback_work_trial_main)  # add the loop to the experiment
    thisNo_feedback_work_trial_main = no_feedback_work_trial_main.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNo_feedback_work_trial_main.rgb)
    if thisNo_feedback_work_trial_main != None:
        for paramName in thisNo_feedback_work_trial_main:
            exec('{} = thisNo_feedback_work_trial_main[paramName]'.format(paramName))
    
    for thisNo_feedback_work_trial_main in no_feedback_work_trial_main:
        currentLoop = no_feedback_work_trial_main
        # abbreviate parameter names if possible (e.g. rgb = thisNo_feedback_work_trial_main.rgb)
        if thisNo_feedback_work_trial_main != None:
            for paramName in thisNo_feedback_work_trial_main:
                exec('{} = thisNo_feedback_work_trial_main[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "no_feedback_work_logic"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        load_feedback_stim_to_draw.pos = (0,0)
        load_feedback_stim_to_draw.setAutoDraw(True)
        # keep track of which components have finished
        no_feedback_work_logicComponents = [no_feedback_work_image]
        for thisComponent in no_feedback_work_logicComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        no_feedback_work_logicClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "no_feedback_work_logic"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = no_feedback_work_logicClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=no_feedback_work_logicClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *no_feedback_work_image* updates
            if no_feedback_work_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                no_feedback_work_image.frameNStart = frameN  # exact frame index
                no_feedback_work_image.tStart = t  # local t and not account for scr refresh
                no_feedback_work_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no_feedback_work_image, 'tStartRefresh')  # time at next scr refresh
                no_feedback_work_image.setAutoDraw(True)
            if no_feedback_work_image.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    no_feedback_work_image.tStop = t  # not accounting for scr refresh
                    no_feedback_work_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(no_feedback_work_image, 'tStopRefresh')  # time at next scr refresh
                    no_feedback_work_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in no_feedback_work_logicComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "no_feedback_work_logic"-------
        for thisComponent in no_feedback_work_logicComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        no_feedback_work_trial_main.addData('no_feedback_work_image.started', no_feedback_work_image.tStartRefresh)
        no_feedback_work_trial_main.addData('no_feedback_work_image.stopped', no_feedback_work_image.tStopRefresh)
        load_feedback_stim_to_draw.pos = (0,0)
        
        load_feedback_stim_to_draw.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed do_not_do_feedback repeats of 'no_feedback_work_trial_main'
    
    
    # set up handler to look after randomisation of conditions etc
    feedback_work_trial_main = data.TrialHandler(nReps=do_feedback, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='feedback_work_trial_main')
    thisExp.addLoop(feedback_work_trial_main)  # add the loop to the experiment
    thisFeedback_work_trial_main = feedback_work_trial_main.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFeedback_work_trial_main.rgb)
    if thisFeedback_work_trial_main != None:
        for paramName in thisFeedback_work_trial_main:
            exec('{} = thisFeedback_work_trial_main[paramName]'.format(paramName))
    
    for thisFeedback_work_trial_main in feedback_work_trial_main:
        currentLoop = feedback_work_trial_main
        # abbreviate parameter names if possible (e.g. rgb = thisFeedback_work_trial_main.rgb)
        if thisFeedback_work_trial_main != None:
            for paramName in thisFeedback_work_trial_main:
                exec('{} = thisFeedback_work_trial_main[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "grey_work_for_fb"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        load_feedback_stim_to_draw.pos = (0,0)
        load_feedback_stim_to_draw.setAutoDraw(True)
        # keep track of which components have finished
        grey_work_for_fbComponents = [grey_stim_work_for_fb]
        for thisComponent in grey_work_for_fbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        grey_work_for_fbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "grey_work_for_fb"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = grey_work_for_fbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=grey_work_for_fbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *grey_stim_work_for_fb* updates
            if grey_stim_work_for_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grey_stim_work_for_fb.frameNStart = frameN  # exact frame index
                grey_stim_work_for_fb.tStart = t  # local t and not account for scr refresh
                grey_stim_work_for_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grey_stim_work_for_fb, 'tStartRefresh')  # time at next scr refresh
                grey_stim_work_for_fb.setAutoDraw(True)
            if grey_stim_work_for_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grey_stim_work_for_fb.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    grey_stim_work_for_fb.tStop = t  # not accounting for scr refresh
                    grey_stim_work_for_fb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(grey_stim_work_for_fb, 'tStopRefresh')  # time at next scr refresh
                    grey_stim_work_for_fb.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in grey_work_for_fbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "grey_work_for_fb"-------
        for thisComponent in grey_work_for_fbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedback_work_trial_main.addData('grey_stim_work_for_fb.started', grey_stim_work_for_fb.tStartRefresh)
        feedback_work_trial_main.addData('grey_stim_work_for_fb.stopped', grey_stim_work_for_fb.tStopRefresh)
        load_feedback_stim_to_draw.pos = (0,0)
        load_feedback_stim_to_draw.setAutoDraw(False)
        
        # ------Prepare to start Routine "ask_want_to_work_for_feedback"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        feedback_choice_key_resp.keys = []
        feedback_choice_key_resp.rt = []
        _feedback_choice_key_resp_allKeys = []
        # keep track of which components have finished
        ask_want_to_work_for_feedbackComponents = [feedback_choice_key_resp, feedback_choice_slide]
        for thisComponent in ask_want_to_work_for_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ask_want_to_work_for_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ask_want_to_work_for_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ask_want_to_work_for_feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ask_want_to_work_for_feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_choice_key_resp* updates
            waitOnFlip = False
            if feedback_choice_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_choice_key_resp.frameNStart = frameN  # exact frame index
                feedback_choice_key_resp.tStart = t  # local t and not account for scr refresh
                feedback_choice_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_choice_key_resp, 'tStartRefresh')  # time at next scr refresh
                feedback_choice_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(feedback_choice_key_resp.clock.reset)  # t=0 on next screen flip
            if feedback_choice_key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_choice_key_resp.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_choice_key_resp.tStop = t  # not accounting for scr refresh
                    feedback_choice_key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_choice_key_resp, 'tStopRefresh')  # time at next scr refresh
                    feedback_choice_key_resp.status = FINISHED
            if feedback_choice_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = feedback_choice_key_resp.getKeys(keyList=['o', 'w'], waitRelease=False)
                _feedback_choice_key_resp_allKeys.extend(theseKeys)
                if len(_feedback_choice_key_resp_allKeys):
                    feedback_choice_key_resp.keys = _feedback_choice_key_resp_allKeys[-1].name  # just the last key pressed
                    feedback_choice_key_resp.rt = _feedback_choice_key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *feedback_choice_slide* updates
            if feedback_choice_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_choice_slide.frameNStart = frameN  # exact frame index
                feedback_choice_slide.tStart = t  # local t and not account for scr refresh
                feedback_choice_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_choice_slide, 'tStartRefresh')  # time at next scr refresh
                feedback_choice_slide.setAutoDraw(True)
            if feedback_choice_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_choice_slide.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_choice_slide.tStop = t  # not accounting for scr refresh
                    feedback_choice_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_choice_slide, 'tStopRefresh')  # time at next scr refresh
                    feedback_choice_slide.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ask_want_to_work_for_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ask_want_to_work_for_feedback"-------
        for thisComponent in ask_want_to_work_for_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if feedback_choice_key_resp.keys in ['', [], None]:  # No response was made
            feedback_choice_key_resp.keys = None
        feedback_work_trial_main.addData('feedback_choice_key_resp.keys',feedback_choice_key_resp.keys)
        if feedback_choice_key_resp.keys != None:  # we had a response
            feedback_work_trial_main.addData('feedback_choice_key_resp.rt', feedback_choice_key_resp.rt)
        feedback_work_trial_main.addData('feedback_choice_key_resp.started', feedback_choice_key_resp.tStartRefresh)
        feedback_work_trial_main.addData('feedback_choice_key_resp.stopped', feedback_choice_key_resp.tStopRefresh)
        feedback_work_trial_main.addData('feedback_choice_slide.started', feedback_choice_slide.tStartRefresh)
        feedback_work_trial_main.addData('feedback_choice_slide.stopped', feedback_choice_slide.tStopRefresh)
        # intialize empty lists to branch experiment
        highlight_no = []
        highlight_yes = []
        
        # decide if we should draw yes or no highlighted slide
        if feedback_choice_key_resp.keys == 'w':     
            decision_to_work_for_feedback = 'yes'
            highlight_no = 0
            highlight_yes = 1
                
        elif feedback_choice_key_resp.keys == 'o':
            decision_to_work_for_feedback = 'no'       
            highlight_no = 1
            highlight_yes = 0
            
        else:
            decision_to_work_for_feedback = 'missed'       
            highlight_no = 0
            highlight_yes = 0
        
        # set up handler to look after randomisation of conditions etc
        no_loop_highlight_main = data.TrialHandler(nReps=highlight_no, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='no_loop_highlight_main')
        thisExp.addLoop(no_loop_highlight_main)  # add the loop to the experiment
        thisNo_loop_highlight_main = no_loop_highlight_main.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisNo_loop_highlight_main.rgb)
        if thisNo_loop_highlight_main != None:
            for paramName in thisNo_loop_highlight_main:
                exec('{} = thisNo_loop_highlight_main[paramName]'.format(paramName))
        
        for thisNo_loop_highlight_main in no_loop_highlight_main:
            currentLoop = no_loop_highlight_main
            # abbreviate parameter names if possible (e.g. rgb = thisNo_loop_highlight_main.rgb)
            if thisNo_loop_highlight_main != None:
                for paramName in thisNo_loop_highlight_main:
                    exec('{} = thisNo_loop_highlight_main[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "no_fb_highlight"-------
            continueRoutine = True
            routineTimer.add(0.300000)
            # update component parameters for each repeat
            # keep track of which components have finished
            no_fb_highlightComponents = [no_fb_slide]
            for thisComponent in no_fb_highlightComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            no_fb_highlightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "no_fb_highlight"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = no_fb_highlightClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=no_fb_highlightClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *no_fb_slide* updates
                if no_fb_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    no_fb_slide.frameNStart = frameN  # exact frame index
                    no_fb_slide.tStart = t  # local t and not account for scr refresh
                    no_fb_slide.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(no_fb_slide, 'tStartRefresh')  # time at next scr refresh
                    no_fb_slide.setAutoDraw(True)
                if no_fb_slide.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > .3-frameTolerance:
                        # keep track of stop time/frame for later
                        no_fb_slide.tStop = t  # not accounting for scr refresh
                        no_fb_slide.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(no_fb_slide, 'tStopRefresh')  # time at next scr refresh
                        no_fb_slide.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in no_fb_highlightComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "no_fb_highlight"-------
            for thisComponent in no_fb_highlightComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            no_loop_highlight_main.addData('no_fb_slide.started', no_fb_slide.tStartRefresh)
            no_loop_highlight_main.addData('no_fb_slide.stopped', no_fb_slide.tStopRefresh)
            thisExp.nextEntry()
            
        # completed highlight_no repeats of 'no_loop_highlight_main'
        
        
        # set up handler to look after randomisation of conditions etc
        yes_loop_highlight_main = data.TrialHandler(nReps=highlight_yes, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='yes_loop_highlight_main')
        thisExp.addLoop(yes_loop_highlight_main)  # add the loop to the experiment
        thisYes_loop_highlight_main = yes_loop_highlight_main.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisYes_loop_highlight_main.rgb)
        if thisYes_loop_highlight_main != None:
            for paramName in thisYes_loop_highlight_main:
                exec('{} = thisYes_loop_highlight_main[paramName]'.format(paramName))
        
        for thisYes_loop_highlight_main in yes_loop_highlight_main:
            currentLoop = yes_loop_highlight_main
            # abbreviate parameter names if possible (e.g. rgb = thisYes_loop_highlight_main.rgb)
            if thisYes_loop_highlight_main != None:
                for paramName in thisYes_loop_highlight_main:
                    exec('{} = thisYes_loop_highlight_main[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "yes_fb_highlight"-------
            continueRoutine = True
            routineTimer.add(0.300000)
            # update component parameters for each repeat
            # keep track of which components have finished
            yes_fb_highlightComponents = [yes_fb_slide]
            for thisComponent in yes_fb_highlightComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            yes_fb_highlightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "yes_fb_highlight"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = yes_fb_highlightClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=yes_fb_highlightClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *yes_fb_slide* updates
                if yes_fb_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    yes_fb_slide.frameNStart = frameN  # exact frame index
                    yes_fb_slide.tStart = t  # local t and not account for scr refresh
                    yes_fb_slide.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(yes_fb_slide, 'tStartRefresh')  # time at next scr refresh
                    yes_fb_slide.setAutoDraw(True)
                if yes_fb_slide.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > .3-frameTolerance:
                        # keep track of stop time/frame for later
                        yes_fb_slide.tStop = t  # not accounting for scr refresh
                        yes_fb_slide.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(yes_fb_slide, 'tStopRefresh')  # time at next scr refresh
                        yes_fb_slide.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in yes_fb_highlightComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "yes_fb_highlight"-------
            for thisComponent in yes_fb_highlightComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            yes_loop_highlight_main.addData('yes_fb_slide.started', yes_fb_slide.tStartRefresh)
            yes_loop_highlight_main.addData('yes_fb_slide.stopped', yes_fb_slide.tStopRefresh)
            
            # ------Prepare to start Routine "fb_work_time"-------
            continueRoutine = True
            # update component parameters for each repeat
            # lets set the stim to draw for feedback contingent on condition and outcome
            feedback_stim_to_draw = []
            
            # in condition 1, the vertical stim means reward
            if condition == 1:
                
                if outcome == 'good':
                    feedback_stim_to_draw = vertical_feedback_stim
                    
                elif outcome == 'bad':
                    feedback_stim_to_draw = horizontal_feedback_stim
                    
            # in condition 2, the horizontal stim means reward
            elif condition == 2:
                
                if outcome == 'good':
                    feedback_stim_to_draw = horizontal_feedback_stim
                    
                elif outcome == 'bad':
                    feedback_stim_to_draw = vertical_feedback_stim
            # keep track of which components have finished
            fb_work_timeComponents = []
            for thisComponent in fb_work_timeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            fb_work_timeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "fb_work_time"-------
            while continueRoutine:
                # get current time
                t = fb_work_timeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=fb_work_timeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fb_work_timeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "fb_work_time"-------
            for thisComponent in fb_work_timeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "fb_work_time" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "draw_feedback_to_screen"-------
            continueRoutine = True
            routineTimer.add(3.000000)
            # update component parameters for each repeat
            feedback_stim_to_draw.pos = (0,0)
            grey_no_feedback_stim.pos = (0,0)
            
            feedback_stim_to_draw.opacity = 1
            grey_no_feedback_stim.opacity = 1
            
            update_opacity = .0150
            
            time_of_press = []
            time_of_press_list = []
            
            work_total_presses = 0
            
            current_work_rate = []
            current_work_rate_list = []
            
            current_opacity_level_list = []
            final_opacity_level = []
            
            event.clearEvents()
            work_for_feedback_space_bar_press.keys = []
            work_for_feedback_space_bar_press.rt = []
            _work_for_feedback_space_bar_press_allKeys = []
            # keep track of which components have finished
            draw_feedback_to_screenComponents = [work_for_feedback_space_bar_press]
            for thisComponent in draw_feedback_to_screenComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            draw_feedback_to_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "draw_feedback_to_screen"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = draw_feedback_to_screenClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=draw_feedback_to_screenClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                feedback_stim_to_draw.setAutoDraw(True)
                grey_no_feedback_stim.setAutoDraw(True)
                
                keys = psychoJS.eventManager.getKeys();
                if 'space' in keys and draw_feedback_to_screenClock.getTime() < 3.0:
                #if 'space' in keys:
                    
                    time_of_press = draw_feedback_to_screenClock.getTime()
                    time_of_press_list.push(time_of_press)
                    work_total_presses = work_total_presses + 1
                    current_work_rate = work_total_presses / time_of_press
                    current_opacity_level_list.push(grey_no_feedback_stim.opacity)
                    
                    if current_work_rate > final_work_for_feedback_threshold:
                        
                        grey_no_feedback_stim.opacity = grey_no_feedback_stim.opacity - update_opacity
                
                # *work_for_feedback_space_bar_press* updates
                waitOnFlip = False
                if work_for_feedback_space_bar_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    work_for_feedback_space_bar_press.frameNStart = frameN  # exact frame index
                    work_for_feedback_space_bar_press.tStart = t  # local t and not account for scr refresh
                    work_for_feedback_space_bar_press.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(work_for_feedback_space_bar_press, 'tStartRefresh')  # time at next scr refresh
                    work_for_feedback_space_bar_press.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(work_for_feedback_space_bar_press.clock.reset)  # t=0 on next screen flip
                if work_for_feedback_space_bar_press.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 3.0-frameTolerance:
                        # keep track of stop time/frame for later
                        work_for_feedback_space_bar_press.tStop = t  # not accounting for scr refresh
                        work_for_feedback_space_bar_press.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(work_for_feedback_space_bar_press, 'tStopRefresh')  # time at next scr refresh
                        work_for_feedback_space_bar_press.status = FINISHED
                if work_for_feedback_space_bar_press.status == STARTED and not waitOnFlip:
                    theseKeys = work_for_feedback_space_bar_press.getKeys(keyList=['e'], waitRelease=False)
                    _work_for_feedback_space_bar_press_allKeys.extend(theseKeys)
                    if len(_work_for_feedback_space_bar_press_allKeys):
                        work_for_feedback_space_bar_press.keys = _work_for_feedback_space_bar_press_allKeys[-1].name  # just the last key pressed
                        work_for_feedback_space_bar_press.rt = _work_for_feedback_space_bar_press_allKeys[-1].rt
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in draw_feedback_to_screenComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "draw_feedback_to_screen"-------
            for thisComponent in draw_feedback_to_screenComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            feedback_stim_to_draw.setAutoDraw(False)
            grey_no_feedback_stim.setAutoDraw(False)
            final_opacity_level = grey_no_feedback_stim.opacity
            
            event.clearEvents()
            
            # ------Prepare to start Routine "post_work_blank"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            post_work_space_presses.keys = []
            post_work_space_presses.rt = []
            _post_work_space_presses_allKeys = []
            # keep track of which components have finished
            post_work_blankComponents = [blank_image, post_work_space_presses]
            for thisComponent in post_work_blankComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            post_work_blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "post_work_blank"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = post_work_blankClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=post_work_blankClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank_image* updates
                if blank_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blank_image.frameNStart = frameN  # exact frame index
                    blank_image.tStart = t  # local t and not account for scr refresh
                    blank_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blank_image, 'tStartRefresh')  # time at next scr refresh
                    blank_image.setAutoDraw(True)
                if blank_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blank_image.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        blank_image.tStop = t  # not accounting for scr refresh
                        blank_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(blank_image, 'tStopRefresh')  # time at next scr refresh
                        blank_image.setAutoDraw(False)
                
                # *post_work_space_presses* updates
                waitOnFlip = False
                if post_work_space_presses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    post_work_space_presses.frameNStart = frameN  # exact frame index
                    post_work_space_presses.tStart = t  # local t and not account for scr refresh
                    post_work_space_presses.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(post_work_space_presses, 'tStartRefresh')  # time at next scr refresh
                    post_work_space_presses.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(post_work_space_presses.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(post_work_space_presses.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if post_work_space_presses.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        post_work_space_presses.tStop = t  # not accounting for scr refresh
                        post_work_space_presses.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(post_work_space_presses, 'tStopRefresh')  # time at next scr refresh
                        post_work_space_presses.status = FINISHED
                if post_work_space_presses.status == STARTED and not waitOnFlip:
                    theseKeys = post_work_space_presses.getKeys(keyList=['space'], waitRelease=False)
                    _post_work_space_presses_allKeys.extend(theseKeys)
                    if len(_post_work_space_presses_allKeys):
                        post_work_space_presses.keys = [key.name for key in _post_work_space_presses_allKeys]  # storing all keys
                        post_work_space_presses.rt = [key.rt for key in _post_work_space_presses_allKeys]
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in post_work_blankComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "post_work_blank"-------
            for thisComponent in post_work_blankComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            yes_loop_highlight_main.addData('blank_image.started', blank_image.tStartRefresh)
            yes_loop_highlight_main.addData('blank_image.stopped', blank_image.tStopRefresh)
            # check responses
            if post_work_space_presses.keys in ['', [], None]:  # No response was made
                post_work_space_presses.keys = None
            yes_loop_highlight_main.addData('post_work_space_presses.keys',post_work_space_presses.keys)
            if post_work_space_presses.keys != None:  # we had a response
                yes_loop_highlight_main.addData('post_work_space_presses.rt', post_work_space_presses.rt)
            yes_loop_highlight_main.addData('post_work_space_presses.started', post_work_space_presses.tStartRefresh)
            yes_loop_highlight_main.addData('post_work_space_presses.stopped', post_work_space_presses.tStopRefresh)
            thisExp.nextEntry()
            
        # completed highlight_yes repeats of 'yes_loop_highlight_main'
        
        thisExp.nextEntry()
        
    # completed do_feedback repeats of 'feedback_work_trial_main'
    
    
    # ------Prepare to start Routine "end_loop_data_log"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    end_loop_data_logComponents = []
    for thisComponent in end_loop_data_logComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_loop_data_logClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_loop_data_log"-------
    while continueRoutine:
        # get current time
        t = end_loop_data_logClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_loop_data_logClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_loop_data_logComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_loop_data_log"-------
    for thisComponent in end_loop_data_logComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # add data
    psychoJS.experiment.addData('decision_to_work_for_feedback', decision_to_work_for_feedback)
    psychoJS.experiment.addData('time_of_press_list', time_of_press_list)
    psychoJS.experiment.addData('work_total_presses', work_total_presses)
    psychoJS.experiment.addData('current_work_rate_list', current_work_rate_list)
    psychoJS.experiment.addData('current_opacity_level_list', current_opacity_level_list)
    psychoJS.experiment.addData('final_opacity_level', final_opacity_level)
    
    # the Routine "end_loop_data_log" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'main_trials'


# ------Prepare to start Routine "blank_screen_2"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
blank_screen_2Components = [blank_slide_2]
for thisComponent in blank_screen_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank_screen_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank_screen_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank_screen_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank_screen_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank_slide_2* updates
    if blank_slide_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank_slide_2.frameNStart = frameN  # exact frame index
        blank_slide_2.tStart = t  # local t and not account for scr refresh
        blank_slide_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_slide_2, 'tStartRefresh')  # time at next scr refresh
        blank_slide_2.setAutoDraw(True)
    if blank_slide_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_slide_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            blank_slide_2.tStop = t  # not accounting for scr refresh
            blank_slide_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank_slide_2, 'tStopRefresh')  # time at next scr refresh
            blank_slide_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank_screen_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank_screen_2"-------
for thisComponent in blank_screen_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blank_slide_2.started', blank_slide_2.tStartRefresh)
thisExp.addData('blank_slide_2.stopped', blank_slide_2.tStopRefresh)

# ------Prepare to start Routine "completed_main_task"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
completed_main_taskComponents = [post_task_image]
for thisComponent in completed_main_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
completed_main_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "completed_main_task"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = completed_main_taskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=completed_main_taskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *post_task_image* updates
    if post_task_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        post_task_image.frameNStart = frameN  # exact frame index
        post_task_image.tStart = t  # local t and not account for scr refresh
        post_task_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(post_task_image, 'tStartRefresh')  # time at next scr refresh
        post_task_image.setAutoDraw(True)
    if post_task_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > post_task_image.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            post_task_image.tStop = t  # not accounting for scr refresh
            post_task_image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(post_task_image, 'tStopRefresh')  # time at next scr refresh
            post_task_image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in completed_main_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "completed_main_task"-------
for thisComponent in completed_main_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('post_task_image.started', post_task_image.tStartRefresh)
thisExp.addData('post_task_image.stopped', post_task_image.tStopRefresh)

# ------Prepare to start Routine "continue_to_fractal_question"-------
continueRoutine = True
# update component parameters for each repeat
post_task_continue_slide.setAutoDraw(True)
go_to_fractal_question.keys = []
go_to_fractal_question.rt = []
_go_to_fractal_question_allKeys = []
# keep track of which components have finished
continue_to_fractal_questionComponents = [go_to_fractal_question]
for thisComponent in continue_to_fractal_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
continue_to_fractal_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "continue_to_fractal_question"-------
while continueRoutine:
    # get current time
    t = continue_to_fractal_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=continue_to_fractal_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *go_to_fractal_question* updates
    waitOnFlip = False
    if go_to_fractal_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        go_to_fractal_question.frameNStart = frameN  # exact frame index
        go_to_fractal_question.tStart = t  # local t and not account for scr refresh
        go_to_fractal_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(go_to_fractal_question, 'tStartRefresh')  # time at next scr refresh
        go_to_fractal_question.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(go_to_fractal_question.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(go_to_fractal_question.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if go_to_fractal_question.status == STARTED and not waitOnFlip:
        theseKeys = go_to_fractal_question.getKeys(keyList=None, waitRelease=False)
        _go_to_fractal_question_allKeys.extend(theseKeys)
        if len(_go_to_fractal_question_allKeys):
            go_to_fractal_question.keys = _go_to_fractal_question_allKeys[-1].name  # just the last key pressed
            go_to_fractal_question.rt = _go_to_fractal_question_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in continue_to_fractal_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "continue_to_fractal_question"-------
for thisComponent in continue_to_fractal_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
post_task_continue_slide.setAutoDraw(False)
# check responses
if go_to_fractal_question.keys in ['', [], None]:  # No response was made
    go_to_fractal_question.keys = None
thisExp.addData('go_to_fractal_question.keys',go_to_fractal_question.keys)
if go_to_fractal_question.keys != None:  # we had a response
    thisExp.addData('go_to_fractal_question.rt', go_to_fractal_question.rt)
thisExp.addData('go_to_fractal_question.started', go_to_fractal_question.tStartRefresh)
thisExp.addData('go_to_fractal_question.stopped', go_to_fractal_question.tStopRefresh)
thisExp.nextEntry()
# the Routine "continue_to_fractal_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "post_task_fractal_question"-------
continueRoutine = True
# update component parameters for each repeat
better_fractal = []

if post_task_fractal_selection == 1:
      
    fractal_blossom.pos = [-0.2, .04]
    fractal_octopus.pos = [0.2, .04]
    post_task_fractal_slide.setAutoDraw(True)
    fractal_blossom.setAutoDraw(True)
    fractal_octopus.setAutoDraw(True)

elif post_task_fractal_selection == 2:

    fractal_blossom.pos = [0.2, .04]
    fractal_octopus.pos = [-0.2, .04]
    post_task_fractal_slide.setAutoDraw(True)
    fractal_blossom.setAutoDraw(True)
    fractal_octopus.setAutoDraw(True)
choose_fractal.keys = []
choose_fractal.rt = []
_choose_fractal_allKeys = []
# keep track of which components have finished
post_task_fractal_questionComponents = [choose_fractal]
for thisComponent in post_task_fractal_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
post_task_fractal_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "post_task_fractal_question"-------
while continueRoutine:
    # get current time
    t = post_task_fractal_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=post_task_fractal_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *choose_fractal* updates
    waitOnFlip = False
    if choose_fractal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choose_fractal.frameNStart = frameN  # exact frame index
        choose_fractal.tStart = t  # local t and not account for scr refresh
        choose_fractal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choose_fractal, 'tStartRefresh')  # time at next scr refresh
        choose_fractal.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(choose_fractal.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(choose_fractal.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if choose_fractal.status == STARTED and not waitOnFlip:
        theseKeys = choose_fractal.getKeys(keyList=['1', '2'], waitRelease=False)
        _choose_fractal_allKeys.extend(theseKeys)
        if len(_choose_fractal_allKeys):
            choose_fractal.keys = _choose_fractal_allKeys[-1].name  # just the last key pressed
            choose_fractal.rt = _choose_fractal_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in post_task_fractal_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "post_task_fractal_question"-------
for thisComponent in post_task_fractal_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
better_fractal = []

if post_task_fractal_selection == 1:
      
    fractal_blossom.pos = [0.2, .04]
    fractal_octopus.pos = [-0.2, .04]
    post_task_fractal_slide.setAutoDraw(False)
    fractal_blossom.setAutoDraw(False)
    fractal_octopus.setAutoDraw(False)

elif post_task_fractal_selection == 2:

    fractal_blossom.pos = [-0.2, .04]
    fractal_octopus.pos = [0.2, .04]
    post_task_fractal_slide.setAutoDraw(False)
    fractal_blossom.setAutoDraw(False)
    fractal_octopus.setAutoDraw(False)

if post_task_fractal_selection == 1 and choose_fractal.keys == '1':
    better_fractal = 'blossom'
elif post_task_fractal_selection == 1 and choose_fractal.keys == '2':
    better_fractal = 'octopus'       
elif post_task_fractal_selection == 2 and choose_fractal.keys == '1':
    better_fractal = 'octopus'
elif post_task_fractal_selection == 2 and choose_fractal.keys == '2':
    better_fractal = 'blossom'   

psychoJS.experiment.addData('better_fractal', better_fractal)
# check responses
if choose_fractal.keys in ['', [], None]:  # No response was made
    choose_fractal.keys = None
thisExp.addData('choose_fractal.keys',choose_fractal.keys)
if choose_fractal.keys != None:  # we had a response
    thisExp.addData('choose_fractal.rt', choose_fractal.rt)
thisExp.addData('choose_fractal.started', choose_fractal.tStartRefresh)
thisExp.addData('choose_fractal.stopped', choose_fractal.tStopRefresh)
thisExp.nextEntry()
# the Routine "post_task_fractal_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SAM_hu_directions"-------
continueRoutine = True
# update component parameters for each repeat
SAM_hu_instructions_key_resp.keys = []
SAM_hu_instructions_key_resp.rt = []
_SAM_hu_instructions_key_resp_allKeys = []
# keep track of which components have finished
SAM_hu_directionsComponents = [SAM_hu_instructions, SAM_hu_instructions_key_resp]
for thisComponent in SAM_hu_directionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SAM_hu_directionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SAM_hu_directions"-------
while continueRoutine:
    # get current time
    t = SAM_hu_directionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SAM_hu_directionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SAM_hu_instructions* updates
    if SAM_hu_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_hu_instructions.frameNStart = frameN  # exact frame index
        SAM_hu_instructions.tStart = t  # local t and not account for scr refresh
        SAM_hu_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_hu_instructions, 'tStartRefresh')  # time at next scr refresh
        SAM_hu_instructions.setAutoDraw(True)
    
    # *SAM_hu_instructions_key_resp* updates
    waitOnFlip = False
    if SAM_hu_instructions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_hu_instructions_key_resp.frameNStart = frameN  # exact frame index
        SAM_hu_instructions_key_resp.tStart = t  # local t and not account for scr refresh
        SAM_hu_instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_hu_instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
        SAM_hu_instructions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SAM_hu_instructions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SAM_hu_instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SAM_hu_instructions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = SAM_hu_instructions_key_resp.getKeys(keyList=None, waitRelease=False)
        _SAM_hu_instructions_key_resp_allKeys.extend(theseKeys)
        if len(_SAM_hu_instructions_key_resp_allKeys):
            SAM_hu_instructions_key_resp.keys = _SAM_hu_instructions_key_resp_allKeys[-1].name  # just the last key pressed
            SAM_hu_instructions_key_resp.rt = _SAM_hu_instructions_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SAM_hu_directionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SAM_hu_directions"-------
for thisComponent in SAM_hu_directionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SAM_hu_instructions.started', SAM_hu_instructions.tStartRefresh)
thisExp.addData('SAM_hu_instructions.stopped', SAM_hu_instructions.tStopRefresh)
# check responses
if SAM_hu_instructions_key_resp.keys in ['', [], None]:  # No response was made
    SAM_hu_instructions_key_resp.keys = None
thisExp.addData('SAM_hu_instructions_key_resp.keys',SAM_hu_instructions_key_resp.keys)
if SAM_hu_instructions_key_resp.keys != None:  # we had a response
    thisExp.addData('SAM_hu_instructions_key_resp.rt', SAM_hu_instructions_key_resp.rt)
thisExp.addData('SAM_hu_instructions_key_resp.started', SAM_hu_instructions_key_resp.tStartRefresh)
thisExp.addData('SAM_hu_instructions_key_resp.stopped', SAM_hu_instructions_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "SAM_hu_directions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SAM_hu_question_2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the select_answer_mouse_3
select_answer_mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
SAM_hu_question_2Components = [SAM_hu_2, choice_1_post, choice_2_post, choice_3_post, choice_4_post, choice_5_post, choice_6_post, choice_7_post, choice_8_post, choice_9_post, select_answer_mouse_3]
for thisComponent in SAM_hu_question_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SAM_hu_question_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SAM_hu_question_2"-------
while continueRoutine:
    # get current time
    t = SAM_hu_question_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SAM_hu_question_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SAM_hu_2* updates
    if SAM_hu_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_hu_2.frameNStart = frameN  # exact frame index
        SAM_hu_2.tStart = t  # local t and not account for scr refresh
        SAM_hu_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_hu_2, 'tStartRefresh')  # time at next scr refresh
        SAM_hu_2.setAutoDraw(True)
    
    # *choice_1_post* updates
    if choice_1_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_1_post.frameNStart = frameN  # exact frame index
        choice_1_post.tStart = t  # local t and not account for scr refresh
        choice_1_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_1_post, 'tStartRefresh')  # time at next scr refresh
        choice_1_post.setAutoDraw(True)
    
    # *choice_2_post* updates
    if choice_2_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_2_post.frameNStart = frameN  # exact frame index
        choice_2_post.tStart = t  # local t and not account for scr refresh
        choice_2_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_2_post, 'tStartRefresh')  # time at next scr refresh
        choice_2_post.setAutoDraw(True)
    
    # *choice_3_post* updates
    if choice_3_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_3_post.frameNStart = frameN  # exact frame index
        choice_3_post.tStart = t  # local t and not account for scr refresh
        choice_3_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_3_post, 'tStartRefresh')  # time at next scr refresh
        choice_3_post.setAutoDraw(True)
    
    # *choice_4_post* updates
    if choice_4_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_4_post.frameNStart = frameN  # exact frame index
        choice_4_post.tStart = t  # local t and not account for scr refresh
        choice_4_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_4_post, 'tStartRefresh')  # time at next scr refresh
        choice_4_post.setAutoDraw(True)
    
    # *choice_5_post* updates
    if choice_5_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_5_post.frameNStart = frameN  # exact frame index
        choice_5_post.tStart = t  # local t and not account for scr refresh
        choice_5_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_5_post, 'tStartRefresh')  # time at next scr refresh
        choice_5_post.setAutoDraw(True)
    
    # *choice_6_post* updates
    if choice_6_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_6_post.frameNStart = frameN  # exact frame index
        choice_6_post.tStart = t  # local t and not account for scr refresh
        choice_6_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_6_post, 'tStartRefresh')  # time at next scr refresh
        choice_6_post.setAutoDraw(True)
    
    # *choice_7_post* updates
    if choice_7_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_7_post.frameNStart = frameN  # exact frame index
        choice_7_post.tStart = t  # local t and not account for scr refresh
        choice_7_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_7_post, 'tStartRefresh')  # time at next scr refresh
        choice_7_post.setAutoDraw(True)
    
    # *choice_8_post* updates
    if choice_8_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_8_post.frameNStart = frameN  # exact frame index
        choice_8_post.tStart = t  # local t and not account for scr refresh
        choice_8_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_8_post, 'tStartRefresh')  # time at next scr refresh
        choice_8_post.setAutoDraw(True)
    
    # *choice_9_post* updates
    if choice_9_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_9_post.frameNStart = frameN  # exact frame index
        choice_9_post.tStart = t  # local t and not account for scr refresh
        choice_9_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_9_post, 'tStartRefresh')  # time at next scr refresh
        choice_9_post.setAutoDraw(True)
    # *select_answer_mouse_3* updates
    if select_answer_mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        select_answer_mouse_3.frameNStart = frameN  # exact frame index
        select_answer_mouse_3.tStart = t  # local t and not account for scr refresh
        select_answer_mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(select_answer_mouse_3, 'tStartRefresh')  # time at next scr refresh
        select_answer_mouse_3.status = STARTED
        select_answer_mouse_3.mouseClock.reset()
        prevButtonState = select_answer_mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if select_answer_mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = select_answer_mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [choice_1_post,choice_2_post,choice_3_post,choice_4_post,choice_5_post,choice_6_post,choice_7_post,choice_8_post,choice_9_post]:
                    if obj.contains(select_answer_mouse_3):
                        gotValidClick = True
                        select_answer_mouse_3.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SAM_hu_question_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SAM_hu_question_2"-------
for thisComponent in SAM_hu_question_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SAM_hu_2.started', SAM_hu_2.tStartRefresh)
thisExp.addData('SAM_hu_2.stopped', SAM_hu_2.tStopRefresh)
thisExp.addData('choice_1_post.started', choice_1_post.tStartRefresh)
thisExp.addData('choice_1_post.stopped', choice_1_post.tStopRefresh)
thisExp.addData('choice_2_post.started', choice_2_post.tStartRefresh)
thisExp.addData('choice_2_post.stopped', choice_2_post.tStopRefresh)
thisExp.addData('choice_3_post.started', choice_3_post.tStartRefresh)
thisExp.addData('choice_3_post.stopped', choice_3_post.tStopRefresh)
thisExp.addData('choice_4_post.started', choice_4_post.tStartRefresh)
thisExp.addData('choice_4_post.stopped', choice_4_post.tStopRefresh)
thisExp.addData('choice_5_post.started', choice_5_post.tStartRefresh)
thisExp.addData('choice_5_post.stopped', choice_5_post.tStopRefresh)
thisExp.addData('choice_6_post.started', choice_6_post.tStartRefresh)
thisExp.addData('choice_6_post.stopped', choice_6_post.tStopRefresh)
thisExp.addData('choice_7_post.started', choice_7_post.tStartRefresh)
thisExp.addData('choice_7_post.stopped', choice_7_post.tStopRefresh)
thisExp.addData('choice_8_post.started', choice_8_post.tStartRefresh)
thisExp.addData('choice_8_post.stopped', choice_8_post.tStopRefresh)
thisExp.addData('choice_9_post.started', choice_9_post.tStartRefresh)
thisExp.addData('choice_9_post.stopped', choice_9_post.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = select_answer_mouse_3.getPos()
buttons = select_answer_mouse_3.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [choice_1_post,choice_2_post,choice_3_post,choice_4_post,choice_5_post,choice_6_post,choice_7_post,choice_8_post,choice_9_post]:
        if obj.contains(select_answer_mouse_3):
            gotValidClick = True
            select_answer_mouse_3.clicked_name.append(obj.name)
thisExp.addData('select_answer_mouse_3.x', x)
thisExp.addData('select_answer_mouse_3.y', y)
thisExp.addData('select_answer_mouse_3.leftButton', buttons[0])
thisExp.addData('select_answer_mouse_3.midButton', buttons[1])
thisExp.addData('select_answer_mouse_3.rightButton', buttons[2])
if len(select_answer_mouse_3.clicked_name):
    thisExp.addData('select_answer_mouse_3.clicked_name', select_answer_mouse_3.clicked_name[0])
thisExp.addData('select_answer_mouse_3.started', select_answer_mouse_3.tStart)
thisExp.addData('select_answer_mouse_3.stopped', select_answer_mouse_3.tStop)
thisExp.nextEntry()
answer_to_draw = []
for answer in [choice_1_post,choice_2_post,choice_3_post,choice_4_post,choice_5_post,choice_6_post,choice_7_post,choice_8_post,choice_9_post]:
    if select_answer_mouse_3.isPressedIn(answer):
        answer_to_draw = answer
# the Routine "SAM_hu_question_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "highlight_post_sam_hu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
highlight_post_sam_huComponents = [sam_hu_highlight_post]
for thisComponent in highlight_post_sam_huComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
highlight_post_sam_huClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "highlight_post_sam_hu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = highlight_post_sam_huClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=highlight_post_sam_huClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sam_hu_highlight_post* updates
    if sam_hu_highlight_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sam_hu_highlight_post.frameNStart = frameN  # exact frame index
        sam_hu_highlight_post.tStart = t  # local t and not account for scr refresh
        sam_hu_highlight_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sam_hu_highlight_post, 'tStartRefresh')  # time at next scr refresh
        sam_hu_highlight_post.setAutoDraw(True)
    if sam_hu_highlight_post.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sam_hu_highlight_post.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            sam_hu_highlight_post.tStop = t  # not accounting for scr refresh
            sam_hu_highlight_post.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sam_hu_highlight_post, 'tStopRefresh')  # time at next scr refresh
            sam_hu_highlight_post.setAutoDraw(False)
    answer_to_draw.fillColor=[.3,.5,.7]
    answer_to_draw.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in highlight_post_sam_huComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "highlight_post_sam_hu"-------
for thisComponent in highlight_post_sam_huComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sam_hu_highlight_post.started', sam_hu_highlight_post.tStartRefresh)
thisExp.addData('sam_hu_highlight_post.stopped', sam_hu_highlight_post.tStopRefresh)
answer_to_draw.setAutoDraw(False)

# ------Prepare to start Routine "SAM_ec_directions"-------
continueRoutine = True
# update component parameters for each repeat
SAM_ec_instructions_key_resp.keys = []
SAM_ec_instructions_key_resp.rt = []
_SAM_ec_instructions_key_resp_allKeys = []
# keep track of which components have finished
SAM_ec_directionsComponents = [SAM_ec_instructions, SAM_ec_instructions_key_resp]
for thisComponent in SAM_ec_directionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SAM_ec_directionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SAM_ec_directions"-------
while continueRoutine:
    # get current time
    t = SAM_ec_directionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SAM_ec_directionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SAM_ec_instructions* updates
    if SAM_ec_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_ec_instructions.frameNStart = frameN  # exact frame index
        SAM_ec_instructions.tStart = t  # local t and not account for scr refresh
        SAM_ec_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_ec_instructions, 'tStartRefresh')  # time at next scr refresh
        SAM_ec_instructions.setAutoDraw(True)
    
    # *SAM_ec_instructions_key_resp* updates
    waitOnFlip = False
    if SAM_ec_instructions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_ec_instructions_key_resp.frameNStart = frameN  # exact frame index
        SAM_ec_instructions_key_resp.tStart = t  # local t and not account for scr refresh
        SAM_ec_instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_ec_instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
        SAM_ec_instructions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SAM_ec_instructions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SAM_ec_instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SAM_ec_instructions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = SAM_ec_instructions_key_resp.getKeys(keyList=None, waitRelease=False)
        _SAM_ec_instructions_key_resp_allKeys.extend(theseKeys)
        if len(_SAM_ec_instructions_key_resp_allKeys):
            SAM_ec_instructions_key_resp.keys = _SAM_ec_instructions_key_resp_allKeys[-1].name  # just the last key pressed
            SAM_ec_instructions_key_resp.rt = _SAM_ec_instructions_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SAM_ec_directionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SAM_ec_directions"-------
for thisComponent in SAM_ec_directionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SAM_ec_instructions.started', SAM_ec_instructions.tStartRefresh)
thisExp.addData('SAM_ec_instructions.stopped', SAM_ec_instructions.tStopRefresh)
# check responses
if SAM_ec_instructions_key_resp.keys in ['', [], None]:  # No response was made
    SAM_ec_instructions_key_resp.keys = None
thisExp.addData('SAM_ec_instructions_key_resp.keys',SAM_ec_instructions_key_resp.keys)
if SAM_ec_instructions_key_resp.keys != None:  # we had a response
    thisExp.addData('SAM_ec_instructions_key_resp.rt', SAM_ec_instructions_key_resp.rt)
thisExp.addData('SAM_ec_instructions_key_resp.started', SAM_ec_instructions_key_resp.tStartRefresh)
thisExp.addData('SAM_ec_instructions_key_resp.stopped', SAM_ec_instructions_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "SAM_ec_directions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SAM_ec_question_2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the select_answer_mouse_4
select_answer_mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
SAM_ec_question_2Components = [SAM_ec_2, choice_num_1_post, choice_num_2_post, choice_num_3_post, choice_num_4_post, choice_num_5_post, choice_num_6_post, choice_num_7_post, choice_num_8_post, choice_num_9_post, select_answer_mouse_4]
for thisComponent in SAM_ec_question_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SAM_ec_question_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SAM_ec_question_2"-------
while continueRoutine:
    # get current time
    t = SAM_ec_question_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SAM_ec_question_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SAM_ec_2* updates
    if SAM_ec_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SAM_ec_2.frameNStart = frameN  # exact frame index
        SAM_ec_2.tStart = t  # local t and not account for scr refresh
        SAM_ec_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAM_ec_2, 'tStartRefresh')  # time at next scr refresh
        SAM_ec_2.setAutoDraw(True)
    
    # *choice_num_1_post* updates
    if choice_num_1_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_1_post.frameNStart = frameN  # exact frame index
        choice_num_1_post.tStart = t  # local t and not account for scr refresh
        choice_num_1_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_1_post, 'tStartRefresh')  # time at next scr refresh
        choice_num_1_post.setAutoDraw(True)
    
    # *choice_num_2_post* updates
    if choice_num_2_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_2_post.frameNStart = frameN  # exact frame index
        choice_num_2_post.tStart = t  # local t and not account for scr refresh
        choice_num_2_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_2_post, 'tStartRefresh')  # time at next scr refresh
        choice_num_2_post.setAutoDraw(True)
    
    # *choice_num_3_post* updates
    if choice_num_3_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_3_post.frameNStart = frameN  # exact frame index
        choice_num_3_post.tStart = t  # local t and not account for scr refresh
        choice_num_3_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_3_post, 'tStartRefresh')  # time at next scr refresh
        choice_num_3_post.setAutoDraw(True)
    
    # *choice_num_4_post* updates
    if choice_num_4_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_4_post.frameNStart = frameN  # exact frame index
        choice_num_4_post.tStart = t  # local t and not account for scr refresh
        choice_num_4_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_4_post, 'tStartRefresh')  # time at next scr refresh
        choice_num_4_post.setAutoDraw(True)
    
    # *choice_num_5_post* updates
    if choice_num_5_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_5_post.frameNStart = frameN  # exact frame index
        choice_num_5_post.tStart = t  # local t and not account for scr refresh
        choice_num_5_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_5_post, 'tStartRefresh')  # time at next scr refresh
        choice_num_5_post.setAutoDraw(True)
    
    # *choice_num_6_post* updates
    if choice_num_6_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_6_post.frameNStart = frameN  # exact frame index
        choice_num_6_post.tStart = t  # local t and not account for scr refresh
        choice_num_6_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_6_post, 'tStartRefresh')  # time at next scr refresh
        choice_num_6_post.setAutoDraw(True)
    
    # *choice_num_7_post* updates
    if choice_num_7_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_7_post.frameNStart = frameN  # exact frame index
        choice_num_7_post.tStart = t  # local t and not account for scr refresh
        choice_num_7_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_7_post, 'tStartRefresh')  # time at next scr refresh
        choice_num_7_post.setAutoDraw(True)
    
    # *choice_num_8_post* updates
    if choice_num_8_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_8_post.frameNStart = frameN  # exact frame index
        choice_num_8_post.tStart = t  # local t and not account for scr refresh
        choice_num_8_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_8_post, 'tStartRefresh')  # time at next scr refresh
        choice_num_8_post.setAutoDraw(True)
    
    # *choice_num_9_post* updates
    if choice_num_9_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choice_num_9_post.frameNStart = frameN  # exact frame index
        choice_num_9_post.tStart = t  # local t and not account for scr refresh
        choice_num_9_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choice_num_9_post, 'tStartRefresh')  # time at next scr refresh
        choice_num_9_post.setAutoDraw(True)
    # *select_answer_mouse_4* updates
    if select_answer_mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        select_answer_mouse_4.frameNStart = frameN  # exact frame index
        select_answer_mouse_4.tStart = t  # local t and not account for scr refresh
        select_answer_mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(select_answer_mouse_4, 'tStartRefresh')  # time at next scr refresh
        select_answer_mouse_4.status = STARTED
        select_answer_mouse_4.mouseClock.reset()
        prevButtonState = select_answer_mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if select_answer_mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = select_answer_mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [choice_num_1_post,choice_num_2_post,choice_num_3_post,choice_num_4_post,choice_num_5_post,choice_num_6_post,choice_num_7_post,choice_num_8_post,choice_num_9_post]:
                    if obj.contains(select_answer_mouse_4):
                        gotValidClick = True
                        select_answer_mouse_4.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SAM_ec_question_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SAM_ec_question_2"-------
for thisComponent in SAM_ec_question_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SAM_ec_2.started', SAM_ec_2.tStartRefresh)
thisExp.addData('SAM_ec_2.stopped', SAM_ec_2.tStopRefresh)
thisExp.addData('choice_num_1_post.started', choice_num_1_post.tStartRefresh)
thisExp.addData('choice_num_1_post.stopped', choice_num_1_post.tStopRefresh)
thisExp.addData('choice_num_2_post.started', choice_num_2_post.tStartRefresh)
thisExp.addData('choice_num_2_post.stopped', choice_num_2_post.tStopRefresh)
thisExp.addData('choice_num_3_post.started', choice_num_3_post.tStartRefresh)
thisExp.addData('choice_num_3_post.stopped', choice_num_3_post.tStopRefresh)
thisExp.addData('choice_num_4_post.started', choice_num_4_post.tStartRefresh)
thisExp.addData('choice_num_4_post.stopped', choice_num_4_post.tStopRefresh)
thisExp.addData('choice_num_5_post.started', choice_num_5_post.tStartRefresh)
thisExp.addData('choice_num_5_post.stopped', choice_num_5_post.tStopRefresh)
thisExp.addData('choice_num_6_post.started', choice_num_6_post.tStartRefresh)
thisExp.addData('choice_num_6_post.stopped', choice_num_6_post.tStopRefresh)
thisExp.addData('choice_num_7_post.started', choice_num_7_post.tStartRefresh)
thisExp.addData('choice_num_7_post.stopped', choice_num_7_post.tStopRefresh)
thisExp.addData('choice_num_8_post.started', choice_num_8_post.tStartRefresh)
thisExp.addData('choice_num_8_post.stopped', choice_num_8_post.tStopRefresh)
thisExp.addData('choice_num_9_post.started', choice_num_9_post.tStartRefresh)
thisExp.addData('choice_num_9_post.stopped', choice_num_9_post.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = select_answer_mouse_4.getPos()
buttons = select_answer_mouse_4.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [choice_num_1_post,choice_num_2_post,choice_num_3_post,choice_num_4_post,choice_num_5_post,choice_num_6_post,choice_num_7_post,choice_num_8_post,choice_num_9_post]:
        if obj.contains(select_answer_mouse_4):
            gotValidClick = True
            select_answer_mouse_4.clicked_name.append(obj.name)
thisExp.addData('select_answer_mouse_4.x', x)
thisExp.addData('select_answer_mouse_4.y', y)
thisExp.addData('select_answer_mouse_4.leftButton', buttons[0])
thisExp.addData('select_answer_mouse_4.midButton', buttons[1])
thisExp.addData('select_answer_mouse_4.rightButton', buttons[2])
if len(select_answer_mouse_4.clicked_name):
    thisExp.addData('select_answer_mouse_4.clicked_name', select_answer_mouse_4.clicked_name[0])
thisExp.addData('select_answer_mouse_4.started', select_answer_mouse_4.tStart)
thisExp.addData('select_answer_mouse_4.stopped', select_answer_mouse_4.tStop)
thisExp.nextEntry()
answer_to_draw = []
for answer in [choice_num_1_post,choice_num_2_post,choice_num_3_post,choice_num_4_post,choice_num_5_post,choice_num_6_post,choice_num_7_post,choice_num_8_post,choice_num_9_post]:
    if select_answer_mouse_4.isPressedIn(answer):
        answer_to_draw = answer
# the Routine "SAM_ec_question_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "highlight_sam_ec_post_choice"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
highlight_sam_ec_post_choiceComponents = [sam_ec_post_highlight]
for thisComponent in highlight_sam_ec_post_choiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
highlight_sam_ec_post_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "highlight_sam_ec_post_choice"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = highlight_sam_ec_post_choiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=highlight_sam_ec_post_choiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sam_ec_post_highlight* updates
    if sam_ec_post_highlight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sam_ec_post_highlight.frameNStart = frameN  # exact frame index
        sam_ec_post_highlight.tStart = t  # local t and not account for scr refresh
        sam_ec_post_highlight.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sam_ec_post_highlight, 'tStartRefresh')  # time at next scr refresh
        sam_ec_post_highlight.setAutoDraw(True)
    if sam_ec_post_highlight.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sam_ec_post_highlight.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            sam_ec_post_highlight.tStop = t  # not accounting for scr refresh
            sam_ec_post_highlight.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sam_ec_post_highlight, 'tStopRefresh')  # time at next scr refresh
            sam_ec_post_highlight.setAutoDraw(False)
    answer_to_draw.fillColor=[.3,.5,.7]
    answer_to_draw.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in highlight_sam_ec_post_choiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "highlight_sam_ec_post_choice"-------
for thisComponent in highlight_sam_ec_post_choiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sam_ec_post_highlight.started', sam_ec_post_highlight.tStartRefresh)
thisExp.addData('sam_ec_post_highlight.stopped', sam_ec_post_highlight.tStopRefresh)
answer_to_draw.setAutoDraw(False)

# ------Prepare to start Routine "total_points_end_experiment"-------
continueRoutine = True
# update component parameters for each repeat
final_total_points.setText(main_total_points)
exit_task.keys = []
exit_task.rt = []
_exit_task_allKeys = []
# keep track of which components have finished
total_points_end_experimentComponents = [final_total_points, rest_of_text, exit_task]
for thisComponent in total_points_end_experimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
total_points_end_experimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "total_points_end_experiment"-------
while continueRoutine:
    # get current time
    t = total_points_end_experimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=total_points_end_experimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *final_total_points* updates
    if final_total_points.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        final_total_points.frameNStart = frameN  # exact frame index
        final_total_points.tStart = t  # local t and not account for scr refresh
        final_total_points.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(final_total_points, 'tStartRefresh')  # time at next scr refresh
        final_total_points.setAutoDraw(True)
    
    # *rest_of_text* updates
    if rest_of_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_of_text.frameNStart = frameN  # exact frame index
        rest_of_text.tStart = t  # local t and not account for scr refresh
        rest_of_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_of_text, 'tStartRefresh')  # time at next scr refresh
        rest_of_text.setAutoDraw(True)
    
    # *exit_task* updates
    waitOnFlip = False
    if exit_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exit_task.frameNStart = frameN  # exact frame index
        exit_task.tStart = t  # local t and not account for scr refresh
        exit_task.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exit_task, 'tStartRefresh')  # time at next scr refresh
        exit_task.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(exit_task.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(exit_task.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if exit_task.status == STARTED and not waitOnFlip:
        theseKeys = exit_task.getKeys(keyList=None, waitRelease=False)
        _exit_task_allKeys.extend(theseKeys)
        if len(_exit_task_allKeys):
            exit_task.keys = _exit_task_allKeys[-1].name  # just the last key pressed
            exit_task.rt = _exit_task_allKeys[-1].rt
            # was this correct?
            if (exit_task.keys == str('')) or (exit_task.keys == ''):
                exit_task.corr = 1
            else:
                exit_task.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in total_points_end_experimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "total_points_end_experiment"-------
for thisComponent in total_points_end_experimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('final_total_points.started', final_total_points.tStartRefresh)
thisExp.addData('final_total_points.stopped', final_total_points.tStopRefresh)
thisExp.addData('rest_of_text.started', rest_of_text.tStartRefresh)
thisExp.addData('rest_of_text.stopped', rest_of_text.tStopRefresh)
# check responses
if exit_task.keys in ['', [], None]:  # No response was made
    exit_task.keys = None
    # was no response the correct answer?!
    if str('').lower() == 'none':
       exit_task.corr = 1;  # correct non-response
    else:
       exit_task.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('exit_task.keys',exit_task.keys)
thisExp.addData('exit_task.corr', exit_task.corr)
if exit_task.keys != None:  # we had a response
    thisExp.addData('exit_task.rt', exit_task.rt)
thisExp.addData('exit_task.started', exit_task.tStartRefresh)
thisExp.addData('exit_task.stopped', exit_task.tStopRefresh)
thisExp.nextEntry()
# the Routine "total_points_end_experiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
