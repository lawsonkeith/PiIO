#  PiIO General library module ===========================
#
#  K Lawson 2022
#
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
# IO Mapper class, maps GPIO # to output numbers
#
from PiIO.PiIO_ADS1x15 import ADS1015
import PiIO.PiIO_max31865
import time,datetime
import sys, termios, fcntl, os

# Define some colours for terminals etc
#
class PiIO_col:
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	#
	RED = '\033[31m'
	GREEN = '\033[32m'
	BLUE = '\033[34m'
	WHITE = '\033[37m'
	BLACK = '\033[30m'
	ORANGE = '\033[33m'
	MAGENTA = '\033[35m'
	CYAN = '\033[36m'
	LGRAY = '\033[37m'
	#
	REDB = '\033[41m'
	GREENB = '\033[42m'
	BLUEB = '\033[44m'
	WHITEB = '\033[47m'
	BLACKB = '\033[40m'
	ORANGEB = '\033[43m'
	MAGENTAB = '\033[45m'
	CYANB = '\033[46m'
	LGRAYB = '\033[47m'
	DGRAYB = '\033[100m'
	WHITEB = '\033[107m'
	YELLOWB = '\033[103m'
	#
	ENDC= '\033[0m'
	#
	HOME = '\033[0;0H'
	CLR = '\033[2J'
	RESET = '\033[0;0H\033[2J'


# This is a funciton to get a char from the keyboard in a non blocking way
#
def PiIO_getc():
	try:
		c = None
		fd = sys.stdin.fileno()
		oldterm = termios.tcgetattr(fd)
		newattr = termios.tcgetattr(fd)
		newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
		termios.tcsetattr(fd, termios.TCSANOW, newattr)

		oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

	#try:
		c = sys.stdin.read(1)

		termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

	except:
		 pass

	return c


# Function to do a days hrs mins secs timer, returns time as a string
#
class PiIO_timer:
	start_time = 0

	def __init__(self):
		self.start_time = time.time()

	def reset(self):
		self.start_time = time.time()

	def read(self):
		diff = time.time() - self.start_time

		m, s = divmod(int(diff), 60)
		h, m = divmod(m, 60)
		d, h = divmod(h, 24)

		str =  '{:d} days {:d}:{:02d}:{:02d}'.format(d, h, m, s)
		return str

# Basic time function run every n secs without sleep()
#
class PiIO_RunEvery:
	tgt_time=0
	time_span=0

	def __init__(self,time_span):
		self.time_span = time_span

	def run(self):
		if(time.time() > tgt_time):
			self.tgt_time = time.time() + self.time_span
			return True
		else:
			return False

	def set_time_mins(self,time_span):
		self.time_span = time_span * 60

	def set_time_hrs(self,time_span):
		self.time_span = time_span * 60 * 60

	def set_time_secs(self,time_span):
		self.time_span = time_span

	def set_time_msecs(self,time_span):
		self.time_span = time_span / 1000.0



# Moving (exponential) average function
#
class PiIO_EMA:
	alpha=0
	average=0

	def __init__(self,alpha):
		self.alpha=alpha

	def ema(self,current):
		'''
		Exponential moving average generator
		http://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average
		Higher alpha discounts old results faster, alpha in range (0, 1).
		'''
		self.average = current * self.alpha + self.average * (1 - self.alpha)
		return self.average

# Really basic alarm function
#
class PiIO_Alarm:
	amin=0
	amax=0
	alarm_st=False

	def __init__(self,amin,amax):
		self.amin=amin
		self.amax=amax

	def alarm(self,proc):
		if(proc > self.amax):
			self.alarm_st=True

		if(proc < self.amin):
			self.alarm_st=True

		return self.alarm_st

	def ack(self):
		self.alarm_st=False

# really basic scale
#
class PiIO_Scale:
	rmin=0
	rmax=0
	smin=0
	smax=0

	def __init__(self,rmin,rmax,smin,smax):
		self.rmin=rmin
		self.rmax=rmax
		self.smin=smin
		self.smax=smax

	def scale(self,raw):
		m = (self.smax-self.smin) / (self.rmax-self.rmin)
		c = self.smax - (m * self.rmax)
		return raw * m + c

# Rising edge detector
#
class PiIO_Redge:
	last_state=0

	def __init__(self,state):
		self.last_state = state

	def redge(self,state):
		if (self.last_state == 0 and state > 0):
			self.last_state = state
			return True

		self.last_state = state
		return False


# Falling edge detector
#
class PiIO_Fedge:
	last_state=0

	def __init__(self,state):
		self.last_state = state

	def fedge(self,state):
		if (self.last_state > 0 and state == 0):
			self.last_state = state
			return True

		self.last_state = state
		return False

# Timed pulse function
# On a REDGE set the output high for time period
#
class PiIO_TP:
	last_state=0
	# pulse length
	time_pulse=0
	# end time
	end_time=0

	def __init__(self,state,time):
		self.last_state = state
		self.time_pulse = time

	def tp(self,state):
		tc = time.time()
		# redge
		if (self.last_state == 0 and state > 0):
			self.end_time = tc + self.time_pulse

		# pulse occring
		if (self.end_time > tc):
			self.last_state = state
			return True

		self.last_state = state
		return False

# Time delayed on
# If input high delay turn on by specified time
#
class PiIO_TON:
	last_state=0
	# pulse length
	time_delay=0
	# end time
	end_time=0

	def __init__(self,state,time):
		self.last_state = state
		self.time_delay = time

	def set_time(self,time):
		self.time_delay = time

	def ton(self,state):
		tc = time.time()

		# redge
		if (self.last_state == 0 and state > 0):
			self.end_time = tc + self.time_delay

		self.last_state = state

		# on condition
		if (state > 0):
			if( tc > self.end_time):
				return True

		return False


# If input high delay turn off by specified time
#
class PiIO_TOF:
	last_state=0
	# pulse length
	time_delay=0
	# end time
	end_time=0

	def __init__(self,state,time):
		self.last_state = state
		self.time_delay = time

	def set_time(self,time):
		self.time_delay = time

	def tof(self,state):
		tc = time.time()

		# fedge
		if (self.last_state > 0 and state == 0):
			self.end_time = tc + self.time_delay

		self.last_state = state

		# on conditions
		if (state > 0):
			return True

		if( tc < self.end_time):
			return True

		return False


#########################################################################
# EARLY BOARDS NOT CONFORMING TO HAT MECHANICAL SPECIFICATION		#
# 1. Board is not rectangular						#
# 2. Uses UDN series of darlington drivers				#
#########################################################################

# Class to interface to the PIIO analog board
#
class PiIO_Analog:
	# GPIO Mapping
	O1 = 5
	O2 = 6
	O3 = 13
	O4 = 16
	O5 = 19
	O6 = 20
	O7 = 26
	O8 = 21
	RUN=25
	OE=12
	PWM1=17
	PWM2=27
	# GPIO Mapping
	I1 = 22
	I2 = 23
	I3 = 24
	I4 = 8
	FAULT=7
	# Constants
	gain = 1;
	data = 0;

	def __init__(self,gain):
		self.adc = ADS1015()
		self.gain = gain
		csPin = 18
		misoPin = 9
		mosiPin = 10
		clkPin = 11

		self.max = PiIO.PiIO_max31865.max31865(csPin,misoPin,mosiPin,clkPin)

	def get_raw(self,channel):
		data = 0;
		data =  self.adc.read_adc(channel, self.gain)
		time.sleep(.001)
		return data  # 2032 is 10V @ gain of 2

	def get_scaled(self,channel):
		data = 0;
		data = self.adc.read_adc(channel, self.gain)
		# ADC input impedance is 6MR in 2V gain
		# Rratio	0.2006
		# Vmax		10V
		# Va dc@MAX	2.006 V
		# Raw@MAX V	2006
		#
		# RawToVolts Scale		0.00492
		# data *= 4.92 / 1000 this was wrong did not take into account ADC resistance
		data *= 4.985 / 1000
		time.sleep(.001)
		return data #(volts)

	def get_temp(self):
		tempC = self.max.readTemp()
		return tempC


# class to interface to the PIIO digi out 24 board
#
class PiIO_DO24_Mapper(object):
	# Map IO numbers to GPIO Numbers
	O1 = 17
	O2 = 15
	O3 = 14
	O4 = 4
	O5 = 3
	O6 = 2
	O7 = 18
	O8 = 27
	O9 = 24
	O10 = 10
	O11 = 9
	O12 = 25
	O13 = 11
	O14 = 8
	O15 = 7
	O16 = 5
	O17 = 6
	O18 = 12
	O19 = 13
	O20 = 19
	O21 = 16
	O22 = 26
	O23 = 20
	O24 = 21
	RUN = 22
	OE = 23

	def __setattr__(self, *_):
		pass


#
class PiIO_DIO12_Mapper(object):
	# Map IO numbers to GPIO Numbers
	O1 = 17
	O2 = 15
	O3 = 14
	O4 = 4
	O5 = 3
	O6 = 2
	O7 = 18
	O8 = 27
	O9 = 24
	O10 = 10
	O11 = 9
	O12 = 25
	I1 = 11
	I2 = 8
	I3 = 7
	I4 = 5
	I5 = 6
	I6 = 12
	I7 = 13
	I8 = 19
	I9 = 16
	I10 = 26
	I11 = 20
	I12 = 21
	RUN = 22
	OE = 23

	def __setattr__(self, *_):
		pass

#########################################################################
# BOARDS CONFORMING TO HAT MECHANICAL SPECIFICATION						#
# 1. Named PiIO-xxxx-H													#
# 2. Are rectangular													#
# 3. Use TBD62783 DMOS driver arrays									#
# 4. Do not have fault LED												#
#########################################################################

#
class PiIO_232_H_Mapper(object):
	# Map IO numbers to GPIO Numbers
	O1 = 19
	O2 = 25
	O3 = 10
	O4 = 24
	O5 = 23
	O6 = 22
	O7 = 27
	O8 = 18
	I1 = 9
	I2 = 11
	I3 = 8
	I4 = 7
	I5 = 5
	I6 = 6
	I7 = 12
	I8 = 13
	RUN = 26

	def __setattr__(self, *_):
		pass

#
class PiIO_DO_H_Mapper(object):
	# Map IO numbers to GPIO Numbers
	O1 = 22
	O2 = 27
	O3 = 18
	O4 = 17
	O5 = 15
	O6 = 4
	O7 = 3
	O8 = 2
	O9 = 1
	O10 = 0
	O11 = 11
	O12 = 25
	O13 = 23
	O14 = 24
	O15 = 10
	O16 = 9
	O17 = 5
	O18 = 6
	O19 = 12
	O20 = 13
	O21 = 19
	O22 = 16
	O23 = 26
	O24 = 20
	RUN = 21


class PiIO_DIO_HZ_Mapper(object):
	# Map IO numbers to GPIO Numbers
	O1 = 18
	O2 = 27
	O3 = 22
	O4 = 24
	O5 = 25
	O6 = 12
	O7 = 13
	O8 = 19

	I1 = 10
	I2 = 9
	I3 = 11
	I4 = 8

	RUN = 16

	def __setattr__(self, *_):
		pass


# Old version - do not use
class PiIO_DIO_H_Mapper(object):
	# Map IO numbers to GPIO Numbers
	O1 = 14
	O2 = 17
	O3 = 18
	O4 = 27
	O5 = 22
	O6 = 23
	O7 = 24
	O8 = 10
	O9 = 9
	O10 = 12
	O11 = 13
	O12 = 19

	I1 = 15
	I2 = 21
	I3 = 4
	I4 = 25
	I5 = 11
	I6 = 8
	I7 = 7
	I8 = 5
	I9 = 6
	I10 = 26
	I11 = 16
	I12 = 20

	RUN = 3

	def __setattr__(self, *_):
		pass



#
class PiIO_Analog_H_Mapper:
	# GPIO Mapping
	O1 = 14
	O2 = 17
	O3 = 18
	O4 = 27
	O5 = 22
	O6 = 23
	O7 = 24
	O8 = 10
	RUN=25
	# GPIO Mapping
	I1 = 11
	I2 = 8
	I3 = 7
	I4 = 5
	I5 = 6
	I6 = 12
	I7 = 13
	I8 = 19
	I9 = 16
	I10 = 26
	I11 = 20
	I12 = 21
	# Constants
	gain = 1;
	data = 0;

	def __init__(self,gain):
		self.adc = ADS1015()
		self.gain = gain
		#csPin = 18
		#misoPin = 9
		#mosiPin = 10
		#clkPin = 11

		#self.max = PiIO.PiIO_max31865.max31865(csPin,misoPin,mosiPin,clkPin)

	def get_raw(self,channel):
		data = 0;
		data =  self.adc.read_adc(channel, self.gain)
		time.sleep(.001)
		return data  # 2032 is 10V @ gain of 2

	def get_scaled(self,channel):
		data = 0;
		data = self.adc.read_adc(channel, self.gain)
		# ADC input impedance is 6MR in 2V gain
		# Rratio	0.2006
		# Vmax		10V
		# Va dc@MAX	2.006 V
		# Raw@MAX V	2006
		#
		# RawToVolts Scale		0.00492
		# data *= 4.92 / 1000 this was wrong did not take into account ADC resistance
		data *= 4.985 / 1000
		time.sleep(.001)
		return data #(volts)

	#def get_temp(self):
	#	tempC = self.max.readTemp()
	#	return tempC

