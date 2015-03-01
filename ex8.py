formatter = "%r %r %r %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# if I put '* 4' at the end it prints the formatter 4 times for a total
# of 16 times... I suppose this could be a random number as well.
print formatter % (formatter, formatter, formatter, formatter) * 4
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", 
	"So I said goodnight."
)

#Notice the last line of output uses both sing-quotes and double-quotes
#Why do you think this is?

# because the commas output it on the same line.


