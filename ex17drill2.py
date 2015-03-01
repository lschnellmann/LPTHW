import time

for y in range (0, 10):
	print "Current date and time " + time.strftime("%c")
	time.sleep(1)
	print " "
	f = open('test.txt')
	i = 10
 
	for x in range(0, 7):
		line = f.readline(i)
		time.sleep(0.5)
		print "Deadly Sin: %s " % (line)
	
f.close()

			
