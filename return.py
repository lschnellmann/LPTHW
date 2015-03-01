# script to try to learn more about the 'return' statement in functions
import time
def add(a,b):
		import time
		print "this function is adding two values %d and %d " % (x,y)
		time.sleep(.5)
		print "ADDING %d + %d" % ( a , b ) 
		return a + b
		
x = int(raw_input("enter a number "))
y = int(raw_input("enter another number "))

print "x is equal to %d" % (x);time.sleep(1)
print "y is equal to %d" % (y);time.sleep(1)

sum = add (x,y);time.sleep(1);print 'which is equal to %g ' %(sum)

def spreadcalc (ask,bid,btc,units):
	import time
	print """This will calculate the spread of a cryptocurrency and multiply it by the price of bitcoin and then return a result in US dollars"""
	time.sleep(1)
	print "calculating spread in USD %f - %f times %f times %d" % (ask,bid,btc,units)
	time.sleep(2)
	return (((ask - bid)*btc)*units) 

bid = float(raw_input("enter the bid "))
ask = float(raw_input("enter the ask "))
btc = float(raw_input("enter the current BTC price in USD ")) 
units = int(raw_input("enter the number of trading units "))

spread = spreadcalc (ask,bid,btc,units); print 'spread is equal to %f USD ' % (spread)


	
