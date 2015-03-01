# Exercise 15: Reading Files

# You know how to get input from a user with raw_input or argv, Now you will learn about
# reading from a file.  You may have to play with this exercise the most to understand what's 
# going on, so do the exercise carefully and remember your checks.  Working with
# files is an easy way to erase your work if you are not careful.

# This exercise involves writing two files.  One is usual usual ex15.py file that you will run, 
# but the other is named ex15.sample.txt.  This second file isn't a script but a plain text 
# file we'll be reading in our script.  Here are teh contents of that file:
#____________________________________
#this  line imports the module 'argv' which stores arguements for unpacking
# at a later time
from sys import argv
# this line 'unpacks' arguements from argv (or does it assign arguments?)
script, filename = argv
# this line opens the file that was specified in the command line (it is 
#  'hardcoded". -- which is bad practice in most cases depending on what 
#  you want to do.
txt = open(filename) 
# this line tells you the filename that is to be read by usign the formatter
# %r  .. (could it be %s?)

print "Here's your file %s :" % filename
# txt.read instructs TXT to 'READ' the text in the file,  and then print it.
print txt.read()
#prompts the user to type the file name again, could be changed to 
# file_again = raw_input("type the file name again >")
print "Type the filename again:"
file_again = raw_input("> ")
#opens the file again from the user prompt, instead of being hardcoded 
txt_again = open(file_again)
#prints out the file
print txt_again.read()

answer = raw_input("do you want to close \%r ")
if answer == "yes":
	txt_again.close()
	print "file is closed"
	quit()
	
print "file is NOT closed"
	

	


	

		
		
