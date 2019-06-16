## ADIO PCB

_TODO:_ update

![](https://github.com/lawsonkeith/PiIO/raw/master/images/PhiSide.PNG)

An IO library for the PiIO boards which demonstrate

* GPIO IO ancluding SPI and I2C peripheral access
* A basic PLC style library containing basic control functions
* A framework for concurrency
* Example node red interface using pub sub topics

There are examples for the three PiIO PCBs:

[DO24 PCB](./Docs/Readme_DO24.md)
[DIO12 PCB](./Docs/Readme_DIO12.md)
[ADIO PCB](./Docs/Readme_ADIO.md)

As well as a description of the four frameworks:

[PiIO Library](./Docs/Readme_PiIO.md)
[Concurrency](./Docs/Readme_Concurrency.md)
[Node red](./Docs/Readme_NodeRed.md)


# PCB description
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

# PCB Pinout

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


# Fault protection

* Each ouput can hold 350mA and trip just above 500mA.  Between these values behavious is undefined.
* When an output trips on overcurrent it remains off untill the Enable pin is cycled, only the pins on the devices that have overloaded will remain off.
* The Fault LED indicates that a overcurrent or thermal shutdown has occured on one of the 8 drive ICs
* For a thermal shutdown the entire device is shut down and all outputs are de-energised.
* Thermally each IC can drive .8A in total over all 8 outputs at 24V DC @ 24 DegC.  
* The board can therefore  drive up to 2.4A in total if spread correctly across the 3 driver ICs.


# Software description

A python example is provided to test PCB functionality.  This includes a class to handle the GPIO to output pin mapping.
The example uses the GPIOZero library.


#Tools

_Concurrency_
* pip3 python package manager [sudo apt-get install python-pip]
* Python twisted for concurrency [sudo apt-get install python-twisted]
 [TODO] 
 some work here to get correct python packages to install...
 sudo apt install python3-pip
 sudo python3.5 -m pip install twisted
 pip3 install service_identity


_GPIO_
* GPIOZero for pi [sudo apt install python3-gpiozero]

_General_
* gedit text editor  [sudo apt-get install gedit]

_Node red_
* [sudo apt-get install node-red]

sudo apt-get install -y i2c-tools
i2cdetect -y 1
pip3 install gpiozero
pip3 install smbus
http://www.python-exemplary.com/index_en.php?inhalt_links=navigation_en.inc.php&inhalt_mitte=raspi/en/adc.inc.php

sudo apt-get -y install python3-rpi.gpio
