# Close -- Closes the file.  Like File->Save..  in  your editor
# read -- Reads the contents of the file. You can assign the result to a variable
# readline -- Reads just one line of a text file
# truncate -- Empties the file
# write('stuff') -- Writes "stuff" to the file.

from sys import argv
# argv is a list containing the name of the script and the filename
script, filename = argv
# in this case the file name is text.txt
print "We're going to erase %r." % filename
# sloppy way to end the python script
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# anything will work, even just a 'RETURN'
raw_input("?")

print "Opening the file..."
# assigns the variable 'target' the file name and the 'w' is to WRITE to the file
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
# erases the entire file
target.truncate()

print "Now I'm going to ask you for three lines."
#assigns variables to input from raw_input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# 'target' is the file name, and the .WRITE command writes the 
# variable into the text file.
# the 'target.write("\n") tells the script to write on a NEW line.
# there is probably a more efficient way of doing this.
# maybe look up something like a 'wrap' command? 
#Use strings, formats, and escapes to print out line1, line2,
# and line3 with just one target.write() command instead of six.

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.write("{0}\n{1}\n{2}\n".format(line1,line2,line3))
target.write("{0}\n{1}\n{2}\n".format(line1,line2,line3))



# open and print the txt file. in read only mode (the 'r').. note the comma
target = open('test.txt', 'r')
print file.read(target)


print "And finally, we close it."
# says 'filename'... CLOSE it.  maybe a 's' overwrites and saves it?
target.close()


