#!/usr/bin/python3
#  example usage of PHiSideDriver PCB
#  ==================================
#
#  K Lawson April 2019
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
from gpiozero import Button
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from time import sleep
from PiIO import PiIO_DIO12_Mapper
from PiIO import PiIO_col
import sys

# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

col = PiIO_col;

# @@@@ Hardware init @@@@
#
io = PiIO_DIO12_Mapper()
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

i1 = Button(io.I1,pull_up=False);
i2 = Button(io.I2,pull_up=False);
i3 = Button(io.I3,pull_up=False);
i4 = Button(io.I4,pull_up=False);
i5 = Button(io.I5,pull_up=False);
i6 = Button(io.I6,pull_up=False);
i7 = Button(io.I7,pull_up=False);
i8 = Button(io.I8,pull_up=False);
i9 = Button(io.I9,pull_up=False);
i10 = Button(io.I10,pull_up=False);
i11 = Button(io.I11,pull_up=False);
i12 = Button(io.I12,pull_up=False);

enable = LED(io.OE);
#run = LED(io.RUN); soldering the onboard link causes run LED to be re-purposed as a fault indicator OUTPUT->INPUT
fault = Button(io.RUN,pull_up=False);
#
# @@@@ END HW INIT @@@@

# Enable outputs
#
enable.on()

#
print (col.HOME,col.CLR,col.GREENB,col.BLACK," PiIO Example program - fault_DIO \n",col.ENDC,sep='')
print ("1. Program to test readback of fault")
print ("2. This is as per the basic functionality program, set an input high to enable corresponding output")
print ("3. But if that output goes into FAULT the software can detect it so long as the solder link LK1 is made on the board")
print ("4. Make sure NOT to set the solder link and set the RUN pin to output as this could damage the PI when a fault occurs")
print ("5. To test, set input 1 high then short output 1 to ground, the software should detect, then clear the fault state")
print ("6. Also note that the RUN and FAULT LED will be set permanently high now.")
print ()
while True:
	try:
		if  i1.value == 1:
			print("i1 pressed")
			o1.on()
		if i2.value == 1:
			print("i2 pressed")
			o2.on()
		if i3.value == 1:
			print("i3 pressed")
			o3.on()
		if i4.value == 1:
			print("i4 pressed")
			o4.on()
		if i5.value == 1:
			print("i5 pressed")
			o5.on()
		if i6.value == 1:
			print("i6 pressed")
			o6.value = 0.5
		if i7.value == 1:
			print("i7 pressed")
			o7.on()
		if i8.value == 1:
			print("i8 pressed")
			o8.on()
		if i9.value == 1:
			print("i9 pressed")
			o9.on()
		if i10.value == 1:
			print("i10 pressed")
			o10.on()
		if i11.value == 1:
			print("i11 pressed")
			o11.on()
		if i12.value == 1:
			print("i12 pressed")
			o12.on()

		if fault.value == 0:
			print("SHORT CCT FAULT DETECTED!")
			print("RESET FAULT...")
			enable.off()
			sleep(5)
			enable.on()
			print("RESET COMPLETE")

		sleep(1)

	except KeyboardInterrupt:
		# required to close down program correctly in case of ctrl+c exit
		print("bye")
		i1.close()
		i2.close()
		i3.close()
		i4.close()
		i5.close()
		i6.close()
		i7.close()
		i8.close()
		i9.close()
		i10.close()
		i11.close()
		i12.close()
		sys.exit()




