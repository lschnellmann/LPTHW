from sys import argv;from os.path import exists;import time;script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
print "_";time.sleep(0.5);print "_";time.sleep(0.5);print "_";time.sleep(0.5);print "_";time.sleep(0.5);
print "_";time.sleep(0.5);print "_";time.sleep(0.5);print "_";time.sleep(0.5);print "_";time.sleep(0.5);
in_file = open(from_file) ; indata = in_file.read();print "The input file is %d bytes long" % len(indata)
if len(indata) <1:
	print "file does not exist"
if len(indata) >1:
	print "File DOES exist" ; print " "
print "Does the output file exist? %r" % len(indata) ; print "Ready, hit RETURN to continue, CTRL-C to abort."
print "******************** ";raw_input()
out_file = open(to_file, 'w') ; out_file.write(indata)
print "Alright, all done.";print "\n";print "Current date and time " + time.strftime("%c")
print "\n" ; print "\n";target = open('test.txt', 'r') ; print "THE SEVEN CARDINAL SINS";print file.read(target)
out_file.close();in_file.close()
