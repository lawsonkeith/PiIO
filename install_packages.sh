#!/bin/sh
clear
tput setab 1; echo " ** installing linux packages ** "; tput  sgr 0
sleep 3
echo
tput setab 1; echo "1. mosquito"; tput  sgr 0
echo Used for node red examples for messaging
sleep 3
sudo apt-get install mosquitto
tput setab 1; echo "2. python 3.5"; tput  sgr 0
echo "The language we're using"
sleep 3
sudo apt-get install python3.5
sudo apt-get install python3-pip
tput setab 1; echo "3. node red"; tput  sgr 0
echo User interface etc
sleep 3
sudo apt-get install nodered
sudo apt-get install npm
echo Adding user interface componets....
sleep 3
cd ~/.node-red
npm install node-red-contrib-ui
cd PiIO
echo done!
