
def tt():
	import time
	x = 1
	time.sleep(x)
	return x 
	

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b 
	
def multiply (a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
tt()
print "Let's do some math with just functions!"
tt()
x = int(raw_input("enter a number" ))
tt()
y = int(raw_input("enter another number" ))
tt()	
age = add(x, y)
tt()
height = subtract(x, y)
tt()
weight = multiply(x, y)
tt()
iq = divide(x, y)
tt()
tt()
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
tt
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
tt
print "That becomes: ", what, "Can you do it by hand?"

	
