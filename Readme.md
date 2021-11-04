## PiIO python repository

![](https://github.com/lawsonkeith/PiIO/raw/master/images/PiIO_logo_sm.PNG)

This is a Python3 IO library for the Raspberry Pi PiIO boards which demonstrates:
The main repository for board level information is now the [PiIO Web page](https://PiIO.co.uk).
Read the admin page for information on installing the packages.


* GPIO IO ancluding SPI and I2C peripheral access
* A basic PLC style library containing basic control functions
* A framework for concurrency
* Example node red interface using pub sub topics

A description of the recources available per board is available here:

* [PiIO-232-H](./docs/Readme_232_H.md)
* [PiIO-DO-H](./docs/Readme_DO_H.md)
* [PiIO-DIO](./docs/Readme_DIO12.md)
* [PiIO-ADIO](./docs/Readme_ADIO.md)


As well as a description of the four main software topics:

* [System admin](docs/Readme_Admin.md)
* [PiIO Library](docs/Readme_PiIO.md)
* [Concurrency](docs/Readme_Concurrency.md)
* [Node red](docs/Readme_NodeRed.md)


## Archive
Discontinued board information is archived here:
* [PiIO-DO24](./docs/old/Readme_DO24.md)

## Porting
Should you wish to port this to another language such as C++, refer to the PiIO.py file.
This contains GPIO mappings and other useful info.
