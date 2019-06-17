## ADIO PCB

![](https://github.com/lawsonkeith/PiIO/raw/master/images/enclosure1.PNG)

### PCB description
The PCB has the following functionality:

* One Field input which also powers the RPi
* 8 x 5-24V High side outputs
* 4 x 0-24V digital inputs
* 350mA max output per channel with overcurrent protection (High side)
* 1 x Output enable to enable / disable all outputs, this also resets faults
* One user controlled user LED for diagnostics
* One LED to indicate field supply present
* Overload fault LED
* One 3 wire PT100 interface
* Two 0-10V analog outputs
* Four 0-10V or 0-20mA inputs with programmable gain
* Empty header for I2C interfacing
* Jumper for optionally feeding overload status back to software and disabling the run LED

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

A python example is provided to test PCB functionality.  This includes a class to handle the GPIO to output pin mapping.
The example uses the GPIOZero library.


### Software library

The PiIO library provides a means of communicating with the board using the RPI GPIO header.

```python
# import library
from PiIO import PiIO_Analog
```

The board uses a 4 channes ADS1115 ADC, this had a programmable gain which needs to be set, the input stage of the PCB has a gain of 0.2 to a 10V signal produces roughly 2V at the ADC.

```python
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
```

Larger or smaller gains can be used if you plan to interface to larger or smaller signals.

The IO is controlled using the GPIOZero library, the PiIO library provides wrapper classes to make this as easy as possible:

```python
# @@@@ Hardware init @@@@
#
adc = PiIO_Analog(GAIN)
run = LED(adc.RUN)
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
```

Using GPIO it's a good idea to flash the RUN led so we know there's a program running.

```python
# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#
run.blink(.100,.900)
```

Next we can use the class methods to control the rest of the board.


```python
print("> Do rate increase AO1")
for x in range(100):
	PWM1.value = x / 100.0
	sleep(.02)
	print(".",end='',flush=True)
print("")

sleep(2)
print("> Do rate increase AO2")
for x in range(100):
	PWM2.value = x / 100.0
	sleep(.02)
	print(".",end='',flush=True)
print("")


print("> Read temp")
temp = adc.get_temp()
print (" {:.2f}".format(temp)," DegC")

print("> Read DI 1-4")
for x in range(10):
	print(" IN1: ",IN1.is_pressed," IN2: ",IN2.is_pressed," IN3 ",IN3.is_pressed," IN4 ",IN4.is_pressed)
	sleep(1)

print("> DO Output 1..8")
OE.on()
print(" ..1",end='',flush=True)	
O1.on()
sleep(2)
print("..2",end='',flush=True)	
O2.on()
sleep(2)
print("..3",end='',flush=True)	
O3.on()
sleep(2)
print("..4",end='',flush=True)	
O4.on()
sleep(2)
print("..5",end='',flush=True)	
O5.on()
sleep(2)
print("..6",end='',flush=True)	
O6.on()
sleep(2)
print("..7",end='',flush=True)	
O7.on()
sleep(2)
print("..8",end='',flush=True)	
O8.on()
sleep(2)
print("")
print("> wait")
sleep(10)
```
