## PiIO DIO H PCB

![](https://github.com/lawsonkeith/PiIO/raw/master/images/PiIO_DIOH_ASS.png)

### Description
The PCB has the following functionality:

* 12 Digital outputs
* 12 Digital inputs
* One RUN LED

For more information please refer to the manual located at [PiIO](https://PiIO.co.uk).

### Software description
Python 3 example programs are provided to allow you to quickly explore the boards features.

Example | Description
--- | ---
DIO_H_basic.py | Basic usage of DIO H
DIO_H_nodered_direct.json | Node red directly controlling GPIO
DIO_H_nodered.py | nodered but using mqt server (code in python)
DIO_H_nodered.json | nodered flow for above
DIO_H_sounder_prox.py | demo which reads a rorary sensor and controls some basic IO
../basic_functs.py | examples for PiIO utility functions such as timer functs etc
