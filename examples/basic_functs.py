#!/usr/bin/python3
#  example usage of PiIO library functs 
#  ====================================
#
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
from PiIO import PiIO_Scale
from PiIO import PiIO_Redge
from PiIO import PiIO_TOF
from PiIO import PiIO_TP
from PiIO import PiIO_Fedge
from PiIO import PiIO_TON
from PiIO import PiIO_EMA
from PiIO import PiIO_Alarm
from time import sleep

print("Testing PiIO Utility functions")
sleep(2)

# Test alarm
#
print("\n>>TESTING ALARM 0 100")
sleep(1)
alm=PiIO_Alarm(0,100)
print("4",alm.alarm(4))
print("4",alm.alarm(4))
print("4",alm.alarm(4))
print("99",alm.alarm(99))
print("101",alm.alarm(101))
print("99",alm.alarm(99))
print("1",alm.alarm(1))
print("ack")
alm.ack()
print("99", alm.alarm(99))
print("-1", alm.alarm(-1))
print("1", alm.alarm(1))
print("ack")
alm.ack()
print("1", alm.alarm(1))


# Test ema
#
print("\n>>TESTING EMA (0-1) small = much avg")
sleep(1)
ema=PiIO_EMA(.1)
print("0.1 = HIGH FILTERING")
print(ema.ema(9))
print(ema.ema(7))
print(ema.ema(4))
print(ema.ema(9))
print(ema.ema(3))
print(ema.ema(6))
print(ema.ema(9))
print(ema.ema(2))
print(ema.ema(5))
print(ema.ema(1))
print("0.9 = LOW FILTERING")
ema=PiIO_EMA(.9)
print(ema.ema(9))
print(ema.ema(7))
print(ema.ema(4))
print(ema.ema(9))
print(ema.ema(3))
print(ema.ema(6))
print(ema.ema(9))
print(ema.ema(2))
print(ema.ema(5))
print(ema.ema(1))

# Test scale
#
print("\n>>TESTING SCALE")
sleep(1)
sc=PiIO_Scale(4,20,0,1000)
print(sc.scale(4))
print(sc.scale(12))
print(sc.scale(20))

# Test Redge
#
print("\n>>TESTING REDGE")
t = PiIO_Redge(0);
sleep(1)
print(0, t.redge(0));
print(1, t.redge(1));
print(1, t.redge(1));
print(1, t.redge(1));
print(0, t.redge(0));
print(1, t.redge(1));
print(0, t.redge(0));
print(0, t.redge(0));

# Test Fedge
#
print("\n>>TESTING FEDGE")
t = PiIO_Fedge(0);
sleep(1)
print(0, t.fedge(0));
print(1, t.fedge(1));
print(1, t.fedge(1));
print(1, t.fedge(1));
print(0, t.fedge(0));
print(1, t.fedge(1));
print(0, t.fedge(0));
print(0, t.fedge(0));

# Test TP
#
print("\n>>TESTING TP .22s")
tp = PiIO_TP(0,.22)
sleep(1)
tp.tp(0)
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(1, tp.tp(1))
sleep(.1)
print(1, tp.tp(1))
sleep(.1)
print(1, tp.tp(1))
sleep(.1)
print(1, tp.tp(1))
sleep(.1)
print(1, tp.tp(1))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(1, tp.tp(1))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(1, tp.tp(1))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(1, tp.tp(1))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))
sleep(.1)
print(0, tp.tp(0))


# Test TON
#
print("\n>>TESTING TON .22s")
ton = PiIO_TON(0,.22)
sleep(1)
sleep(.1)
print(0, ton.ton(0))
sleep(.1)
print(0, ton.ton(0))
sleep(.1)
print(1, ton.ton(1))
sleep(.1)
print(1, ton.ton(1))
sleep(.1)
print(1, ton.ton(1))
sleep(.1)
print(1, ton.ton(1))
sleep(.1)
print(0, ton.ton(0))
sleep(.1)
print(1, ton.ton(1))
sleep(.1)
print(1, ton.ton(1))
sleep(.1)
print(1, ton.ton(1))
sleep(.1)
print(0, ton.ton(0))
sleep(.1)
print(1, ton.ton(1))
sleep(.1)
print(0, ton.ton(0))
sleep(.1)
print(0, ton.ton(0))
sleep(.1)
print(0, ton.ton(0))
sleep(.1)
print(0, ton.ton(0))

# Test TOFF
#
print("\n>>TESTING TOF .22s")
tof = PiIO_TOF(0,.22)
sleep(1)
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(1, tof.tof(1))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(1, tof.tof(1))
sleep(.1)
print(1, tof.tof(1))
sleep(.1)
print(1, tof.tof(1))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(0, tof.tof(0))
sleep(.1)
print(0, tof.tof(0))

