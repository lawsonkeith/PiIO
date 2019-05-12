#  example usage of PHiSideDriver PCB
#  ==================================
#
#  K Lawson April 2019
# 
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from time import sleep

# IO Mapper class, maps GPIO # to output numbers
#
class HSD(object):
	# Map IO numbers to GPIO Numbers
	O1 = 17
	O2 = 15
	O3 = 14
	O4 = 4
	O5 = 3
	O6 = 2
	O7 = 18
	O8 = 27
	O9 = 24
	O10 = 10
	O11 = 9
	O12 = 25
	O13 = 11
	O14 = 8
	O15 = 7
	O16 = 5
	O17 = 6
	O18 = 12
	O19 = 13
	O20 = 19
	O21 = 16
	O22 = 26
	O23 = 20
	O24 = 21
 	RUN = 22
	OE = 23

	def __setattr__(self, *_):
		pass
  
HSD = HSD()


# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#

# @@@@ Hardware init @@@@
#
o1 = LED(HSD.O1); 
o2 = LED(HSD.O2); 
o3 = LED(HSD.O3); 
o4 = LED(HSD.O4); 
o5 = LED(HSD.O5); 
#o6 = LED(O6) 
o6 = PWMLED(HSD.O6,True,0,1000);
o7 = LED(HSD.O7); 
o8 = LED(HSD.O8); 
o9 = LED(HSD.O9); 
o10 = LED(HSD.O10); 
o11 = LED(HSD.O11); 
o12 = LED(HSD.O12); 
o13 = LED(HSD.O13); 
o14 = LED(HSD.O14); 
o15 = LED(HSD.O15); 
o16 = LED(HSD.O16); 
o17 = LED(HSD.O17); 
o18 = LED(HSD.O18); 
o19 = LED(HSD.O19); 
o20 = LED(HSD.O20); 
o21 = LED(HSD.O21); 
o22 = LED(HSD.O22); 
o23 = LED(HSD.O23); 
o24 = LED(HSD.O24); 

enable = LED(HSD.OE);
run = LED(HSD.RUN);
#
# @@@@ END HW INIT @@@@

# Enable outputs
#
enable.on()

# flash LED and drive output at variable rate 0-100% duty cycle 
while True:
	# rate toggle output 6
	#
	o6.value = 0;
	print "pause at off"
	sleep(5)
	for b in range(100):
		# flash LED
		sleep(.1)
		run.toggle()
		# PWM to output
		o6.value  = b / 100.0
		print b, "% duty"
	print "pause at full..."
	sleep(5)
	
	#  turn on all outputs in 5s steps...
	#
	print "turning all outputs on..."
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
	print "Done"
	sleep(5)
	
	# Disable outputs
	#
	print "turning outputs off"
	enable.off()
	sleep(10)
	
	
