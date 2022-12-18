#https://www.kaggle.com/harnoor343/fall-detection-accelerometer-data
import numPy as np
import pandas as pd 
import glob
import os 
# create a new directory called 'kaggle_normalized', ignore it if it already exists
os.makedirs('kaggle_normalized', exist_ok=True)

labels = ['runfall', 'downSit', 'freeFall', 'runSit', 'walkFall', 'walkSit']
for l in labels:
    #read all csv files in the director "./kaggle_data/" + l, delimit by ';'
    #this is different from chen human min project
    files = glob.glob('./kaggle_data/' + l + '/*.csv')
    #assign l to to df column 'Label'
    df = pd.concat([pd.read_csv(f, sep=';') for f in files], ignore_index=True)
    # assign l to df column 'Label'
    df['Label'] = l
    # save columns 'DeviceOrientation', 'AccelerationX', 'AccelerationY', 'AccelerationZ', 'Label' to a new csv file
    df[['DeviceOrientation', 'AccelerationX', 'AccelerationY', 'AccelerationZ', 'Label']].to_csv('./kaggle_normalized/' + l + '.csv', index=False)

df = pd.concat([pd.read_csv(f) for f in glob.glob('./kaggle_normalized/*.csv')], ignore_index = True)
columns = ['DeviceOrientation', 'AccelerationX', 'AccelerationY', 'AccelerationZ', 'Label']

# for each column in 'Accerlation', 'AccelerationY', 'AccelerationZ', and a new column that is the fft of the original column
for c in ['AccelerationX', 'AccelerationY', 'AccelerationZ']:
    df[c + '_fft'] = np.fft.fft(df[c])

# plot the first 100 column 'Acce


