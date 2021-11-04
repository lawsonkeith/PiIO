#!/usr/bin/python3
#  example usage of DIO24 PCB PCB
#  ===============================
#
#  K Lawson April 2021
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
from gpiozero import Button
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from time import sleep
from PiIO import PiIO_DO24_Mapper
from PiIO import PiIO_col
	
# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

# @@@@ Hardware init @@@@
#
io = PiIO_DO24_Mapper()
o1 = LED(io.O1); 
o2 = LED(io.O2); 
o3 = LED(io.O3); 
o4 = LED(io.O4); 
o5 = LED(io.O5); 
#o6 = LED(O6) 
o6 = PWMLED(io.O6,True,0,1000);
o7 = LED(io.O7); 
o8 = LED(io.O8); 
o9 = LED(io.O9); 
o10 = LED(io.O10); 
o11 = LED(io.O11);
o12 = LED(io.O12);
o13 = LED(io.O13);
o14 = LED(io.O14);
o15 = LED(io.O15);
o16 = LED(io.O16);
o17 = LED(io.O17);
o18 = LED(io.O18);
o19 = LED(io.O19);
o20 = LED(io.O20);
o21 = LED(io.O21);
o22 = LED(io.O22);
o23 = LED(io.O23);
o24 = LED(io.O24);
enable = LED(io.OE);
col=PiIO_col()
run = LED(io.RUN);
#
# @@@@ END HW INIT @@@@

# Enable outputs
#


#
try:
	print (col.HOME,col.CLR,col.GREENB,col.BLACK," PiIO Example program - basic_DO24 \n",col.ENDC,sep='')
	print ("1. Program to set outputs high")
	print ("2. We will step through 1s at a time")
	print ("3. The output voltage will be Vfield")
	print ("4. Output 6 uses a PWM Output so will be 50% of the other values")
	print ()
	sleep(1)
	run.blink()
	enable.on()

	print ("1..")
	o1.on()
	sleep(2)
	print ("2..")
	o2.on()
	sleep(2)
	print ("3..")
	o3.on()
	sleep(2)
	print ("4..")
	o4.on()
	sleep(2)
	print ("5..")
	o5.on()
	sleep(2)
	print ("6..")
	o6.value = 0.5
	sleep(2)
	print ("7..")
	o7.on()
	sleep(2)
	print ("8..")
	o8.on()
	sleep(2)
	print ("9..")
	o9.on()
	sleep(2)
	print ("10..")
	o10.on()
	sleep(2)
	print ("11..")
	o11.on()
	sleep(2)
	print ("12..")
	o12.on()
	sleep(2)
	print ("13..")
	o13.on()
	sleep(2)
	print ("14..")
	o14.on()
	sleep(2)
	print ("15..")
	o15.on()
	sleep(2)
	print ("16..")
	o16.on()
	sleep(2)
	print ("17..")
	o17.on()
	sleep(2)
	print ("18..")
	o18.on()
	sleep(2)
	print ("19..")
	o19.on()
	sleep(2)
	print ("20..")
	o20.on()
	sleep(2)
	print ("21..")
	o21.on()
	sleep(2)
	print ("22..")
	o22.on()
	sleep(2)
	print ("23..")
	o23.on()
	sleep(2)
	print ("24..")
	o24.on()
	sleep(2)
	print ("done..")
	input()


#except KeyboardInterrupt:
	# code to run before CTRL+C

#except:
	# all other errors

finally:
	o6.close()
	run.close();
	# cleanup gpio so we don't get an error next time




