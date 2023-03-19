# FallAllD files to Python struct

# Hannah's Comment: takes data and turns in to panda dataframe, and it's saved in a pickle file.
#The pickle file is called FallAllD.pkl
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import os
from numpy import genfromtxt
import numpy as np
import pandas as pd 

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
res = pd.DataFrame(columns=['SubjectID', 'Device','ActivityID','TrialNo','Acc_x','Acc_y', 'Acc_z','Gyr_x','Gyr_y', 'Gyr_z'])
for i in range(LL):
    f_name=FileNames[i]
    SubjectID=int(f_name[1:3])    
    ActivityID=int(f_name[8:11])    
    TrialNo=int(f_name[13:15])    
    Device=int(f_name[5])
    
    df_acc = pd.read_csv(f_name, header=None, sep=',', names=['Acc_x','Acc_y', 'Acc_z'])
    chArr=list(f_name)
    chArr[16]='G'
    f_name="".join(chArr)    
    df_gyr = pd.read_csv(f_name, header=None, sep=',', names=['Gyr_x','Gyr_y', 'Gyr_z'])
    # create a new dataframe called df, df's columns are from the two dataframes df_acc and df_gyr
    df = pd.concat([df_acc, df_gyr], axis=1)
    df['SubjectID'] = SubjectID
    df['Device'] = Device
    df['ActivityID'] = ActivityID
    df['TrialNo'] = TrialNo
    #print(df.head(1))
    
    #Not used
    #chArr[16]='M'
    #f_name="".join(chArr)    
    #l_Mag.append(np.int16(genfromtxt(f_name, delimiter=',')))
    #chArr=list(f_name)
    #chArr[16]='B'
    #f_name="".join(chArr)    
    #l_Bar.append(genfromtxt(f_name, delimiter=','))
    res = res.append(df, ignore_index=True)
    print(f'File  {i+1}  out of {len(FileNames)} shape {res.shape}')
    filename = 'FallAllD' +  '-' + str(SubjectID) +  '-' + str(Device) +  '-' + str (ActivityID) + '-' + str(TrialNo) + '.csv'
    res.to_csv(filename)
    res = pd.DataFrame(columns=['SubjectID', 'Device','ActivityID','TrialNo','Acc_x','Acc_y', 'Acc_z','Gyr_x','Gyr_y', 'Gyr_z'])


# read all csv and combine them into one dataframe
FallAllD = pd.concat([pd.read_csv(f) for f in os.listdir('.') if f.endswith('.csv')], ignore_index = True)
#This create the panda dataframe
os.chdir(oldDir)
FallAllD.to_csv('FallAllD2.csv')

