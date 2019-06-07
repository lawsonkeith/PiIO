#!/usr/bin/python3
#  example usage of Analog PCB for basic hydraulic control
#  =======================================================
#
#  K Lawson June 2019
# 
#  This example provides 3 levels of functionality
#  -----------------------------------------------
#	1. Brewing controller, uses PT100 to control the temperature of my tasty homebrew.
# 		so when the probe senses the beer is too cold a relay on DO1 turns the heater on, the temperature then goes above another
#		setpoint it turns off again.  A node red user interface allows us to track temperature variations.
#	2. Irrigation controller - when we detect we have had warm weather for 3 days in a row we turn on the irrigation solenoid for 5 minutes at midnight
#	3. Water fountain controller - A button on the unit allows the outside fountain to be turned on for 30 minutes per press.  It can be turned off
#		using the node red user interface.
#
#	IO Map
#	------
#	DI1		Fountain enable button
#	DO1		Brewing belt relay
#	DO2		Irigation solenoid
#	DO3		Water fountain relay
#	DO4		Fountain enable button LED feedback
#	T1		Beer PT100
#	WLAN0	Wifi interface for Node red UI, use exxternal dongle
#
#  Additional packages
#  ------------------
#  1. Node red, and Node red UI for user interface
#  2. pip3 install pyowm
#		a. https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html#using-a-paid-pro-api-key-subscription
#		b. w3ather99
#

import concurrent.futures 
from termcolor import colored
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from gpiozero import Button
from time import sleep
from PiIO import PiIO_DO24_Mapper
from PiIO import PiIO_Analog
from PiIO import PiIO_Watch
from PiIO import PiIO_col
from pyowm import OWM

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
adc = PiIO_Analog(GAIN)
RUN = LED(adc.RUN)
PWM1 = PWMLED(adc.PWM1)
PWM2 = PWMLED(adc.PWM2)
IN1 = Button(adc.I1,pull_up=False)
IN2 = Button(adc.I2,pull_up=False)
IN3 = Button(adc.I3,pull_up=False)
IN4 = Button(adc.I4,pull_up=False)
O1 = LED(adc.O1)
O2 = LED(adc.O2)
O3 = LED(adc.O3)
O4 = LED(adc.O4)
O5 = LED(adc.O5)
O6 = LED(adc.O6)
O7 = LED(adc.O7)
O8 = LED(adc.O8)
OE = LED(adc.OE)

hours_no_water = 0

# sleep abstractions
#
def sleepMin(time):
	sleep(time * 60)

# @@@@ WEATHER TASK @@@@
#

def timed_task1():
	print( PiIO_col.REDB,"T1> Starting",PiIO_col.ENDC)
	# use pyowm to get weather where I am
	API_key = 'a3f08180a153e131e0e13d9d30a7c315'
	owm = OWM(API_key)
	# sett locale to my garden
	obs = owm.weather_at_coords(54.92,-1.74)      
	while True:	
		print("T1> Checking weather")
		w = obs.get_weather()
		rain_str = w.get_detailed_status()
		print('T1>',rain_str)
		if 'rain' in rain_str:
			print('T1> reset counter')
			hours_no_water = 0
		else:
			print('T1> increment counter')
			hours_no_water += 1
		# wait an hour
		sleepMin(60)

# @@@@ IRRIGATION SOLENOID CTRL @@@@
#
def timed_task2():
	print( PiIO_col.REDB,"T2> Starting",PiIO_col.ENDC)
	sleepMin(1)
	if(hours_no_water > 36):
		print('T2> Turn on irrigation');
		#turn on solenoid
		O2.on();
		sleepMin(3)
		#solenoid off
		O2.off();
		hours_no_water = 0
	

# @@@@ WATER FOUNTAIN CTRL @@@@
#
def timed_task3():
	print( PiIO_col.REDB,"T3> Starting",PiIO_col.ENDC)
	on_time = 0 # seconds
	relay_on = False
	tof = PiIO_TOF(0,1800) # 30 min
	while True:
		state = 0
		# @@@@ Button state machine @@@@
		#
		# every button press gives 30 mins of the fountain
		if state == 0: # wait for btn
			if IN1.is_pressed():
				print('T3> Fountain on')
				State = 1
				DO4.on() # LED
				if relay_on:
					on_time += 1800
				else:
					on_time = 1800
				tof.set_time = on_time
		else: # wait for btn rel
			tof(1) # arm off timer
			if IN1.is_pressed() == 0:
				State = 0; #  btn release			
				DO4.off() # LED
				sleep(.05) # debounce
	
		relay_on = tof(0)
		if(relay_on):
			DO3.on()
		else:
			DO3.off()
			
		if(	IN1.is_pressed()):
			O4.on() # LED
			tof(1)
		else:
			O4.off()

		if IN1.is_pressed():			
			if(tof(0) == 0):
				tof(1)



		
		

# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#
RUN.blink(.100,.900)
OE.on()
sleepMin(1)
watch = PiIO_Watch()

# Submit parallel tasks to executor
#
executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

executor.submit(timed_task1)
executor.submit(timed_task2)
executor.submit(timed_task3)

# Handle shutdown of threads so CTRL+C works
try:
	executor.shutdown(wait=True)
except KeyboardInterrupt:
	executor._threads.clear()
	concurrent.futures.thread._threads_queues.clear()

print( PiIO_col.REDB,"T> done.",PiIO_col.ENDC)
