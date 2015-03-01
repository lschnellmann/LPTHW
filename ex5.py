name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 # inches
weight = 180 # Lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

repeat = int(raw_input("how many times do you want this to print?" ))

for x in range (0, repeat):

	print x 
	

	
	print "Let's talk about %s." % name
	print "Zed's age is %d." % age
	print "He's %d inches tall." % height
	print "He's %d pounds heavy." % weight
	print "Actually that's not too heavy."
	print "He's got %s eyes and %s hair." % (eyes, hair)
	print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
	print "If I add %d, %d, and %d I get %d." %(
		age, height, weight, age + height + weight)

	#do the same thing using the metric system using formulae to convert.
	print "___________________________"
	print "on a metric basis, %s, is " % name
	print "He's %g centimeters tall." % (height * 2.54)
	print "He's %r kilograms heavy." % (weight / 2.2046)
	print "Zed is a fat ass for making me type all this over and over, but it works"
	print "very well as a learning technique." 
