from sklearn.metrics import accuracy_score
import sklearn.model_selection
import tensorflow as tf
import glob
import os
import numpy as np
import pandas as pd

def main():
  make_predictions()

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

#TODO create a function for turning the data into categorical data
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

def data_split(df):
  # can you drop accx, accy, and accz?
  x = np.array(df.drop(['Label'], 1)) #drops row 'Label'
  y = np.array(df["Label"])

  #TODO CONFIRM IF I CAN CHANGE X_TRAIN RESHAPED FOR EARLIER
  #Spliting Data
  x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size = 0.3)

  # reshape training and testing data
  y_train = np.array(y_train).reshape(-1,1) # (-1,1) because our data has a single feature, and a 'n' amount of rows
  x_train = np.array(x_train).reshape(x_train.shape[0], x_train.shape[1], 1)
  y_test = np.array(y_test).reshape(-1,1) # (-1,1) bec  ause our data has a single feature, and a 'n' amount of rows
  x_test = np.array(x_test).reshape(x_test.shape[0], x_test.shape[1], 1)
  
  return x_train, x_test, y_train, y_test

def model_run(x_test, y_test):
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

def make_predictions():
  df = data_collection()
  df = data_normalize(df)
  df = data_categorical(df)
  x_train, x_test, y_train, y_test = data_split(df)
  model_run(x_test, y_test)

if __name__ == "__main__":
  print("this ran")
  main()
