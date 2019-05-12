#!/usr/bin/python3
#  example usage of PHiSideDriver PCB
#  ==================================
#
#  K Lawson April 2019
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
#  This example turns on the outputs on this 24 output only board
#
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from time import sleep
from PiIO import PiIO_DO24_Mapper
from PiIO import PiIO_Analog

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

# @@@@ Hardware init @@@@
#
#io = PiIO_DO24_Mapper()
#o1 = LED(io.O1); 
#o2 = LED(io.O2); 
#o3 = LED(io.O3); 
#o4 = LED(io.O4); 
#o5 = LED(io.O5); 
#o6 = LED(O6) 
#o6 = PWMLED(io.O6,True,0,1000);
#o7 = LED(io.O7); 
#o8 = LED(io.O8); 
#o9 = LED(io.O9); 
#o10 = LED(io.O10); 
#o11 = LED(io.O11); 
#o12 = LED(io.O12); 
#o13 = LED(io.O13); 
#o14 = LED(io.O14); 
#o15 = LED(io.O15); 
#o16 = LED(io.O16); 

adc = PiIO_Analog(GAIN)

for x in range(4):
	data = adc.get_raw(x)	
	print (data)
	temp = adc.get_temp()
	print (temp)

