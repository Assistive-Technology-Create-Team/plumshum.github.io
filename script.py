import numpy as np
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Flatten, Conv1D, MaxPooling1D
from tensorflow.keras.losses import BinaryCrossentropy, KLDivergence
import sklearn.model_selection
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
def main():
  make_predictions()

def data_collection():
  # right now only using testing data
    # get the data from the csv file in the data folder normalized_raspberrypi 
    #df = pd.read_csv('/normalized_raspberrypi.csv')
  df = pd.read_csv('FallAllD2.csv')
  # convert all columns to float32
  df = df.astype('float32')
  print("finished collecting data")
  return df 

#might use when we use actually raspberry pi data
def data_normalize(df):
  for c in ['AccelerationX', 'AccelerationY', 'AccelerationZ']:
    df[c + '_fft'] = np.fft.fft(df[c])

  #debug purposes
  for c in df.columns:
    print(c)
  return df

#might use when we use actually raspberry pi data
def data_categorical(df):
  # convert categorical data to numerical data
  df['Label'] = df['Label'].astype('category')
  df['Label'] = df['Label'].cat.codes
  
  #debug purposes
  print(df['Label'].unique())

  # convert column `DeviceOrientation` to numerical data
  df['DeviceOrientation'] = df['DeviceOrientation'].astype('category')
  df['DeviceOrientation'] = df['DeviceOrientation'].cat.codes

  return df

def data_label(df):
    # add a new column called "IsFall" that is 1 if the ActivityID > 100, and 0 if it is not
    df['IsFall'] = df['ActivityID'].apply(lambda x: 1 if x > 100 else 0)
    return df

def data_split(df): # NOT SURE EXACTLY HOW YOU WANT TO SPLIT IT
  # take a section of the df dataframe to test the model. not compatible with raspberry pi data
  # x_test is df from 0 to 1000, excluding the column IsFall
  x_test = df.iloc[0:1000, 0:10]
  # y_test is df from 0 to 1000, only the column IsFall
  y_test = df.iloc[0:1000, 10]
  scaler = StandardScaler()
  x = scaler.fit_transform(x)
  x = x.reshape((x.shape[0], 1, x.shape[1]))
  return x_test, y_test

def model_run(x_test, y_test, num):
  # load the model from saved_model
  model_name = 'student_model' + str(num) + '.h5' #you can switch it to teacher model to test it out too
  model = tf.keras.models.load_model('all models/' + model_name)
  # predict the outputs using the model
  predictions = model.predict(x_test)
    # x_test : the data collected from the raspberry pi
    # predicted : the labels and the confidence level of the prediction
  # print the accuracy of the predictions
  accuracy = model.evaluate(x_test, y_test)
  print("Accuracy:", accuracy)

  # print the confidence level and label of each prediction
  correct = 0
  for i in range(len(predictions)):
      print("Confidence level: ", predictions[i], "Label: ", y_test[i])
      if predictions[i] > .75: correct+=1
  print("Confidence Level Accurate Percentage:", correct/len(predictions) * 100)
  #create a confusion matrix
  print("Confusion Matrix")
  y_pred = model.predict(x_test)
  y_pred = (y_pred > 0.5)
  confusion_mtx = confusion_matrix(y_test, y_pred)
  confusion_mtx_percent = confusion_mtx / confusion_mtx.sum(axis=1)[:, np.newaxis]
  print(confusion_mtx_percent)

  #save the accuracy in a csv file, with also the model_name as title of csv file
  df = pd.DataFrame({'Accuracy': [accuracy]})
  df.to_csv('all models/' + model_name + '.csv', index=False)

def make_predictions():
  df = data_collection()
  #df = data_normalize(df) #might use when we use actually raspberry pi data
  #df = data_categorical(df) #might use when we use actually raspberry pi data
  df = data_label(df) #adds IsFall column
  x_test, y_test = data_split(df)
  model_run(x_test, y_test, 1) #change the number to the model you want to run

if __name__ == "__main__":
  print("this ran")
  main()
