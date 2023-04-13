# Navigating this Repository
This is where we organize the code for our project. This is a README file in the repository. It informs you what this repository is all out.
Repositories track the code and its history. Code can be managed and changed in different versions. To nagivate changes and different versions, Github uses a system of managing *branches* and utilizing *pulls and commits*
Most updated branch is the **main** branch

# Overall Process:
*For running machine learning*
1. Upload FallAllD2.csv and machine learning.ipynb to Google Colab
2. Run machine learning.ipynb to create the machine learning model. Right now models are already created so you don't need to do this step. 
*For running prediction script*
4. run sensordata.py to run the prediction script. it will automaticaly collect data from the raspberry pi's sensehat

*For Connecting Raspberry Pi* 

link to [instructions](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8)
1. ctrl p (microsoft)
2. command shift p (linux)
3. remote ssh either connect or add new host
  - username@ip address
4. input password 
5. connect to linux
6. enter password

7. on raspberry pi terminal:
- connect to wifi 
- ifconfig

8. to run on local terminal:
- open terminal
type:
   -  python3 name of file
- to stop file:
   -  ctrl c 

# Files and Descriptions:
## all models
  folder that holds all the models 
  - teacher models 
     1. `teacher_model0_device2_acc_aggregate` is the current teacher model AND model being tested on `sensordata.py`
     2. `teacher_model0_device2_aggregate` is the teacher model with all three sensors 
  - student models
    they all hold aggregate data from device 2 (wrist data) 
    they are numbered with from 0-6. a number corresponding to how many sensors are configured. Below is the 
    pseudo code snippet that you can also find in `machine learning.ipynb` (in python) that explains the layout

    0: ['Device','Acc_x','Acc_y','Acc_z', 'Gyr_x', 'Gyr_y', 'Gyr_z', 'Bar_x', 'Bar_y']

    1: ['Device','Acc_x','Acc_y','Acc_z', 'Gyr_x', 'Gyr_y', 'Gyr_z']

    2: ['Device','Gyr_x', 'Gyr_y', 'Gyr_z', 'Bar_x', 'Bar_y']

    3: ['Device','Acc_x','Acc_y','Acc_z', 'Bar_x', 'Bar_y']

    4: ['Device','Acc_x','Acc_y','Acc_z']

    5: ['Device','Gyr_x', 'Gyr_y', 'Gyr_z']

    6: ['Device','Bar_x', 'Bar_y']
    
## FallAllD: 
  a folder that holds the raw data from FallAllD dataset. It is stored in csv files

  *M. Saleh, M. Abbas and R. L. B. Jeannès, "FallAllD: An Open Dataset of Human Falls and Activities of Daily Living for Classical and Deep Learning Applications," in IEEE Sensors Journal, doi: 10.1109/JSEN.2020.3018335.*

  ## scripts
  a folder that holds the description and code for the data extraction from the FALLALLID dataset
   ### data_extract.py
   extracts data from all csv files from `FallAllID` and turns it into a panda dataframe on a csv file for `machinelearning.ipynb`
   this was modified from FallALlID's data extraction file. 
   ### Plot_FallAllD_Record.m
   file from FALLALLID website that provides an example of the data extraction (From their original website)
## Sensor and Sound Description
a text file that describes the methodology of the sensors and sound in our product
## machine learning.ipynb
  machine learning modeling on jupyter notebook
  if your device doesn't have GPU, you can upload the jupyter notebook onto Google Colab
  In different branches there are different models. Right now there are 4 models:
   1. Simple Neural Network Model
   2. LSTM Model with Kaggle Data
   3. LSTM Model with FallAllD data
   4. LSTM Model with Knowledge Distillation [MAIN BRANCH]
## sensordata.py
  where Accelerometer and Gyroscope data is collected using raspberry pi's sensor 
  then, the data is run through the model and predictions are made 
## test_student_model.py
testing python file to debug our student model
# What is the MIT Create [Challenge](https://sites.google.com/view/beaver-works-assistive-tech/create-challenge/the-challenge)?

# Our Project
## Summary
Create an assistive piece of technology that can sense when a senior is in danger, and contacts for help

The base product works without wifi connection
The entire product works will work with wifi connection

## Major Components
There are three major components
1) Sensors that detect *falling* movement
2) A device that connects the sensor to a communicative application
3) The program

*to articulate: as of now we are planning to program either in Raspberry Pi 4  + Python*

## Sample Projects
Please look at these sample projects to understand what we are doing:

**Our recent [slideshow](https://docs.google.com/presentation/d/1UKiu0qB-KCjSiXp1Kg6J7CR_UiFspL7GR_qOvW0-YNU/edit#slide=id.g1d6b888cecd_3_1340)**
**Understanding Rasberry Pi**
- [Intro Project  w/ Raspberry Pi](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8)
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/accessories/sense-hat.html)
- [Raspberry Pi Official Website](https://www.raspberrypi.com/)


## Citations
M. Saleh, M. Abbas and R. L. B. Jeannès, "FallAllD: An Open Dataset of Human Falls and Activities of Daily Living for Classical and Deep Learning Applications," in IEEE Sensors Journal, doi: 10.1109/JSEN.2020.3018335.

[FallAllID Dataset](https://ieee-dataport.org/open-access/fallalld-comprehensive-dataset-human-falls-and-activities-daily-living)