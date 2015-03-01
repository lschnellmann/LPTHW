#exercise 28 LPTHW
#easier than typing them individually into the command line
#UPDATE: NOW IT'S TURNING INTO A QUIZ 2/24/2015
def clear(num):
    for i in range(num): print 
	
#question number
q = 0;u = 1;e = 1 
	
line =  """___________________________________________________________\n"""
n = 0
from random import randint
import time;import sys 
print " \n :"
print "ANSWER EACH LOGIC QUESTION.";print " \n "
#1
print 'Question %i' % (q+1) ; q = (q+1) 
print "NOT.....|.....TRUE?"
answer = str(raw_input(" 1 ) Not False is :"))
r = randint(2,5)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "


if answer == str("true"):
	print "CORRECT, answer is TRUE";print " \n "; n = (n + 1);print n,;print "correct"
	
else:
	print "WRONG, answer is ---> ",
	x = (not False)
	print x;print line;print " \n \n "
	


C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)

#2
print'Question %i' % (q+1); q = q + 1 
print "NOT.....|.....TRUE?"
answer = str(raw_input(" 2 ) Not True is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
if answer == str("false"):
	print "CORRECT, answer is False";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (not True)
	print x;print line;print " \n \n "
	

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#3	

print 'Question %i' % (q+1);q = q + 1 
print "   OR.....|.....TRUE?"

answer = str(raw_input(" 3 ) True or False is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "

if answer == str("true"):
	print "CORRECT, answer is True";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (True or False)
	print x;print line;print " \n \n "

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):	
	clear(80)
#4	
print 'Question %i' % (q+1);q = q + 1 
print "   OR.....|.....TRUE?"
answer = str(raw_input(" 3 ) True or True is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("true"):
	print "CORRECT, answer is True";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (True or True)
	print x;print line;print " \n \n "

print "\n \n"

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#5
print 'Question %i' % (q+1);q = q + 1 
print "   OR.....|.....TRUE?"
answer = str(raw_input(" 3 ) False or True is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("true"):
	print "CORRECT, answer is True";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (False or True)
	print x;print line;print " \n \n "

print "\n \n"

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#6
print 'Question %i' % (q+1);q = q + 1 
print "   OR.....|.....TRUE?"
answer = str(raw_input(" 3 ) False or False is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("false"):
	print "CORRECT, answer is False";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (False or False)
	print x;print line;print " \n \n "

print "\n \n"

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#7
print 'Question %i' % (q+1);q = q + 1 
print "   AND.....|.....TRUE?"
answer = str(raw_input(" 3 ) True and False is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("false"):
	print "CORRECT, answer is False";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (True and False)
	print x;print line;print " \n \n "

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):	
	clear(80)
#8	
print 'Question %i' % (q+1);q = q + 1 
print "   AND.....|.....TRUE?"
answer = str(raw_input(" 3 ) True and True is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("true"):
	print "CORRECT, answer is True";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (True and True)
	print x;print line;print " \n \n "

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):	
	clear(80)
#9	
print 'Question %i' % (q+1);q = q + 1 
print "   AND.....|.....TRUE?"
answer = str(raw_input(" 3 ) False and True is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("false"):
	print "CORRECT, answer is false";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (False and True)
	print x;print line;print " \n \n "
	
C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)	
#10	
print 'Question %i' % (q+1);q = q + 1 
print "   OR.....|.....TRUE?"
answer = str(raw_input(" 10 ) False And False is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("false"):
	print "CORRECT, answer is False";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (False and False)
	print x;print line;print " \n \n "

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#11	
print 'Question %i' % (q+1);q = q + 1 
print "   NOT OR.....|.....TRUE?"
answer = str(raw_input(" 3 ) Not (True or False) is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("false"):
	print "CORRECT, answer is False";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (not (True or False))
	print x;print line;print " \n \n "

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):	
	clear(80)
#12	
print 'Question %i' % (q+1);q = q + 1 
print "   NOT OR.....|.....TRUE?"
answer = str(raw_input(" 3 ) not(true or true) is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("false"):
	print "CORRECT, answer is False";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (not (True or True))
	print x;print line;print " \n \n "

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#13	
print 'Question %i' % (q+1);q = q + 1 
print "   NOT OR.....|.....TRUE?"
answer = str(raw_input(" 3 ) not(False or True) is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("false"):
	print "CORRECT, answer is False";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (not(False or True))
	print x;print line;print " \n \n "
	
C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#14
print 'Question %i' % (q+1);q = q + 1 
print "   OR.....|.....TRUE?"
answer = str(raw_input(" 3 ) not (False or False) is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("true"):
	print "CORRECT, answer is True";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (not(False or False))
	print x;print line;print " \n \n "

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
	
#15	
print 'Question %i' % (q+1);q = q + 1 
print "   NOT AND.....|.....TRUE?"
answer = str(raw_input(" 3 ) Not (True and false) is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("true"):
	print "CORRECT, answer is true";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = not (True and False)
	print x;print line;print " \n \n "

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#16	
print 'Question %i' % (q+1);q = q + 1 
print "   NOT AND.....|.....TRUE?"
answer = str(raw_input(" 3 ) not(True and True) is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("false"):
	print "CORRECT, answer is False";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (not(True and True))
	print x;print line;print " \n \n "

C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#17	
print 'Question %i' % (q+1);q = q + 1 
print "   NOT AND .....|.....TRUE?"
answer = str(raw_input(" 3 ) not(False and True) is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("true"):
	print "CORRECT, answer is true";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (not(False and True))
	print x;print line;print " \n \n "
	
C = str(raw_input("TYPE C TO CLEAR SCREEN OR ENTER FOR NEXT QUESTION"))
if C == str("C"):
	clear(80)
#18	
print 'Question %i' % (q+1);q = q + 1 
print "   NOT AND .....|.....TRUE?"
answer = str(raw_input(" 3 ) not(False and False) is :"))
r = randint(2,3)
for i in range (1,r):
	time.sleep(1)
	print "\r %i" % (i), ; sys.stdout.flush() 
	
print "\n \n "
if answer == str("true"):
	print "CORRECT, answer is true";print " \n "
else:
	print "WRONG, answer is ---> ",
	x = (not(False and False))
	print x;print line;print " \n \n "
	

	
	
	
