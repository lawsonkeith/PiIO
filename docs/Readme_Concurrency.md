
## PiIO concurrency

Concurrency is used in some of the examples in order to make programming easier.  
Without a framework for cuncurrency performing multiple control tasks can become difficult as no part of the code can be allowed to block.  
For example if we want to flash one LED and 1Hz and another at 100Hz we'd have to write something like this:  

```python
sleep(.01)
count+=1
ToggleLED(1)
if ((count % 100) == 0):
	ToggleLED(2)
```

This can get quite complex once we start doing more complex tasks and once we start using more complex APIs that may block for several seconds on some calls it becomes unmanageable.  For example:

```python
while True:
	#get user input
	freq = input()

	sleep(freq)
	ToggleLED(1)
```

The above program get stuck at the input() call and can't actully toggle the LED at the user specified frequency.
There are three ways of dealing with this:  

1. Some kind of state machine that requires co-operative handover of control as per the above example, function calls need to be re-written to be non blocking.
2. Running tasks as separate execution threads within a single program
3. Running multiple independant programs that may communicate with each other using a messaging framework such as zeromq

In the examples we use method (2) using the concurrent futures python framework in reality the first method isn't allways possible and often requires more complex coding and option (3) works well for larger problems.  More information on this can be found at:

https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures

With this approach we can have python processes that run concurrently within the same program as separate execution threads.    
Going back to the original example the code would then look like:  

![](https://github.com/lawsonkeith/PiIO/raw/master/images/thread_pic.PNG)

```python
def Thread1:
	while True:
		sleep(.01)
		ToggleLED(1)

def Thread2:
	while True:
		sleep(1)
		ToggleLED(2)

RunAsThread(Thread1)
RunAsThread(Thread2)
```

and...


```python
freq = 1

def Thread1:
	global freq
	while True:
		#get user input
		freq = input()

def Thread2:
	global freq
	while True:
		sleep(freq)
		ToggleLED(1)


RunAsThread(Thread1)
RunAsThread(Thread2)
```


Which for a simple example may look more complex but for real world problems is much easier to code once the threading code has been handled.  
The following code examples use the concurrency framework:  

* hydro_ADIO.py
* concurrency_DO.py

Communications can can be implemented between threads using global variables but it must be remembered that the contents can be changed in unpredictable ways by other threads therefore it's a good idea to have some kind of setup whereby one thread writes to a variable and others read from it and the actions of the reader are atomic.

```python
count=0

def Thread1:
	global count
	if count > 5:
		sleep(.01)
		ToggleLED(1)

def Thread2:
	global count
	count+=1
	sleep(1)
	ToggleLED(2)

RunAsThread(Thread1)
RunAsThread(Thread2)
```
