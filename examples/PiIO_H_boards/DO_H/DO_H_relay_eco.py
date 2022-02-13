#!/usr/bin/python3
#  example usage of PiIO DO H PCB
#  ==============================
#
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
from gpiozero import Button
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs
from time import sleep
from PiIO import PiIO_DO_H_Mapper
from PiIO import PiIO_col
	
# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

# @@@@ Hardware init @@@@
#
io = PiIO_DO_H_Mapper()
o1 = PWMLED(io.O1,True,0,500);
o2 = LED(io.O2); 
o3 = LED(io.O3); 
o4 = LED(io.O4); 
o5 = LED(io.O5); 
o6 = LED(io.O6); 
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

col=PiIO_col()
run = LED(io.RUN);
#
# @@@@ END HW INIT @@@@
#
try:
	print (col.HOME,col.CLR,col.GREENB,col.BLACK," PiIO Example program - DO_H_relay_eco \n",col.ENDC,sep='')
	print ("1. Program to turn a relay on and save power")
	print ("2. Turn on then 1s later switch to reduced power")
	print ("3. This will save significant power")
	print ()
	print ("Press any key to coninue.")
	input()
	sleep(1)
	run.blink()


	print ("Bringing contactor in full current ...")
	o1.value = 1
	sleep(5)
	print ("Switch to power saving mode")
	o1.value = 0.25
	sleep(5)
	print("Done!, press any key to exit")

	input()


#except KeyboardInterrupt:
	# code to run before CTRL+C

#except:
	# all other errors

finally:
	o1.close()
	run.close();
	# cleanup gpio so we don't get an error next time




