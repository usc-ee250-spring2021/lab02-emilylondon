""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Emily London
Insert Github repository link here.
https://github.com/usc-ee250-spring2021/lab02-emilylondon
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import * #needed for LCD screen

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""

"""Note: the syntax, structure, and libraries for this code are sourced from 
the GrovePi documentation. """
#Variables
UPORT = 2   # D4, where the Ultrasonic Ranger is connected
APORT = 0	#A0, where the rotary analog sensor is connected
grovepi.set_bus("RPI_1") #sets I2C to use the hardware bus
grovepi.pinMode(APORT,"INPUT")
setRGB(0,255,0)

if __name__ == '__main__':
    
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        #Collect readings for sensor data
        threshold=grovepi.analogRead(APORT)
        distance=grovepi.ultrasonicRead(UPORT)

        #Setting realistic max distance for this exercise to 50 cm
        if distance>517:
        	distance=517

        #Compare threshold to distance
        if threshold >= distance:
        	setText_norefresh(str(threshold)+"cm  OBJ PRES\n" + str(distance)+"cm")
        	setRGB(255,0,0)
        else:
        	setText_norefresh(str(threshold)+"cm               \n"+str(distance)+"cm")
        	setRGB(0,255,0)
