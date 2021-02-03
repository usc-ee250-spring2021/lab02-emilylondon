""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Emily London
Insert Github repository link here.
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

grovepi.set_bus("RPI_1") #sets I2C to use the hardware bus
grovepi.pinMode(APORT,"INPUT")

if __name__ == '__main__':
	#Variables
    UPORT = 4   # D4, where the Ultrasonic Ranger is connected
    APORT = 0	#A0, where the rotary analog sensor is connected
    
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
        threshold=threshold_calc(grovepi.analogRead(APORT))
        distance=grovepi.ultrasonicRead(UPORT)
        setText(str(threshold)+"\n"+str(distance))

        	
        #find the value 
        print(grovepi.ultrasonicRead(UPORT))
#Function to calculate the threshold value based on rotation
def threshold_calc(sensorData):
	adcRef= 5	 #Analog to digital conversion reference voltage
    groveVcc= 5  #V high of the grove 
    fullRot= 300 #300 degrees is the full rotation of the rotary angle
	voltage= round( (float)(sensorData) *adcRef/1023,2)
	threshold= round( (voltage*fullRot) /groveVcc, 2)
	return threshold
