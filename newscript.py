import pandas as pd
import numpy as np  
import tensorflow as tf
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
red = (255,0,0)
green = (0,255,0)

fall = pd.read_csv('fall.csv')
fall = fall[['Device', 'Acc_x','Acc_y','Acc_z', 'Gyr_x', 'Gyr_y', 'Gyr_z', 'Bar_x', 'Bar_y']]
# load model from 'model0_device2_aggregate.h5' file
model = tf.keras.models.load_model('student_model4_device2_aggregate_coach.h5')

fall = fall.values.reshape((fall.shape[0], 1, fall.shape[1]))
# split fall into chuncks, each chuck has 100 rows and predict and loop on all the chuncks
fall = np.array_split(fall, fall.shape[0] / 100)
sense.clear(green)
input("Press Enter to start predicting...")

# for each chunk, predict fall and if 50% of the predictions are 1, then the fall is
for i in range(len(fall)):
    pred = model.predict(fall[i])
    # if 50% of the predictions are 1, then the fall is predicted
    if np.sum(pred) >= 0.5 * pred.shape[0]:
        sense.clear(red)
        #speaker makes sound
        
    else:
        sense.clear(green)
sense.clear()