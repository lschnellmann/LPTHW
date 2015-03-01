
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually poiontless, we can just do this;
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
	print "Learning about functions."
	
def time():
	import time
	for y in range (0, 10):
		print "Current date and time " + time.strftime("%c")
		time.sleep(.0375)
		print "__________________________________ "
		f = open('test.txt')
		i = 10
 
	for x in range(0, 7):
		line = f.readline(i)
		time.sleep(0.5)
		print "Deadly Sin: %s " % (line)
	
	f.close()
	
	
print_none()
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
time()

