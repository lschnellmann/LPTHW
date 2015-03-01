# Here's some new strange stuff, remember type it exactly.
# assigns the variables...
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\Apr\nMaynJun\nJul\nAug"

# prints the variables 
# why the 'n' in front of each month?
# ahhh.. it must mean print on new line.. lets take one out 
# and see what happens...

#sure enough.. take out the 'n' and it prints on the same line.
# so using the n tells python to print on a new line... 
# the '\' is a seperator,, if it is not followed by a 'n'.. it prints as a string
# take out the \ and see what happens..

# the backslash tells python that the 'n' is a line command


print "Here are the days: ", days
print "Here are the months: ", months 

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
