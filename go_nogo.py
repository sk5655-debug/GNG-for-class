##go no go

#Hi, I’m trying to adapt a GO/NOGO protocol from Price et al., 2016. Food-specific response inhibition,
#dietary restraint and snack intake in lean and overweight/obese adults.
#The task consists in 50 trials (40 go and 10 no-go). During go trials the 
#subject should press a key as fast as possible. During no-go trials, no key should be pressed. 
#Each trial is composed by an image presented for 750ms and was separated by a blank screen for 500 ms 
#and preceded by a fixation cross for 500 ms. The sequence of go/nogo stimuli are predetermined. 
#Two set of images are used: 10 go images (each one is presented 4 times) and 10 no-go images 
#(each one is presented one time). Image order should be randomized across subjects.
# we are going to change for anorexia nervosa intervention

import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data
import random

exp_info = {'participant_nr': '', 'age': '21'}
dlg = DlgFromDict(exp_info)

p_name= exp_info['participant_nr']

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1200, 800), fullscr=False)

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=False)

#Instructions
instruct_txt = """ 
You will see pictures of foods on each trial. Press the space bar when you see GO. 
DO NOT press anything when you see NO-GO.
To continue, hit the return key.
"""
instruct=TextStim(win,instruct_txt,pos=(0.0,0.05))
instruct.draw()
win.flip()
# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'return' in keys:
        break  # break out of the loop!

# Initialize a (global) clock
clock = Clock()
f_list = f'/Users/stutikarna/Desktop/coding course/L7/HF_LF_60.csv'
foods = pd.read_csv(f_list)
hf = foods[foods['fat']==1]
lf = foods[foods['fat']==0]
lf = lf.sample(frac=0.4) #randomly samples through the list for the frac of 0.4
hf = hf.sample(frac=0.4)
trial_foods=pd.concat([lf,lf,lf,lf,hf])
trial_foods = trial_foods.sample(frac=1) #1 is 100% sampling through the entire list
cue_1 = "Go"
cue_2 = "No-Go"
kb=Keyboard()

for i in range(0,len(trial_foods)): #whole dataframe
    trial=trial_foods.iloc[i] # only 'i=integer-location' will change go from 0 to 50
    print(trial)
    t=TextStim(win,"+")
    t.draw()
    win.flip()
    wait(0.5)
    path = '/Users/stutikarna/Desktop/coding course/L7/stimuli/' + trial.food
    print(trial.fat)
    if trial.fat==1:
        stim_txt1 = TextStim(win, cue_2, pos=(0.0, 0.5))
        correct = "nogo"
    else: 
        stim_txt1 = TextStim(win, cue_1, pos=(0.0, 0.5))
        correct = "go"
    im=ImageStim(win, path)
    
    t_clock=Clock()
    response = "nogo"
    rt="NA"
    while t_clock.getTime() < .75:
        im.draw()
        stim_txt1.draw()
        win.flip()
        keys = kb.getKeys(['space','escape'], waitRelease=False)
        if keys:
            resp = keys[0].name
            rt = keys[0].rt
            if resp == 'escape':
                win.close()
                quit()
            else:
                response = "go"

    win.flip()
    wait(.5)
    trial_foods['response']=response
    trial_foods['rt']= rt
    trial_foods['correct_response'] = correct

trials.save(f"{p_name}_gonogo.csv")

## tasks
# 1. figure out what is happening in the task & add instructions
# 2. we need to add go-nogo! How would we do that?

    
