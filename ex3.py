# line 2 prints a string
print "I will now count my chickens:"
#line 4 adds 25 + 30 then divides by 6 -- it divides before it adds
print "Hens", 25 + 30 / 6
# line 6 -- what does the percent (%) sign do? % returns the remainder of two numbers.. what is the order of operations?
# PEMDAS is parenthesis exponents, multiplication, division, addition, subtraction
# first the line multiplies 25 times 3 and gets 75
# then it 'mods' 75 (%) by 4 and gets 3. (75 divided by 4 is 18.75, and the mod
# truncates it (2.75 turns into 3), which ends up with 100 - 3 which equals 97.
# then it subracts 3 from 100 to get an answer of '97'
# because if you put 4 into 18.75 it only goes 4 times with 2.75 leftover!.. i.e.
# 3!
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

#this line first does 1 divided by 4 and gets .25, then it 
# 'mods' (%) 4 and 2 and gets 0 then it adds 3 plus 2 plus 1 plus 0 (the mod) 
# result is 1 plus 6 for an answer of 7

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

print "Is it true that 3.0 + 2.0 < 5.0 - 7.0?"
# this is false because 3 + 2 is 5 which is more than 5 - 7 which is negative 2


print 3.0 + 2.0 < 5.0 - 7.0
# this is simple 3 plus 2 is 5, so the line prints 5 after doing PEMDAS

print "What is 3 + 2?", 3.0 + 2.0

# This line is also simple, 5 minus 7 equals negative 2 in accordance with PEMDAS

print "What is 5 - 7?", 5.0-7.0


#  Just a print statement
print "Oh, that's why it's False."

print "How about some more."
# 5 is greater than - 2 so it is TRUE

print "Is it greater?", 5.0 > -2.0
# 5 is greater or equal to -2 so this is TRUE
print "Is it greater or equal?", 5.0 >= -2.0 
# this is NOT TRUE, SO it is FALSE
print "Is it less or equal?", 5.0 <= -2.0 
#below is scratch pad to figure out these seemingly simple operations.
print 3.0 % 2.0 
print 100.0 - 25.0 * 3.0 % 4.0
print 3.0 % 4.0



