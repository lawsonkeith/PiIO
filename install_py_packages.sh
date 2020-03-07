#!/bin/sh
clear
tput setab 1; echo " ** installing python packages ** "; tput  sgr 0
sleep 3
echo
#tput setab 1; echo "1. concurrent-futures"; tput  sgr 0
#echo Used for concurrency example
#sleep 3
#sudo pip3 install concurrent-futures
tput setab 1; echo "1. paho-mqtt"; tput  sgr 0
echo messaging for node red examples
sleep 3
sudo pip3 install paho-mqtt
tput setab 1; echo "2. gpiozero"; tput  sgr 0
echo used to control the gpio
sleep 3
sudo pip3 install gpiozero
tput setab 1; echo "3. smbus"; tput  sgr 0
echo used to control spi devices on analog board
sleep 3
sudo pip3 install smbus
tput setab 1; echo "4. pyowm"; tput  sgr 0
echo weather reading api - used in node red example
sleep 3
sudo pip3 install pyowm
tput setab 1; echo "5. RPi"; tput  sgr 0
echo used in the temp sensor API (currently!)
sleep 3
sudo pip3 install RPi.gpio


