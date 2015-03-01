# number of cars total

cars = 100
# number of people who can fit in each car
space_in_a_car = 4
#available drivers

drivers = 30
# available passengers
passengers = 90
# cars idle.. since there are 100 cars, and only 30 drivers, 70 idle cars 
cars_not_driven = cars - drivers
# it follows that with 30 drivers only 30 cars will be driven
cars_driven = drivers
# total number of people that can be transported (including drivers)

carpool_capacity = cars_driven * space_in_a_car
#some more.. some less.. may be a floating point number of passengers per car driven

average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Traceback (most recent call last): an exception error most recent call in file ex4.py, in line 8 
# in the module (program).. 'car_pool_capacity' was not defined with a variable values
#study drills if you use just 4 instead of 4.0 then it turns into integers instead of 
# floating point numbers.

#I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
#Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
#Write comments above each of the variable assignments.
#Make sure you know what = is called (equals) and that it's making names for things.
#Remember that _ is an underscore character.
#Try running python from the Terminal as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.
