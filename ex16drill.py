#Write a script similar to the last exercise that uses READ 
#and ARGV to read the file you just created

# first thing is to import the ARGV module

from sys import argv 

script, filename = argv

target = open(filename)

print file.read(target)

target.close()
