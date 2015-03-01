print "how old are you?",
age = raw_input()
print "how tall are you?", 
height = raw_input()
print "How much do you weigh?", 
weight = raw_input()

print "So, you're %r years old, %s tall and %r heavy." % (
	age, height, weight)
	
print "what is the temperature outside?",
fahrenheit = int(raw_input("enter temp in F:"))
#convert to celsius 
Celsius = (fahrenheit - 32) * 5.0/9.0
# round(number[, ndigits])
print "Temperature:", fahrenheit, "Fahrenheit = ", round(Celsius, 2), " C"
