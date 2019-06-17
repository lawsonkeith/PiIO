## DO24 PCB

![](https://github.com/lawsonkeith/PiIO/raw/master/images/PhiSide.PNG)

### PCB description
The PCB has the following functionality:

* 24 x 5-24V High side outputs
* One user controlled user LED for diagnostics
* One LED to indicate field supply present
* Overload fault LED
* 24 x 3.5mm terminal blocks for high side outputs
* 350mA max output per channel with overcurrent protection (High side)
* 1 x Field supply to power high side drivers
* 1 x 5V terminal block for Pi 5V optional power
* 1 x Output enable to enable / disable all outputs, this also resets faults

The device uses Darlington transistors with a saturation voltage of 1.6-1.8V, therefore the output voltage of will be VField - Vsat.
In some applications this will cause problems with driving  relay coils:

VField | Rated VCoil | VCoil | Note
------- | ------ | ------- | -----
5 | 5 | 3.2 | Will not work
5 | 3V3 | 3.2 | Ok
12 | 12 | 10.2 | Ok
24 | 24 | 22.2 | Ok


* The LED is designed to be cycled by the user program to show that is is running.
* VField can range from 5-24V

### PCB Pinout

Output | RPI GPIO number
---- | ----
O1 | 17
O2 | 15
O3 | 14
O4 | 4
O5 | 3
O6 | 2
O7 | 18
O8 | 27
O9 | 24
O10 | 10
O11 | 9
O12 | 25
O13 | 11
O14 | 8
O15 | 7
O16 | 5
O17 | 6
O18 | 12
O19 | 13
O20 | 19
O21 | 16
O22 | 26
O23 | 20
O24 | 21
RUN | 22
OE | 23


### Fault protection

* Each ouput can hold 350mA and trip just above 500mA.  Between these values behavious is undefined.
* When an output trips on overcurrent it remains off untill the Enable pin is cycled, only the pins on the devices that have overloaded will remain off.
* The Fault LED indicates that a overcurrent or thermal shutdown has occured on one of the 8 drive ICs
* For a thermal shutdown the entire device is shut down and all outputs are de-energised.
* Thermally each IC can drive .8A in total over all 8 outputs at 24V DC @ 24 DegC.  
* The board can therefore  drive up to 2.4A in total if spread correctly across the 3 driver ICs.


### Software description

The PiIO library provides mapping functions for this boards.

'''python
# import mapper
from PiIO import PiIO_DO24_Mapper

# @@@@ Hardware init @@@@
#
io = PiIO_DO24_Mapper()
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

enable = LED(io.OE);
run = LED(io.RUN);
'''

We can now control the outputs using the GPIO zero library, we can use them as digital outs or PWM outs.

'''python
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

	for b in range(100):
		# flash LED
		sleep(.1)
		
		# PWM to output
		o6.value  = b / 100.0
		print(b, "% duty")

	sleep(5)
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
'''
