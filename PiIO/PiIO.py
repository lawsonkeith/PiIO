#  PiIO General library module ===========================
#
#  K Lawson April 2019
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
	#
	REDB = '\033[41m'
	GREENB = '\033[42m'
	BLUEB = '\033[44m'
	WHITEB = '\033[47m'
	#
	ENDC= '\033[0m'
	#
	HOME = '\033[0;0H'
	CLR = '\033[2J'
	RESET = '\033[0;0H\033[2J'


def PiIO_getc():
	fd = sys.stdin.fileno()
	oldterm = termios.tcgetattr(fd)
	newattr = termios.tcgetattr(fd)
	newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
	termios.tcsetattr(fd, termios.TCSANOW, newattr)

	oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

	c = None

	try:
		c = sys.stdin.read(1)
	except IOError: pass

	termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

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
 


# Moving average function
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
	RUN=8
	OE=12
	PWM1=17
	PWM2=27
	# GPIO Mapping
	I1 = 22
	I2 = 23
	I3 = 24
	I4 = 25
	FAULT=7
	# Constants
	gain = 1;
	data = 0;

	def __init__(self,gain):
		self.adc = ADS1015()
		#self.adc = Adafruit_ADS1x15.ADS1015()

		self.gain = gain
		csPin = 18
		misoPin = 9
		mosiPin = 10
		clkPin = 11

		self.max = PiIO.PiIO_max31865.max31865(csPin,misoPin,mosiPin,clkPin)
#		return self.adc

	def get_raw(self,channel):
		data = 0;
		data =  self.adc.read_adc(channel, self.gain)
		time.sleep(.001)
		return data  # 2032 is 10V @ gain of 2

	def get_scaled(self,channel):
		data = 0;
		data = self.adc.read_adc(channel, self.gain)
		# Rratio	0.2032520325 (100/492)
		# Vmax		10V	
		# Vadc@MAX	2.0325203252	
		# Raw@MAX	0.992441565 x 2^11 = 2032.5203252033
		#
		# RafToVolts Scale		0.00492 
		data *= 4.92 / 1000
		time.sleep(.001)
		return data #(volts)
	
	def get_temp(self):
		tempC = self.max.readTemp()
		return tempC

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


# IO Mapper class, maps GPIO # to output numbers
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





#	def __init__(self, str):
#		print "KK" 
#		print str
#		return  
#
#PiIO_DO24_Mapper = PiIO_DO24_Mapper()


	
