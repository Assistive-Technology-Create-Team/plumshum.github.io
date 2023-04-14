import pandas as pd
import numpy as np  
#import tensorflow as tf
#load model student_model4_device2_aggregate_coach in the folder 'all models'
fall = pd.DataFrame(columns=['Device',
                            'Acc_x','Acc_y', 'Acc_z' 
                            ])
fall.append({'Device': [2], 'Acc_x': [0.1], 'Acc_y': [0.2], 'Acc_z': [0.3]}, ignore_index=True)
fall.append({'Device': [2], 'Acc_x': [0.1], 'Acc_y': [0.2], 'Acc_z': [0.3]}, ignore_index=True)
fall.append({'Device': [2], 'Acc_x': [0.1], 'Acc_y': [0.2], 'Acc_z': [0.3]}, ignore_index=True)
fall.append({'Device': [2], 'Acc_x': [0.1], 'Acc_y': [0.2], 'Acc_z': [0.3]}, ignore_index=True)
fall.append({'Device': [2], 'Acc_x': [0.1], 'Acc_y': [0.2], 'Acc_z': [0.3]}, ignore_index=True)

#go through columns and print out the values
for index, row in fall.iterrows():
    print("anything running?")
    print(row['Acc_x'], row['Acc_y'], row['Acc_z'])



#seems i have to set keras loss to the custom loss function i created
