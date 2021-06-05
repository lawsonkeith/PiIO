Useful commands
===============

Linux
=====
ATL1-12													new terminal

sudo raspi-config										config
sudo i2cdetect -y 1										detect i2c devices
sudo apt-get install i2cdetect
sudo ps -A												show processes

dmesg | grep											look at startup cmds
top														performance tasks
ifconfig												ip stuff
man ls													manual

Nano
====
nano /etc/nanorc										config
set linenumbers
alt+s													scroll mode
alt+u													undo
ctrl/alt space											move 1 word
ctrl w r 												search replace
alt a 6 												select copy
ctrl u													paste
alt >													next buffer
alt p 													whitespaces
alt del													del line

Serial
======
minicom 


Python
======
pip3 install pyserial									get serial port lib
sudo python3 setup.py install							install/update PiIO lib

Minicom
========
Ctrl+A X												quit
minicom -b 19200 -o -D /dev/ttyAMA0						serial tests


Git
===
git clone https://github.com/lawsonkeith/PiIO.git		Clone repo
git status
git pull origin master
git reset --hard HEAD									ditch local changes
git status
git commit -am "some msg"								commit changes

GPIO
====
pinout													show pinout
ls /dev | grep spi										is spi enabled?
ls /dev | grep i2c 										is i2c enabled?
sudo raspi-config										enable peripherals / ssh