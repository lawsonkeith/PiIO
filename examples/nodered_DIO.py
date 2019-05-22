#!/usr/bin/python3
#  example usage of DIO PCB with node red UI
#  =========================================
#
#  K Lawson April 2019
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
# Publishes 	mem/count (Str)
# Subscribes	sensor/sensor1
#
from gpiozero import Button
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from time import sleep
from PiIO import PiIO_DO24_Mapper
from PiIO import PiIO_DIO12_Mapper
import paho.mqtt.client as mqtt #import the client1


# subscribe to all sensor topics
#
def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))


count=0
broker_address="127.0.0.1" 
client = mqtt.Client("pimoz") #create new instance
client.on_message=on_message_print #attach function to callback
client.connect(broker_address) #connect to broker
client.loop_start()
client.subscribe("sensor/#")




# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

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
run = LED(io.RUN);
#
# @@@@ END HW INIT @@@@

# Enable outputs
#
enable.on()

#
print ("Program to echo when input pins are pulled high")
print ("use 3V3 to 24V")
print ()
while True:
	count+=1
	client.publish("mem/count",str(count))
	if  i1.value == 1:
		print("i1 pressed")
	if i2.value == 1:
		print("i2 pressed")
	if i3.value == 1:
		print("i3 pressed")
	if i4.value == 1:
		print("i4 pressed")
	if i5.value == 1:
		print("i5 pressed")
	if i6.value == 1:
		print("i6 pressed")
	if i7.value == 1:
		print("i7 pressed")
	if i8.value == 1:
		print("i8 pressed")
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



