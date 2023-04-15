#from sense_hat import SenseHat
import time
import pandas as pd
import numpy as np  
import tensorflow as tf

#each action will collect invidiaul data
#press joystick to switch action

#create a pand dataframe and defin the columns
fall = pd.read_csv('walk2.csv')
model = tf.keras.models.load_model('all models/teacher_model0_device2_aggregate.h5')
while True:
    fall = fall.values.reshape((fall.shape[0], fall.shape[1]))
    
    #print size of dataframe
    print(fall.shape)
    fall = np.array_split(fall, fall.shape[0] / 100)

    # for each chunk, predict fall and if 50% of the predictions are 1, then the fall is
    for i in range(len(fall)):
        pred = model.predict(fall[i])
        # if 50% of the predictions are 1, then the fall is predicted
        pred_value = np.sum(pred) >= 0.5 * pred.shape[0]
        print("predict value", pred_value)
        if pred_value:
            print("Fall detected") 
            #display on text
            #call Home Assistant API to send notification
            time.sleep(30) #30 seconds delay to allow the user to get up
        else:
            print("all set")
    time.sleep(1)
    
    print("end of prediction")
    break
        
        
