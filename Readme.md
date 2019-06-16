## PiIO python library

![](https://github.com/lawsonkeith/PiIO/raw/master/images/PhiSide.PNG)


An Python3 IO library for the Paspberry Pi PiIO boards which demonstrates:

* GPIO IO ancluding SPI and I2C peripheral access
* A basic PLC style library containing basic control functions
* A framework for concurrency
* Example node red interface using pub sub topics


There are examples for the three PiIO PCBs:

* [DO24 PCB](./docs/Readme_DO24.md)
* [DIO12 PCB](./docs/Readme_DIO12.md)
* [ADIO PCB](./docs/Readme_ADIO.md)


As well as a description of the four main software topics:

* [System admin](./docs/Readme_Admin.md)
* [PiIO Library](./docs/Readme_PiIO.md)
* [Concurrency](./docs/Readme_Concurrency.md)
* [Node red](./docs/Readme_NodeRed.md)


Example | Description
--- | ---
basic_DO.py | Simple usage of DO PCB
concurrent_DO.py | As above but implementing basic concurrency 
basic_DIO.py | Basic usage of DIO PCB
nodered_DIO.py | as above but with node red UI interface
basic_ADIO.py | Basic usage of analog PCB
PiIO.py | Low level library holding PCB abstractions and utility functions
basic_functs.py | examples for PiIO utility funciotns such as timer functs
sudo pip3 install Adafruit-ADS1x15
sudo python3 setup.py install
