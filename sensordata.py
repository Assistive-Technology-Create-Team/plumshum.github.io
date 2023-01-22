from sense_hat import SenseHat
filename = input ("Enter a filename: ")

sense = SenseHat()
import time
collecting = False
pressed = False
samples = 0
while True:
    acceleration = sense.get_accelerometer_raw()
    pressed = False
    for event in sense.stick.get_events():
        if event.action == "pressed":
            pressed = True
            print("The joystick was pressed")
    
    if pressed == True:
        if collecting == False:
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

        x=round(x*1000, 0)
        y=round(y*1000, 0)
        z=round(z*1000, 0)

        print("x={0}, y={1}, z={2}".format(x, y, z))
        # write x, y, z to a file
        with open(filename + ".txt", "a") as f:
            f.write("{0},{1},{2}".format(x, y, z))
            # write a new line
            f.write("\n")
        if samples == 20:
            quit()
        time.sleep(0.1) #time interval 0.1 seconds 
        
        