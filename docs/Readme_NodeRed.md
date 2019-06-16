## Node red

Node-RED is a programming tool for wiring together hardware devices, APIs and online services in new and interesting ways.

It provides a browser-based editor that makes it easy to wire together flows using the wide range of nodes in the palette that can be deployed to its runtime in a single-click.


### Installation

Installation of node red is covered here:

https://nodered.org/docs/getting-started/installation


### Dependencies

User interfaces done in my examples were done using __node-red-contrib-ui__.
This provides additional nodes to provide all the user interface components.

This can be installed as follows:

cd ~\.node-red
npm install node-red-contrib-ui


### Using

For my examples there are 2 node red browser addresses you will use (assuming a host IP of 192.168.1.4:

* __http://192.168.1.4:1880__ - Node red editor
* __http://192.168.1.4:1880/ui/#/0__ - User interface

The flows can be developed in the editor, in the examples saved versions of the flows are provided for experimentation.
Mqt messages are used to communicate with the underlying python program via the mosquito broker.  In this way the python programs are allways in control and the node-red interface is a bit like a SCADA application in that it just provides the user interface.

It is possible to just control everything from node-red since it has it's own GPIO control functions but this method of controlling the boards has not been covered in the examples.  Control of SPI and I2C devices isn't that easy but for basic DIO use cases using just node red is straightforward.  The mqt messaging nodes can be replaced with direct GPIO control node calls although it's then not possible to use the PiIO user library.

Node red can be controlled via the terminal as follows:

* __node-red-start__ - start node red
* __node-red-stop__ - stop node red
* __sudo systemctl enable nodered.service__ - set to autostart on boot
* __sudo systemctl disable nodered.service__ - turn off auto start


