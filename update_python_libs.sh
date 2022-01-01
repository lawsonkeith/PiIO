#!/bin/sh
#
tput clear
tput setab 1
echo "> updating PiIO global python libraries "
tput sgr0
sudo python3 setup.py install
cd examples
echo done..
