#!/usr/bin/python3

#  example usage of Analog PCB for basic hydraulic control =======================================================
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
import sys
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from gpiozero import Button
from time import sleep
from PiIO import PiIO_DO24_Mapper
from PiIO import PiIO_Analog
from PiIO import PiIO_col
from PiIO import PiIO_getc
from PiIO import PiIO_timer
from PiIO import PiIO_EMA
from pyowm import OWM
import paho.mqtt.client as mqtt #import the client1


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

# globals / topics
hours_no_water = 0
irrigation_cnt = 0
irrigation_timer = PiIO_timer()
irrigation_auto = False
irrigation_manual = False

fountain_cnt = 0
fountain_mins = 0

beer_setp = 15
beer_temp = 0
beer_enable = False
beer_heating = False
beer_timer = PiIO_timer()

run_timer = PiIO_timer()

NoFault=True

# sleep abstractions
#
def sleepMin(time):
	sleep(time * 60)


# @@@@ WEATHER and IRRIGATION TASK @@@@
#
def timed_task1():
	global hours_no_water, irrigation_cnt, irrigation_timer, NoFault, irrigation_manual
	# use pyowm to get weather where I am
	API_key = 'a3f08180a153e131e0e13d9d30a7c315'
	owm = OWM(API_key)
	# sett locale to my garden
	obs = owm.weather_at_coords(54.92,-1.74)      
	while NoFault:	
		if irrigation_auto :
			# check weather forecast, see if there's any rain
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
			# run irrigation if required
			if(hours_no_water >= 60):
				print('T1> Turn on irrigation');
				#turn on solenoid
				O2.on();
				irrigation_timer.reset()
				irrigation_cnt+=1
				sleepMin(3)
				#solenoid off
				O2.off();
				hours_no_water = 0
			# wait an hour
			sleepMin(60) 




# @@@@@ BREWING @@@@@
#
def timed_task2():
	global beer_temp, beer_setp, beer_enable, beer_heating, NoFault
	#
	deadband = .5;
	avg = PiIO_EMA(0.5)
	while NoFault:
		sleepMin(.5)
		# brewing is enabled via the UI
		if beer_enable == True:
			beer_temp = avg.ema( adc.get_temp() )
			if beer_temp < (beer_setp - deadband):
				beer_heating = True
			if beer_temp > (beer_setp + deadband):
				beer_heating = False
		else:
			beer_heating = False
			beer_temp = 0
		O1.value = beer_heating
		# plot data
		temp = '{0:.2f}'.format(beer_temp)
		client.publish("hydro/beer_temp",str(temp)) # format 2dp
		client.publish("hydro/beer_heating",str(beer_heating))


# @@@@ Debugger  terminal @@@@
#
def timed_task3():
	global hours_no_water, fountain_cnt, irrigation_cnt, run_timer, irrigation_timer
	global beer_setp, beer_temp, beer_heating, beer_enable, beer_timer, NoFault
	# example console UI debugger

	sleep(4)
	while NoFault:
		sleep(1)
		if beer_enable:
			beer_time = beer_timer.read()
		else:
			beer_time = 'disabled'

		if irrigation_cnt > 0:
			irrigation_time = irrigation_timer.read()
		else:
			irrigation_time = 'none'

		print( PiIO_col.RESET,end='',sep='')
		#          			 "_123456789_123456789_123456789_123456789_123456789_123456789_123456789_123456789
		print( PiIO_col.REDB,'                       << hydro_ADIO Terminal debugger >>                      ',PiIO_col.ENDC,sep='')
		print( 'Run time:\t',run_timer.read(),'(s)')
		print( PiIO_col.REDB,'                                                                               ',PiIO_col.ENDC,sep='')
		print()
		print( 'Hours no water:\t',hours_no_water)
		print( 'Irrigatios:\t',irrigation_cnt)
		print( 'Irrigation on:\t',O2.is_lit)
		print()
		print( 'brew time:\t',beer_time)
		print( 'beer temp setp:\t',beer_setp,'DegC')
		print( 'beer temp:\t {0:.2f}'.format(beer_temp),'DegC')
		print( 'heating on:\t',beer_heating)
		print()
		print( PiIO_col.REDB,'                                                                               ',PiIO_col.ENDC,sep='')

		# publish mqt data back to node red UI
		client.publish("hydro/beer_time",beer_time)

		client.publish("hydro/irrigation_cnt",irrigation_cnt)
		client.publish("hydro/hours_no_water",hours_no_water)
		client.publish("hydro/last_irrigation",irrigation_time)


# @@@@ KEYBOARD INPUT @@@@
#
def timed_task4():
	# instead of node-red you are free to use a console UI 
	global beer_setp, irrigation_cnt, fountain_cnt 

	while NoFault:
		sleep(.1)
		c = PiIO_getc()
		if c == '+':
			beer_setp += .5
		if c == '-':
			beer_setp -= .5
		if c == 'r':
			irrigation_cnt = 0
			fountain_cnt = 0


# @@@@@ mqt message handler @@@@@
#
def on_mqt_message(client, userdata, message):
	global beer_setp, beer_enable, beer_timer, irrigation_manual, irrigation_auto

	if 'beer_enable' in message.topic:	
		beer_enable = (message.payload.decode('utf-8').lower() == 'true')
		if beer_enable :
			beer_timer.reset()

	if 'irrigation_auto' in message.topic:	
		irrigation_auto = (message.payload.decode('utf-8').lower() == 'true')

	if 'irrigation_manual' in message.topic:	
		irrigation_manual = (message.payload.decode('utf-8').lower() == 'true')
		# not enables
		if irrigation_manual:
			O2.on()
		else:
			O2.off()

	if 'beer_setp' in message.topic:
		beer_setp = float( message.payload.decode('utf-8') )

# @@@@@ Example code here @@@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#
RUN.blink(.1,.9)
OE.on()
#
broker_address="127.0.0.1" 
client = mqtt.Client("pimoz") #create new instance
client.on_message=on_mqt_message #attach function to callback
client.connect(broker_address) #connect to broker
client.loop_start()
client.subscribe("hydro/#")


# Submit parallel tasks to executor
#
executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

futures = []
futures.append( executor.submit(timed_task1) )
futures.append( executor.submit(timed_task2) )
futures.append( executor.submit(timed_task3) )
futures.append( executor.submit(timed_task4) )


# Handle shutdown of threads so CTRL+C works
try:
#	concurrent.futures.wait(futures, timeout=None, return_when=concurrent.futures.FIRST_EXCEPTION)
	for future in concurrent.futures.as_completed(futures):
		try:
			data = future.result()
		except Exception as exc:
			print('%s generated an exception: %s' % (future, exc))
			NoFault = False

except KeyboardInterrupt:
	print('ctrl+C')
	executor.shutdown(wait=False)
	executor._threads.clear()
	concurrent.futures.thread._threads_queues.clear()











# @@@@ WATER FOUNTAIN CTRL @@@@
#
"""
def timed_task3():
	global fountain_cnt, fountain_mins

	relay_on = False
	tof = PiIO_TOF(0,fountain_mins * 60) # 30 min
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
					fountain_mins += 30
				else:
					fountain_mins = 30
				# change timer off setpoint
				tof.set_time = fountain_mins * 60
				fountain_cnt+=1
		else: # wait for btn rel
			tof(1) # arm off timer
			if IN1.is_pressed() == 0:
				State = 0; #  btn release			
				DO4.off() # LED
				sleep(.05) # debounce
		# drive solenoid on timed off
		relay_on = tof(0)
		if(relay_on.tof()):
			DO3.on()
		else:
			DO3.off()
"""









































