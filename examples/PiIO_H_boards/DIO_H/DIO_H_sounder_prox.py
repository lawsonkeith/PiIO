#!/usr/bin/python3
#  example usage of PiIO DIO H PCB
#  ===============================
# 
#

import concurrent.futures
from gpiozero import Button
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs
from time import sleep
from PiIO import PiIO_DIO_H_Mapper
from PiIO import PiIO_col
import serial
#
io = PiIO_DIO_H_Mapper()
# power feed to switch
OUT_switch_en = LED(io.O1);
# switch internal LED
OUT_switch_led = PWMLED(io.O2,True,0,100);
# rotary pot led
OUT_rot_led = PWMLED(io.O3,True,0,100);
# sounder
OUT_sounder = LED(io.O4);
# prox power
OUT_prox_en = LED(io.O6);
# pullups on rotoarr pot
OUT_rot_pup = LED(io.O5);

# rotary pot inputs
IN_a = Button(io.I1,pull_up=False);
IN_b = Button(io.I2,pull_up=False);
# switch on rotary pot
IN_rot_sw = Button(io.I3,pull_up=False);
# main switch 
IN_sw = Button(io.I4,pull_up=False);
# prox detector ip
IN_prox = Button(io.I5,pull_up=False);


col=PiIO_col()
run = LED(io.RUN);
#
# @@@@ END HW INIT @@@@
#
print (col.HOME,col.CLR,col.GREENB,col.BLACK," PiIO Example program - basic control \n",col.ENDC,sep='')
print ("0. Required raspi-config I2C:disabled SPI:disbled Serial:disabled")
print ("1. When prox triggers sounder goes off")
print ("2. Btn cancels sounder")
print ("3. Rotary switch controls LED brightness")
print ()
#
print("press [ret] to perform test.")
input()
#
#
OUT_rot_pup.on()
OUT_switch_en.on()
OUT_prox_en.on()
brightness = 0.01
old=0.1
state=0
count=0
#

# run 2 tasks, one general and one to read rotary pot
#
while True:
	count+=1
	# @@@@ slow task @@@@
	if count==20:
		if IN_prox.value == 1:
			print("prox hi, enable sounder")
			OUT_sounder.on()

		if IN_sw.value == 1:
			print("switch disables sounder")
			OUT_sounder.off()

		if brightness < 0.1:
			OUT_switch_led.value = brightness
			OUT_rot_led.value = brightness
		else:
			OUT_switch_led.value = 1
			OUT_rot_led.value = 1
		

		count=0
		run.toggle()
		sleep(.1)

	# @@@@ fast task @@@@
	# crude encoder scanner
	if True:
		if state==0:
			# looking for 1,1
			if ((IN_a.value == 1) and (IN_b.value == 1)):
				state=1
		elif state==1:
			# both 1,1
			if IN_a.value == 0:
				state=2
			if IN_b.value == 0:
				state=3
		elif state==2:
			#dec
			brightness-=0.01
			state = 4
		elif state==3:
			#inc
			brightness+=0.01
			state=4
		else:
			#default
			# looking for 1,1
			if ((IN_a.value == 1) and (IN_b.value == 1)):
				state=0

		if brightness > 0.1:
			brightness = 0.1

		elif brightness < 0.0:
			brightness = 0.0

#		if old != brightness:
#			old=brightness
#			fbright = "{:.2f}".format(brightness)
#			print("brightness ",fbright)

	# 200 Hz
	sleep(0.005)

