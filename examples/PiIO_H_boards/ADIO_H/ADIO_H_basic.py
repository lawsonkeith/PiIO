#!/usr/bin/python3
#  example usage of PiIO ADIO H PCB
#  ================================
#
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
#  This example does an IO check on the board
#
#  NOTE - enable I2C in raspiconfig, disbale UART, SPI
#  NOTE2 - if you experience problems accesing i2C check node red is not also trying to access it (if using node red)
#
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from gpiozero import Button
from time import sleep
from PiIO import PiIO_Analog_H_Mapper
from PiIO import PiIO_col

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 2

# @@@@ Hardware init @@@@
#
try:
	adc = PiIO_Analog_H_Mapper(GAIN)
except :
	print("IO Exception - check I2C enabled in raspi-config, disable Serial & SPI")	
	quit()
run = LED(adc.RUN)
col = PiIO_col()
i1 = Button(adc.I1,pull_up=False)
i2 = Button(adc.I2,pull_up=False)
i3 = Button(adc.I3,pull_up=False)
i4 = Button(adc.I4,pull_up=False)
i5 = Button(adc.I5,pull_up=False)
i6 = Button(adc.I6,pull_up=False)
i7 = Button(adc.I7,pull_up=False)
i8 = Button(adc.I8,pull_up=False)
i9 = Button(adc.I9,pull_up=False)
i10 = Button(adc.I10,pull_up=False)
i11 = Button(adc.I11,pull_up=False)
i12 = Button(adc.I12,pull_up=False)

o1 = LED(adc.O1)
o2 = LED(adc.O2)
o3 = LED(adc.O3)
o4 = LED(adc.O4)
o5 = LED(adc.O5)
o6 = LED(adc.O6)
o7 = LED(adc.O7)
o8 = LED(adc.O8)

# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#
print (col.HOME,col.CLR,col.GREENB,col.BLACK," PiIO Example program - ADIO_H_basic \n",col.ENDC,sep='')
print ("0. Required raspi-config I2C:enabled SPI/UART:disabled")
print ("1. Program to cycle through and test all IO")
print ("2. Analog inputs, read 1-4 0-10V")
print ("3. Read in DI states then set DO states")
print ()
run.blink(.100,.900)
print("Press return at each test to continue.")
sleep(2)
print("> reading ADC 1..4")
input()
data = .4
for x in range(4):
	for y in range(20):
		data = adc.get_scaled(x) 	
		print (" ",x," scaled ","{:.2f}".format(data),sep='\t',end='')
		data = adc.get_raw(x) 	
		print ("         raw    ",data,sep='\t')
		sleep(.4)



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
	if i10.value == 1:
		print("i10 pressed")
	if i11.value == 1:
		print("i11 pressed")
	if i12.value == 1:
		print("i12 pressed")

	sleep(1)
	run.toggle()



