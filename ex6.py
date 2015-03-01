#this assigns the variable 'x' to the number of subjects / 
#since it is 10 there is a modulus operator in front of the number
x = "there are %d types of people." % 10
# this assigns the variable 'binary' to the string 'binary'
binary = "binary"
# assigns 'do_not' to the word 'don't'
do_not = "don't"
# this assigns the variable 'y' to "binary and 'do_not', both of which are 
#used as variables later in the script. using the formating modulus $s since they are both strings.
y = "Those who know %s and those who %s. " % (binary, do_not)

#this prints the integer variable 'x'
print x
#this prints the string variable 'y'
print y

# prints the variable x using the formatting code %r which prints whatever x is no matter what
print "I said: %r." % x 
# prints the variable 'y' as a string
print "I also said: '%s'."% y

#assigns the variable hilarious "False" which is actally a programing response.
hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"
# prints the variable hilarious which is 'False' but uses only the modulus formatting symbol code.
print joke_evaluation % hilarious
# this is the how you combine a string to print on one line, I was 
# wondering about how you do that and it looks like if you say "print the added variables it works to print on one line".
w = "This is the left side of ..."
e = "a string with a right side,"

# lets try 'textwrap.wrap(text[, width[, ...]])
#wrap()[ 40[ ...]]
#print "when I was naught but a poor child growing up in the hills of siberia our family had a flock of chickens which provided meat and eggs."

print w + e 
