#!/usr/bin/python3
#  example usage of PiIO 232 H PCB
#  ===============================
# 
# Example program to read in an RS232 gyro string and then
# Gyro type is a TOGS subsea gyro
# parse it and send data back to somewhere else over Ethernet
# This is a common Protocol conversion task in industry.
# This example features some additional string validation
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
print ("5. Some basic string validation is done here, but we do not check the CRC")
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

	# Parse string of the form 
	# 'AH187.45 AP-0.09 AR+0.09 M9 E4930 S2 CE3B
	sub = read.split(' ')
	print(sub)

	ERROR = False;
	if len(sub) != 7:
		ERROR = True
    
	HDG = sub[0][2:]
	try:
		float(HDG)
	except ValueError:
		ERROR = True
	print(HDG);

	PITCH = sub[1][2:]
	try:
		float(PITCH)
	except ValueError:
		ERROR = True
	print(PITCH);

	ROLL = sub[2][2:]
	try:
		float(ROLL)
	except ValueError:
		ERROR = True
	print(ROLL);

	# if data error, put it in the message
	if ERROR == True:
		ERR = "ERR"
	else:
		ERR = "OK"


	# create UDP message
	MESSAGE = HEADER + ',' + HDG + ',' + PITCH + ',' + ROLL  + ',' + ERR + '\n' + '\r'

	# Send it
	sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

	sleep(0.1)
	run.toggle()



