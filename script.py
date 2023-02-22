from sense_hat import SenseHat
from sklearn.metrics import accuracy_score
import tensorflow as tf
import glob
import os
import numpy as np
import pandas as pd
sense = SenseHat()

# load the model from saved_model
model = tf.keras.models.load_model('saved_model/my_model')
# predict the outputs using the model
predictions = model.predict(x_test)
  # x_test : the data collected  from the accelerometer
  # predicted : the labels and the confidence level of the prediction
# print the accuracy
print("Accuracy: ", accuracy_score(y_test, predictions))
# print the confidence level and label of each prediction

correct = 0
for i in range(len(predictions)):
    print("Confidence level: ", predictions[i], "Label: ", y_test[i])
    if predictions[i] > .75: correct+=1
print("Confidence Level Accurate Percentage:", correct/len(predictions) * 100)

#TODO create a function for collecting data 
#TODO create a parameter for the humber of labels to include for the collection data function
def data_collection():
  os.makedirs('./normalized_raspberrypi', exist_ok=True)
  labels = ['runfall', 'downSit', 'freeFall', 'runSit', 'walkFall', 'walkSit']
  for label in labels:
      #read all csv files in the directory "raspberry_pi_data' + label, delimit by ';'
      files = glob.glob('./raspberry_pi_data/' + label + '/*.csv')
      df = pd.concat([pd.read_csv(f, sep=';') for f in files], ignore_index=True)
      # assign label to df column 'Label'
      df['Label'] = label
      # save columns 'DeviceOrientation', 'AccelerationX', 'AccelerationY', 'AccelerationZ', 'Label' to a new csv file
      df[['DeviceOrientation', 'AccelerationX', 'AccelerationY', 'AccelerationZ', 'Label']].to_csv('./normalized_raspberrypi/' + label + '.csv', index=False)
      
      
  df = pd.concat([pd.read_csv(f) for f in glob.glob('./normalized_raspberrypi/*.csv')], ignore_index = True)
  return df 

#TODO create a function for normalizing data
def data_normalize(df):
  for c in ['AccelerationX', 'AccelerationY', 'AccelerationZ']:
    df[c + '_fft'] = np.fft.fft(df[c])

  #debug purposes
  for c in df.columns:
    print(c)

  return df