#!/usr/bin/python3
#  example usage of PiIO 232 H PCB
#  ===============================
# 
# Example program to read in an RS232 gyro string and then
# parse it and send data back to somewhere else over Ethernet
# This is a common Protocol conversion task in industry.
# Gyro type is CDL INSENSE with TOGS string but this will work for most
# serial devices if you just modify the string formating
#
from gpiozero import Button
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs
from time import sleep
from PiIO import PiIO_232_H_Mapper
from PiIO import PiIO_col
import serial

# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

# @@@@ Open udp port @@@@
#
import socket

UDP_IP = "192.168.1.13" # Target address
UDP_PORT = 49152		# Target port
HEADER = "$PiIO_232"		# MSG header

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP

# @@@@ Hardware init @@@@
#
io = PiIO_232_H_Mapper()
o1 = LED(io.O1); 
o2 = LED(io.O2); 
o3 = LED(io.O3); 
o4 = LED(io.O4); 
o5 = LED(io.O5); 
#o6 = LED(O6) 
o6 = PWMLED(io.O6,True,0,1000);
o7 = LED(io.O7); 
o8 = LED(io.O8); 
ser = serial.Serial('/dev/ttyAMA0',19200,timeout=1)

i1 = Button(io.I1,pull_up=False); 
i2 = Button(io.I2,pull_up=False); 
i3 = Button(io.I3,pull_up=False); 
i4 = Button(io.I4,pull_up=False); 
i5 = Button(io.I5,pull_up=False); 
i6 = Button(io.I6,pull_up=False); 
i7 = Button(io.I7,pull_up=False); 
i8 = Button(io.I8,pull_up=False); 

col=PiIO_col()
run = LED(io.RUN);
#
# @@@@ END HW INIT @@@@
#
print (col.HOME,col.CLR,col.GREENB,col.BLACK," PiIO Example program - 232_H_ProtocolConv \n",col.ENDC,sep='')
print ("1. Program to parse a 232 string and send it back over ethernet")
print ("2. This example uses 19200,8,N,1 Marine TOGS gyro string")
print ("3. IO isn't used here but could be used to power gyro or do PWM ctrl")
print ("4. Take note of port and IP address target here")
print ()
print ("   UDP target IP:", UDP_IP)
print ("   UDP target port:", UDP_PORT)
print ()
#
print("press [ret] to perform test.")
input()
#
while True:
	# get serial string
	read = ser.readline().decode('ascii','ignore')

	# Parse string of the form, to get the sub items we are interested in 
	# 'AH187.45 AP-0.09 AR+0.09 M9 E4930 S2 CE3B
	sub = read.split(' ')
	print(sub)
	# ['AH187.45', 'AP-0.09', 'AR+0.09', 'M9', 'E4930', 'S2', 'CE3B4']

	HDG = sub[0][2:]
	print(HDG);
	# 187.45

	PITCH = sub[1][2:]
	print(PITCH);
	# -0.09

	ROLL = sub[2][2:]
	print(ROLL);
	# 0.09

	# create UDP message
	MESSAGE = HEADER + ',' + HDG + ',' + PITCH + ',' + ROLL  + '\n' + '\r'
	# $PiIO_232,257.70,+0.03,+0.23

	# Send it over UDP
	sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

	sleep(0.1)
	# Toggle LED
	run.toggle()



