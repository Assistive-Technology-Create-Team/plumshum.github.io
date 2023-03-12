% FallAllD files to MATLAB struct
% By Majd SALEH 08-April-2020.
ParentDir=pwd;
FP=[ParentDir '\FallAllD\'];

oldDir = cd (FP);

Files=dir('*_A.dat');
LL=size(Files,1);
FileIDs=[];
cd(oldDir);

for i=1:LL
   FileName=Files(i).name;
   CurReg=[str2double(FileName(2:3)),str2double(FileName(6)),str2double(FileName(9:11)),...
       str2double(FileName(14:15))];
    FileIDs=[FileIDs;CurReg];
    FallAllD(i).SubjectID=cast(str2double(FileName(2:3)),'uint8');
    FallAllD(i).AtivityID=cast(str2double(FileName(9:11)),'uint8');
    FallAllD(i).TrialNo=cast(str2double(FileName(14:15)),'uint8');
    if str2double(FileName(6))==1
        Device='Neck';
    elseif str2double(FileName(6))==2
        Device='Wrist';
    else
        Device='Waist';
    end
    FallAllD(i).Device=Device;
    Acc=load([FP FileName]);
    FallAllD(i).Acc=Acc;
    FileName(17)='G';
    Gyr=load([FP FileName]);
    FallAllD(i).Gyr=Gyr;
    FileName(17)='M';
    Mag=load([FP FileName]);
    FallAllD(i).Mag=Mag;
    FileName(17)='B';
    Bar=load([FP FileName]);
    FallAllD(i).Bar=Bar;
    disp(['File ' num2str(i*4) ' out of ' num2str(LL*4)]);
end
disp('Saving FallAllD in MATLAB struct ...');
save('FallAllD','FallAllD');
disp('Done!');
% to load the structure, use load('FallAllD.mat')
% use Plot_FallAllD_Register to get familiar with the dataset