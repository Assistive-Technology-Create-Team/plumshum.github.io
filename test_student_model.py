import pandas as pd
import numpy as np  
import tensorflow as tf
#load model student_model4_device2_aggregate_coach in the folder 'all models'
fall = pd.DataFrame(columns=['Device',
                            'Acc_x','Acc_y', 'Acc_z' 
                            ])
fall = fall.append({'Device': [2], 'Acc_x': [0.1], 'Acc_y': [0.2], 'Acc_z': [0.3]}, ignore_index=True)
fall = fall.append({'Device': [2], 'Acc_x': [0.1], 'Acc_y': [0.2], 'Acc_z': [0.3]}, ignore_index=True)
fall = fall.append({'Device': [2], 'Acc_x': [0.1], 'Acc_y': [0.2], 'Acc_z': [0.3]}, ignore_index=True)
model = tf.keras.models.load_model('teacher_model4_device2_aggregate.h5')

#go through columns and print out the values
for index, row in fall.iterrows():
    print("anything running?")
    print(row['Acc_x'], row['Acc_y'], row['Acc_z'])


fall = fall.values.reshape((fall.shape[0], fall.shape[1]))

#print size of dataframe
print(fall.shape)
fall = np.array_split(fall, fall.shape[0] / 100)

#input("Press Enter to start predicting...")

# for each chunk, predict fall and if 50% of the predictions are 1, then the fall is
for i in range(len(fall)):
    pred = model.predict(fall[i])
    # if 50% of the predictions are 1, then the fall is predicted
    pred_value = np.sum(pred) >= 0.5 * pred.shape[0]
    if pred_value:
        
        print("Fall detected") 
        #display on text
        
        #call Home Assistant API to send notification
       # time.sleep(30) #30 seconds delay to allow the user to get up
    else:
        print("all set")
print("predict value", pred_value)


fall = pd.DataFrame(columns=['Device', 'Acc_x','Acc_y', 'Acc_z'])
        

#seems i have to set keras loss to the custom loss function i created
