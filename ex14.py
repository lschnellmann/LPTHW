# Let's do  one exercise that uses argv and raw_input together to askthe user something specific.
# You will  need  this for the next exercise where we learn to read and write files.  In  this 
# exercise we'll use raw_input slightly differently by having it print a simple > prompt.
# This i s similar to a game like Zork or Adventure.

from  sys import argv

script, user_name, computer = argv
prompt = '--:) _/0\_ '

print "Hi %s, I'm the %s  script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "why are  you trying to learn %s ?" % computer 
reason = raw_input(prompt) 


print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Awright, so you  said %s about liking me.
You are learning python because %s 
You live in %s.  Not sure where that is.
And you have a %s computer.  Nice.
""" % (likes, reason, lives, computer)
