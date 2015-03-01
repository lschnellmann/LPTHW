from sys import argv
import time 

#tells python to unpack an input file which is a script using 'argv'
script, input_file = argv
# defines the print_all function which prints 'f' (the file),
#and tells it to read 
def print_all(f):
	print f.read()
	#defins the rewind function and seeks (rewinds) to byte 0
	#which is the beginning of the file.
def rewind(f):
	f.seek(0)
	#defines the print_a_line function which uses the line_count
	#to read a particular line.
def print_a_line(line_count, f):
	print line_count, f.readline(),
		#asigns the variable current_file to whatever the open input file is.
current_file = open(input_file)
	#prints the entire text.txt file (which was unpacked with argv command.	
print "First let's print the whole file:\n"
	#calls the funchtion 'print_all' which in our case is text.txt	
print_all(current_file);time.sleep(1)
	#prints a line	
print "Now let's rewind, kind of like a tape."
	#uses the defined function 'rewind' to seek back to byte 0	
rewind(current_file);time.sleep(1)
	#prints out a message to the user	
print "Let's print three lines:";time.sleep(1)
	#assigns the variable current_line to 1
current_line = 1
	#prints line 1 from the current file which is test.txt
print_a_line(current_line, current_file),
	#prints line 2 because it incremented the variable current_line
current_line += 1
print_a_line(current_line, current_file),
	#prints line 3 because of an additional increment
current_line += 1
print_a_line(current_line, current_file),

# study drill 2: current_line becomes line_count because it is
#like a tape drive and the read head stays put unless its commanded
#to go elsewhere.  

