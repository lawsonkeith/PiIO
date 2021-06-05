#!/usr/bin/python3
#  example usage of PiIO DO H PCB
#  ==================================
#
#  K Lawson 
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
import concurrent.futures 
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs
from time import sleep
from PiIO import PiIO_DO_H_Mapper

# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

# @@@@ Hardware init @@@@
#
io = PiIO_DO_H_Mapper()
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
o13 = LED(io.O13); 
o14 = LED(io.O14); 
o15 = LED(io.O15); 
o16 = LED(io.O16); 
o17 = LED(io.O17); 
o18 = LED(io.O18); 
o19 = LED(io.O19); 
o20 = LED(io.O20); 
o21 = LED(io.O21); 
o22 = LED(io.O22); 
o23 = LED(io.O23); 
o24 = LED(io.O24); 

run = LED(io.RUN);
#
# @@@@ END HW INIT @@@@
	


# Main test loop
#
def timed_task1():

	# rate toggle output 6
	#
	o6.value = 0;
	print("pause at off")
	sleep(5)
	for b in range(100):
		# flash LED
		sleep(.1)
		
		# PWM to output
		o6.value  = b / 100.0
		print(b, "% duty")
	print("pause at full...")
	sleep(5)

	#  turn on all outputs in 5s steps...
	#
	print("turning all outputs on...")
	o1.on()
	sleep(5)
	o2.on()
	sleep(5)
	o3.on()
	sleep(5)
	o4.on()
	sleep(5)
	o5.on()
	sleep(5)
	#o6 = LED(O6) 
	o7.on()
	sleep(5)
	o8.on()
	sleep(5)
	o9.on()
	sleep(5)
	o10.on()
	sleep(5)
	o11.on()
	sleep(5)
	o12.on()
	print("12 on...")
	sleep(5)
	o13.on()
	sleep(5)
	o14.on() 
	sleep(5)
	o15.on()
	sleep(5)
	o16.on()
	sleep(5)
	o17.on()
	sleep(5)
	o18.on()
	sleep(5)
	o19.on()
	sleep(5)
	o20.on()
	sleep(5)
	o21.on()
	sleep(5)
	o22.on()
	sleep(5)
	o23.on()
	sleep(5)
	o24.on()
	sleep(5)
	print("Done")
	sleep(5)

	# Disable outputs
	#
	print("turning outputs off")
	enable.off()
	sleep(10)
	print("exit...")
	
	
# Concurrent status loop
#
def timed_task2():
	# ok so gpio zero can do this for us ... but you get the point
	while True:
		run.toggle()
		sleep(.1)
	
# Submit parallel tasks to executor
#
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
a = executor.submit(timed_task1)	
b = executor.submit(timed_task2)
# wait for 1at task to complete
while a.done() is False:
        pass

