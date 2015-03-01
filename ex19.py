
def f_1(helpme):
	print "You need %s finding a place to live" % helpme

f_1() 









def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheeses!" % cheese_count
	print "you have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
def name_info():
	import time
	n = raw_input ("Enter your name: ") 
	time.sleep(1)
	print "**************************************"
	time.sleep(0.5)
	print  n
	
def timer():
	import time
	t = int(raw_input ("Enter minutes to alarm time: "))
	x = (t*60)
	for y in range ( 0 , x):	
		print y,
		time.sleep(.251)
	for z in range (0,10):
		print "\a,",
		
#timer ()
	
#name_info ()

	
# line 8 prints 'give the f numbers directly, THEN calls the function.	
#print "We can just give the function numbers directly:"
#cheese_and_crackers(20, 30)
	
# line 13,14,15 -- 
# and line 18 calls (runs) the function
# uses the two variables by assigning values to them.  
	
#print "OR, we can use variables from our script:"
#amount_of_cheese = 10 
#amount_of_crackers = 50
# line 18 calls the function (or uses the function) with the variables assigned
# in lines 14 and 15.
#cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#line 21 changes the amounts by doing math after the calling the function, 
# thus changing the amounts.. and runs the function again.
#print "We can even do math inside too:"
#cheese_and_crackers(10 + 20, 5 + 6)

#line 26 combines variables and math and then runs the function.
#print "And we can combine the two , variables and math:\n \a"
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

	
