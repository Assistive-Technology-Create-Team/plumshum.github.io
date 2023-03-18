# NEW VERSION: FallAllD files to Python struct

# Hannah's Comment: takes data and turns in to panda dataframe, and it's saved in a pickle file.
#The pickle file is called FallAllD.pkl
import os
from numpy import genfromtxt
import numpy as np
import pandas as pd 

os.chdir('..')
oldDir=os.getcwd()
ParentDir=os.getcwd()
# join ParentDir and FallAllD to FP
FP = os.path.join(ParentDir, "FallAllD")
os.chdir(FP)

FileNamesAll=os.listdir(FP)
FileNames=[]
for f_name in FileNamesAll:
    if f_name.endswith('_A.dat'):
        FileNames.append(f_name)
LL=len(FileNames)

l_SubjectID=[]
l_Device=[]
l_ActivityID=[]
l_TrialNo=[]
l_Acc=[]
l_Gyr=[]
#l_Mag=[] not used
#l_Bar=[] not used

for i in range(LL):
    f_name=FileNames[i]
    SubjectID=int(f_name[1:3])    
    l_SubjectID.append(np.float32(SubjectID))
    ActivityID=int(f_name[8:11])    
    l_ActivityID.append(np.float32(ActivityID))
    TrialNo=int(f_name[13:15])    
    l_TrialNo.append(np.float32(TrialNo))
    Device=''
    if(int(f_name[5])==2): #Means they used 'wrist' device
        #print("Device is neck")
        Device='Neck'
        l_Device.append(Device)
    else: 
        continue
        if (int(f_name[5])==1):
            Device='Wrist' 
        else:
            Device='Waist'  
    
    #Biggest change: Instead of storing accelerometer data as one unit, we split and store it as three separate columns
    df_acc = pd.read_csv(f_name, header=None, sep=',', names=['Acc_x','Acc_y', 'Acc_z'])
    chArr=list(f_name)
    chArr[16]='G'
    f_name="".join(chArr)    
    df_gyr = pd.read_csv(f_name, header=None, sep=',', names=['Gyr_x','Gyr_y', 'Gyr_z'])
    l_Gyr.append(np.int16(genfromtxt(f_name, delimiter=',')))

    df = pd.concat([df_acc, df_gyr], axis=1)
    df['SubjectID'] = SubjectID
    df['Device'] = Device
    df['ActivityID'] = ActivityID
    df['TrialNo'] = TrialNo

    #Not used
    #chArr[16]='M'
    #f_name="".join(chArr)    
    #l_Mag.append(np.int16(genfromtxt(f_name, delimiter=',')))
    #chArr=list(f_name)
    #chArr[16]='B'
    #f_name="".join(chArr)    
    #l_Bar.append(genfromtxt(f_name, delimiter=','))

    print(f'File  {i+1}  out of {len(FileNames)}')
os.chdir(oldDir)

#This create the panda dataframe
FallAllD = df

# Debuggin Tool: extract the data from the dataframe and use columns 'SubjectID', 'Device','ActivityID','TrialNo','Acc'(3),'Gyr'(3)
def extract_data(df, col_name):
    print(df[col_name].values.tolist())
    return df[col_name].values.tolist()

#Pickle: Serializing and deserializing a Python object structure
FallAllD.to_pickle('FallAllD.pkl')

#NOT USING. Write the contained data to an HDF5 file using HDFStore.
#FallAllD.to_hdf('FallAllD.h5', key='df', mode='w')

# to import data use:
#FallAllD = pd.read_pickle('FallAllD.pkl')
#FallAllD = pd.read_hdf('FallAllD.h5', 'df')