## PiIO Rasbian administrtion guide

### Image

All examples were witten using rasbian stretch lite.


### Dependencies

__Python packages__ 

| Item | Notes |
| ---- | ----- |
| concurrent-futures | python concurrency framework |
| paho-mqtt | python mqtt client |
| gpiozero | python gpio framework |
| smbus | python smbus framework |
| pyowm | python open weather map framework |

All packages need to be installed as root e.g. [sudo pip3 install paho-mqtt]


__linux packages__

| Item | Notes |
| ---- | ----- |
| mosquitto | mqtt broker |
| python3.5 | Varsion 3.5+ |
| python-pip3 | package installer for python |
| git | revision control package |
| node red | user interface and / or control via mqtt |
 
All packages can be installed using apt-get e.g. [sudo apt-get install python-pip3]  
Use [python3 --version] to find out what version you are running.
 
 
### Auto boot programs

* The file __etc/rc.local__ can be modified to automatically boot python programs after a reboot.
* To subsequently kill this program use the command [sudo killall python3]
* Use command [ps -A | grep python] to check if it is running


### Basic config of stretch

Use [sudo raspi-config] to perform the following basic tasks.

* __Enable ssh__ required for remote admin i.e. no keyboard and monitor
* __Enable spi__ required for ADIO board
* __Enable i2c__ required for ADIO board
* __Enable wifi__ required if LAN cable not used

Further notes on how to do this can be found here:  
[https://www.raspberrypi.org/documentation/configuration/raspi-config.md]


### Remote management

Can be done once wifi is setup using ssh and by editing files using nano.  
A terminal debugger is provided in some of the examples to help.


### Local management

If possible it's easer to hook a monitor and keyboard up to the pi and edit the files locally.  
The range of editors will be much better if you use the destop version of stretch.  
If you can using a LAN cable is more reliable than wifi also.  
If you do this you can substitute __nano__ out for __geany__, __gedit__ or __thonny__ (the best)  
