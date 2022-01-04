#!/usr/bin/python3
#
#  example usage of DIO H PCB with node red UI
#  ===========================================
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
#  1. This example powers a contactor on DO6, but once pulled in uses PWM to reduce current draw
#  2. Also O1 can be controlled via a node-red slider
#  3. And any digital input is read and it's value passed back to th UI
#  
#  Instructions
#  ------------
#  1. start node red [node-red]
#  2. Navigate to PI_IP:1880 in a browser
#  3. On node red import->flow->clipboard, past the json text file data in there (from DIO_H_nodered.json)
#  4. Flows should appear, double click an mqtt node and set the pimoz server IP address to the PI IP address (purple box).
#		(or edit the json file and update the IP address in there before importing)
#  5. Deploy
#  6. UI will be at PI IP e.g. http://192.168.1.42:1880/ui/
#  7. Run python program ('./DIO_H_nodered.py')
#  8. The 'python->program cycle' indicator should now increment
#  9. 'Input' Section reads digital input status, 'output' section simulates a DC motor controller
#
from gpiozero import Button
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from time import sleep
from PiIO import PiIO_DIO_H_Mapper
from PiIO import PiIO_col
from PiIO import PiIO_timer
from PiIO import PiIO_TON
import paho.mqtt.client as mqtt #import the client1


# @@@@ Hardware init @@@@
#
io = PiIO_DIO_H_Mapper()
o1 = PWMLED(io.O1,True,0,1000)	# PWM
o2 = LED(io.O2)
o3 = LED(io.O3)
o4 = LED(io.O4)
o5 = LED(io.O5)
o6 = PWMLED(io.O6,True,0,1000) # contactor
o7 = LED(io.O7) 
o8 = LED(io.O8)
o9 = LED(io.O9)
o10 = LED(io.O10)
o11 = LED(io.O11)
o12 = LED(io.O12)

i1 = Button(io.I1,pull_up=False)
i2 = Button(io.I2,pull_up=False)
i3 = Button(io.I3,pull_up=False)
i4 = Button(io.I4,pull_up=False)
i5 = Button(io.I5,pull_up=False)
i6 = Button(io.I6,pull_up=False)
i7 = Button(io.I7,pull_up=False)
i8 = Button(io.I8,pull_up=False)
i9 = Button(io.I9,pull_up=False)
i10 = Button(io.I10,pull_up=False)
i11 = Button(io.I11,pull_up=False)
i12 = Button(io.I12,pull_up=False)

col=PiIO_col()
motor_timer = PiIO_TON(0,2) # 2s timer
run_timer = PiIO_timer() # run timer
run = LED(io.RUN);
count=0
servo_setp=0
motor_enable=False
run.blink(.100,.900) # run LED

# mqt message handler
#
def on_mqt_message(client, userdata, message):
	global servo_setp, motor_enable

	if 'motor' in message.topic:	
		motor_enable = (message.payload.decode('utf-8').lower() == 'true')
		if motor_enable :
			run_timer.reset()
			print("on")

	if 'servo' in message.topic:	
		servo_setp = float(message.payload.decode('utf-8'))
		print(servo_setp)

# create client
#
broker_address="127.0.0.1" 
client = mqtt.Client("pimoz") #create new instance
client.on_message=on_mqt_message #attach function to callback
client.connect(broker_address) #connect to broker
client.loop_start()
client.subscribe("mem/#")


#
# @@@@ END HW INIT @@@@

# Enable outputs
#

#
print (col.HOME,col.CLR,col.GREENB,col.BLACK," PiIO Example program - nodered_DIO \n",col.ENDC,sep='')
print ("1. Program to illustrate node red indirect control of board")
print ("2. note - You will have to update the mqtt broker IP in node red")
print ("3. To do that click the pencil next to the broker in the mqtt node")
print ("4. So rather than node red direct controlling GPIO it sends msgs to this pgm")
print ("5. This provides additional functionality but is harder to implement.")
print ("6. But we can now make the control much more intelligent")


print ()
while True:
	count+=1
	# publish topics over mqtt to node red
	client.publish("mem/count",str(count))	
	client.publish("mem/input",str(input))
	if motor_enable :
		client.publish("mem/run_time",run_timer.read())
	else:
		client.publish("mem/run_time","--")
	input=0


	# read inputs and report on UI which button has been pressed
	#
	if  i1.value == 1:
		print("i1 pressed")
		input=1
	if i2.value == 1:
		print("i2 pressed")
		input=2
	if i3.value == 1:
		print("i3 pressed")
		input=3
	if i4.value == 1:
		print("i4 pressed")
		input=4
	if i5.value == 1:
		print("i5 pressed")
		input=5
	if i6.value == 1:
		print("i6 pressed")
		input=6
	if i7.value == 1:
		print("i7 pressed")
		input=7
	if i8.value == 1:
		print("i8 pressed")
		input=8
	if i9.value == 1:
		print("i9 pressed")
		input=9
	if i10.value == 1:
		print("i10 pressed")
		input=10
	if i11.value == 1:
		print("i11 pressed")
		input=11
	if i12.value == 1:
		print("i12 pressed")
		input=12


	# motor on output 6 - implement power saving control of motor
	#
	if motor_enable:
		if motor_timer.ton(1):
			# ok it's pulled in PWM the output to lower current draw
			o6.value = 0.4
			# print("lo pwr")
		else:
			# max op to pull in contactor
			o6.value = 1.0
			# print("hi pwr")
				
	else:
		# leave it off
		o6.value = 0
		motor_timer.ton(0)


	# motor on output 1
	#
	# here we control a motor but we only allow it on it the motor is enabled
	if motor_enable:
		o1.value = servo_setp / 100.0
	else:
		o1.value = 0

	sleep(1)
