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
        Acc = acceleration
        b = pressure #can't use right now
        Gyr = gyro

        Acc = Acc * Acc_Sen  # convert to g units (m/s^2 units/9.81)
        Gyr = Gyr * Gyr_Sen  # convert to dps units

            # Time vector
    # A time vector is created for each signal based on the number of samples and the corresponding sampling frequency. 
    # The time vectors can be used to plot the signals over time or to synchronize signals with each other
        t_Acc = (range(Acc.shape[0]) / Fs_Acc)
        t_Gyr = (range(Gyr.shape[0]) / Fs_Gyr)
        print("Shape", t_Acc, t_Gyr)

        #spllit t_Acc into x, y, z 
        x = Acc[:,0]
        y = Acc[:,1]
        z = Acc[:,2]

        #split t_Gyr into b, g, h
        b = Gyr[:,0]
        g = Gyr[:,1]
        h = Gyr[:,2]

        #These conversions not needed
        #x=round(x*1000, 0)
        #y=round(y*1000, 0)
        #z=round(z*1000, 0)
        #b=round(b, 3)
        #g=round(g, 3)
        #h=round(h, 3)
        #i=round(i, 3)

        print("x={0}, y={1}, z={2}, b={3}, g={4}, h={5}, i={6}".format(x, y, z, b, g, h))
        
        # write x, y, z, b, g, h to a file
        file_name = "{0}_{1}".format(label_name, file_counter)
        with open(file_name + ".txt", "a") as f:
            # write x, y, z, g, h, i to the file. cant add barometer data right now
            f.write("{0},{1},{2},{3},{4},{5},{6}".format(x, y, z, b, g, h))
            # write a new line
            f.write("\n")
        if samples == 20:
            file_counter +=1
            samples = 0

        time.sleep(0.1) #time interval 0.1 seconds 
        
        