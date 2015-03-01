
def xtrueorfalse():
	import time
	for y in range (1,7,2):
	
		for x in range (1,20):
			if (x > 10): 
				print "x is true %d '   main loop is ' %d " % (x,y) 
				time.sleep(1.5025 / x)
			if (x < 10):
				print "x is false %d " % (x)
				time.sleep(	.5025 / x)
	

def binary_joke():
	import time
	z = int(raw_input("how many types of people in this world? "))
	for i in range(0, z, 1):
		x = "there are %d types of people." % (z)
		binary = "binary"
		do_not = "don't"
		y = "Those who know %s and those who %s." % (binary, do_not) 

		print x;print y;time.sleep(.1);print " " 
		print "we're on loop number %d" % (i);print " "
		print ' %d ' % (i)
binary_joke()
xtrueorfalse()


