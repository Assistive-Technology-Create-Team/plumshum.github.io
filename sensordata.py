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

while True:
    acceleration = sense.get_accelerometer_raw()
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
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        b = pressure

        x=round(x*1000, 0)
        y=round(y*1000, 0)
        z=round(z*1000, 0)
        b=round(b, 3)

        print("x={0}, y={1}, z={2}, b={3}".format(x, y, z, b))
        # write x, y, z to a file
        file_name = "{0}_{1}".format(label_name, file_counter)
        with open(file_name + ".txt", "a") as f:
            f.write("{0},{1},{2},{3}".format(x, y, z,b))
            # write a new line
            f.write("\n")
        if samples == 20:
            file_counter +=1
            samples = 0

        time.sleep(0.1) #time interval 0.1 seconds 
        
        