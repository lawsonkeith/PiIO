#!/usr/bin/python3
#  example usage of PiIO DIO H PCB
#  ===============================
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
from gpiozero import Button
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs
from time import sleep
from PiIO import PiIO_DIO_H_Mapper
from PiIO import PiIO_col
import serial
	
# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

# @@@@ Hardware init @@@@
#
io = PiIO_DIO_H_Mapper()
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

col=PiIO_col()
run = LED(io.RUN);
#
# @@@@ END HW INIT @@@@
#
print (col.HOME,col.CLR,col.GREENB,col.BLACK," PiIO Example program - basic_DIO_H \n",col.ENDC,sep='')
print ("0. setup I2C off, SPI off, Serial off in raspi-config")
print ("1. Program to echo when input pins are pulled high")
print ("2. We will also set corresponding output high when this happens")
print ("3. The output voltage will be Vfield")
print ("4. Output 6 uses a PWM Output so will be 50% of the other values")
print ()
#
print("press [ret] to perform test.")
input()
#
#
while True:
	if i1.value == 1:
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

	sleep(1)
	run.toggle()



