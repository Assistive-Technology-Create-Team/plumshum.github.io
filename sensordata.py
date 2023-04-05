from sense_hat import SenseHat
label_name = input ("Enter an action label: ")
file_counter = 0
samples = 0
#each action will collect invidiaul data
#press joystick to switch action

sense = SenseHat()
import time
collecting = False
pressed = False

Fs_Acc = 238  # Sampling frequency of accelerometer 238 Hz
Fs_Gyr = 238  # Sampling frequency of gyroscope 238 Hz
Fs_Mag = 80   # Sampling frequency of magnetometer 80 Hz
Fs_Bar = 10   # Sampling frequency of barometer 10 Hz

Acc_Sen = 0.000244  # Accelerometer sensitivity 0.244 mg/LSB
Gyr_Sen = 0.07      # Angular rate sensitivity 70 mdps/LSB
Mag_Sen = 0.00014   # Magnetic sensitivity 0.14 mgauss/LSB


while True:
    acceleration = sense.get_accelerometer_raw()
    gyro = sense.get_gyroscope_raw()
    pressure = sense.get_pressure()
    pressed = False
    for event in sense.stick.get_events():
        if event.action == "pressed":
            pressed = True
            print("The joystick was pressed")
    
    if pressed == True:
        if collecting == False:
            samples = 0
            collecting = True
        else:
            collecting = False
            print("Not collecting data")
    pressed = False
    if collecting == True:
        print("Collecting data")
        samples +=1
        #split acleration into x, y, z
        Acc_x = acceleration['x']
        Acc_y = acceleration['y']
        Acc_z = acceleration['z']
        b = pressure #can't use right now
        Gyr_x = gyro['x']
        Gyr_y = gyro['y']
        Gyr_z = gyro['z']
        

        Acc_x = Acc_x / Acc_Sen  # convert to g units (m/s^2 units/9.81)
        Acc_y = Acc_y / Acc_Sen  # convert to g units (m/s^2 units/9.81)
        Acc_z = Acc_z / Acc_Sen  # convert to g units (m/s^2 units/9.81)
        Gyr_x = Gyr_x / Gyr_Sen  # convert to dps units
        Gyr_y = Gyr_y / Gyr_Sen  # convert to dps units
        Gyr_z = Gyr_z / Gyr_Sen  # convert to dps units



            # Time vector
    # A time vector is created for each signal based on the number of samples and the corresponding sampling frequency. 
    # The time vectors can be used to plot the signals over time or to synchronize signals with each other

        print("x={0}, y={1}, z={2}, g={3}, h={4}, i={5}".format(Acc_x, Acc_y, Acc_z, Gyr_x, Gyr_y, Gyr_z))
        
        # write x, y, z, b, g, h to a file
        file_name = "fall"
        with open(file_name + ".csv") as f:
            # write x, y, z, g, h, i to the file. cant add barometer data right now
            f.write("{0},{1},{2},{3},{4},{5}".format(Acc_x, Acc_y, Acc_z, Gyr_x, Gyr_y, Gyr_z))
            # write a new line
            f.write("\n")
        if samples == 20:
            file_counter +=1
            samples = 0

        time.sleep(0.1) #time interval 0.1 seconds 
        
        