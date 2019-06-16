## PiIO concurrency

Concurrency is used in some of the examples in order to make programming easier.  
Without a framework for cuncurrency performing multiple control tasks can become difficult as no part of the code cn be allowed to block.  
For example if we want to flash one LED and 1Hz and another at 100Hz we'd have to write something like this:  

'''
sleep(10ms)
count++
ToggleLED(1)
if(count % 100) == 0
	ToggleLED(2)
'''

This can get quite complex once we start doing more complex tasks and once we start using more complex APIs that may block for several seconds on some calls it becomes unmanageable.  
There are three ways of dealing with this:  

1. Some kind of state machine that requires co-operative handover of control as per the above example.
2. Running tasks as threads within a single program
3. Running multiple independant programs that may communicate with each other using a messaging framework such as zeromq.

In the examples we use method (2) using the concuffent futures python framework.  
With this aooroach we can have python processes that run concurrently within the same program in something called a thread.  
Going back to the original example the code would then look like:  

'''
def Thread1:
	sleep(10ms)
	ToggleLED(1)

def Thread2:
	sleep(1s)
	ToggleLED(2)

RunAsThread(Thread1)
RunAsThread(Thread2)
'''

Which for a simple example may look more complex but for real world problems is much easier to code once the threading code has been handled.  
The following code examples use the concurrency framework:  

* hydro_ADIO.py
* concurrency_DO.py

Communications can can be implemented between threads using global variables but it must be remembered that the contents can be changed in unpredictable ways by other threads therefore it's a good idea to have some kind of setup whereby one thread writes to a variable and others read from it and the actions of the reader are atomic.

