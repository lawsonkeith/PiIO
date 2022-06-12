## PiIO python repository

![](https://github.com/lawsonkeith/PiIO/raw/master/images/PiIO_logo_sm.PNG)

This is a Python3 IO library for the Raspberry Pi PiIO boards which demonstrates:

* GPIO IO ancluding SPI and I2C peripheral access
* A basic PLC style library containing basic control functions
* A framework for concurrency
* Example node red interface using pub sub topics

The main repository for board level information is now the [PiIO Web page](https://PiIO.co.uk).
Read the admin page for information on installing the packages.

A description of the resources available per board is available here:

### Gen 2 - H series
* [PiIO-232-H](./docs/Readme_232_H.md)
* [PiIO-DO-H](./docs/Readme_DO_H.md)
* [PiIO-DIO-H](./docs/Readme_DIO_H.md)
* [PiIO-DIO-HZ](./docs/Readme_DIO_HZ.md)
* [PiIO-ADIO-H](./docs/Readme_ADIO_H.md)


### Gen 1 - original boards
* [PiIO-DIO](./docs/Readme_DIO12.md)
* [PiIO-ADIO](./docs/Readme_ADIO.md)
* [PiIO-DO24](./docs/old/Readme_DO24.md)

As well as a description of the four main software topics:

* [System admin](docs/Readme_Admin.md)
* [PiIO Library](docs/Readme_PiIO.md)
* [Concurrency](docs/Readme_Concurrency.md)
* [Node red](docs/Readme_NodeRed.md)


## Porting
Should you wish to port this to another language such as C++, refer to the PiIO.py file.
This contains GPIO mappings and other useful info.
