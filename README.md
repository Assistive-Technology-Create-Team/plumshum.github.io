# Navigating this Repository
This is where we organize the code for our project. This is a README file in the repository. It informs you what this repository is all out.
Repositories track the code and its history. Code can be managed and changed in different versions. To nagivate changes and different versions, Github uses a system of managing *branches* and utilizing *pulls and commits*

# Files and Descriptions:
## FallAllD: 
  a folder that holds the raw data from FallAllD dataset. 
## archive:
  a folder that holds the csv files from kaggle
## normalized
  a folder that holdes the csv files that contain the normalized data from the kaggle data from folder archive: [DeviceOrientation, AccX_fft, AccY_fft, AccZ_ftt, Label]
## saved_model
  a folder that stores the most recent saved_model. each time a new model is saved, it gets overrided into the file lstm_model.h5
## Instructions.md
  instructions for setting up raspberry pi on vscode
## machine learning.ipynb
  it's where the machine learning does it job duh
## script.py
  using the saved model, it tests the model with raspberry pi data collected 

# What is the MIT Create [Challenge](https://sites.google.com/view/beaver-works-assistive-tech/create-challenge/the-challenge)?

# Our Project
## Summary
Create an assistive piece of technology that can sense when a senior is in danger, and communicate the situation to emergency workers

## Major Components
There are three major components
1) Sensors that detect *falling* movement
2) A device that connects the sensor to a communicative application
3) The program

*to articulate: as of now we are planning to program either in Raspberry Pi + Typescript, or potentially Python*

## Sample Projects
Please look at these sample projects to understand what we are doing:

**Our current ideas and block diagrams [slideshow](https://docs.google.com/presentation/d/1aa9CrvCU01R1dKsot-3q9yuEzjVwWQEgsKHpUEQwsT0/edit?usp=sharing)**

**Understanding Rasberry Pi**
- [Intro Project  w/ Raspberry Pi](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8)
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/accessories/sense-hat.html)
- [Raspberry Pi Official Website](https://www.raspberrypi.com/)

**Sensor Data**
- [Install Homebridge on Macs](https://github.com/homebridge/homebridge/wiki/Install-Homebridge-on-macOS)
- [How the Accelerometer and Fall Detection System works](https://iotdesignpro.com/projects/iot-based-fall-detection-system-using-nodemcu-esp8266-and-accelerometer-mpu6050)
