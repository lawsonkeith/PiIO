Useful commands
===============

Linux
=====
ATL1-12													new terminal

sudo raspi-config										config
sudo i2cdetect -y 1										detect i2c devices
sudo apt-get install i2cdetect
sudo ps -A												show processes


Nano
====



Serial
======



Python
======
pip3 install pyserial									get serial port lib

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

