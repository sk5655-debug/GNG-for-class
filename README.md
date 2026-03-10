Importing all the required libraries

Ask for participant info

Store that info

Initialize the window and mouse

Present instructions for the participant. only continue if they hit the return key

Initialize the keyboard to wait for the participant's response before moving to the next screen

Initialize the clock 

Get the list of high fat and low fat foods from the CSV file 

Assign HFNLF then make it randomly sample through the list for a fraction of .4 or 40

Concatenate the list with 4LF presentations and one HF presentation 

Sample through this entire list by using 100% or frac=1 which means that LF will be presented 40 times and HF will be presented 10 times 

resulting in a total of 50 trials 

Cue1 as go and Cue2 as no go and call the keyboard 

Run through the entire data frame and then locate i to go from 0 to 50

Present the fixation cross for 500 ms before every trial

Assign the path for the pictures that have to be presented according to the csv list

In this For loop, if the trial is high fat, then cue 2 of Nogo is presented and the correct response is to not press anything

Else, Cue1 of Go is presented, and the correct response would be to press the button

Make the image stimuli

Call the clock and if the response is no go then the resulting reaction time will be NA

In the While loop, for around 750 ms, present the images according to the list and then present the cue2 as no go according to the criteria defined in before

In this if condition, assign the keys for space and escape as two keys that can be pressed

If the response is the space, then the reaction time will be stored, and if the response is escape, then the window will close and the experiment will quit 

Else, then the response will be go

Wait for 500 ms

Store response, reaction time and correctresponse

Finally save it to a CSV file.
