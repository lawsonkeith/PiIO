## PiIO user library

The PiIO user library is a library containing functions to:

* Control specific boards
* Provide generic control functions

![](https://github.com/lawsonkeith/PiIO/raw/master/images/framework.PNG)

### Board specific API - H boards
Gen 2 board mappers.

| Class | Applies to | Description |
| --- | --- | --- |
| PiIO_232_H_Mapper | PiIO 232 H PCB | Class for controlling PCB |
| PiIO_DIO_H_Mapper | PiIO DIO H PCB | Class for controlling PCB |
| PiIO_DIO_HZ_Mapper | PiIO DIO HZ PCB | Class for controlling PCB |
| PiIO_DO_H_Mapper | PiIO DO H PCB | Class for controlling PCB |

### Board specific API - original boards
Gen 1 board mappers.

| Class | Applies to | Description |
| --- | --- | --- |
| PiIO_Analog | PiIO ADIO PCB | Class for controlling PCB |
| PiIO_DIO12_Mapper | PiIO DIO12 PCB | Class for controlling PCB |
| PiIO_DO24_Mapper | PiIO DO24 PCB | Class for controlling PCB |


### Generic API

| Class | Description |
| --- | --- |
| PiIO_Col | Class providing definitions to control terminal colours |
| PiIO_getc | Function to provide non blocking terminal char capture |
| PiIO_timer | Funciton to provide basic timer to time actions (ascii) |
| PiIO_RunEvery | Enables timed periodic calls |
| PiIO_EMA | Provides exponential moving average |
| PiIO_Alarm | Provides basic min max alarm on a variable |
| PiIO_Scale | Provides basic scaling on a variable |
| PiIO_Redge | Provides rising edge detection |
| PiIO_Fedge | Provides falling edge detection |
| PiIO_TON | Provides timed on function |
| PiIO_TOF | Provides timed off function |
| PiIO_TP | Provides timed pulse function |


### Usage

The program [basic_functs.py] provides examples of the generic functions and the board specific examples provide examples of the others.
The file [PiIO.py] provides an in depth description of the function calls.
The API can be accessed from within python as follows:

```python
from PiIO import PiIO_DO24_Mapper
from PiIO import PiIO_Analog
from PiIO import PiIO_col
from PiIO import PiIO_getc
from PiIO import PiIO_timer
from PiIO import PiIO_EMA
```

### GPIOZero
The examples use GPIO Zero, it will work with other PI GPIO class's as well e.g. RPI.gpio.
For digital inputs not pullups must be set to OFF, if your IO needs a pullup you will need to add it externally.


### Modifying the library

The API can be updated using the upd script, this copies the local version to the global library location and is useful if you want to modify any of the functions.

```
$ upd

```


### Installation

First time library installation can be achieved using the setup script.  Alternatively use the above method which is functionally identical.


```
$ sudo python3 setup.py install
```
