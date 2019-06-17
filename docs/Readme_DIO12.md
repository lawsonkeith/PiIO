## DIO12 PCB

![](https://github.com/lawsonkeith/PiIO/raw/master/images/PhiSide.PNG)

# PCB description
The PCB has the following functionality:

* 12 x 5-24V High side outputs
* 12 x 3.3-24V Digital inputs
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


# Fault protection

* Each ouput can hold 350mA and trip just above 500mA.  Between these values behavious is undefined.
* When an output trips on overcurrent it remains off untill the Enable pin is cycled, only the pins on the devices that have overloaded will remain off.
* The Fault LED indicates that a overcurrent or thermal shutdown has occured on one of the 8 drive ICs
* For a thermal shutdown the entire device is shut down and all outputs are de-energised.
* Thermally each IC can drive .8A in total over all 8 outputs at 24V DC @ 24 DegC.  
* The board can therefore  drive up to 2.4A in total if spread correctly across the 3 driver ICs.


# Software description

The PiIO software library provides a means of interfaceing to the PCB.

```python
# import PiIO library
from PiIO import PiIO_DIO12_Mapper

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
```

The GPIO zero library can now be used to control the IO.

```python
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


```

 
