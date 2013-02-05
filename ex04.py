#number of cars
cars = 100

#number of spaces in a car
space_in_a_car = 4.0

#number of drivers
drivers = 30

#number of passengers
passengers = 90

#number of cars that do not have drivers
cars_not_driven = cars - drivers

#number of cars being driven
cars_driven = drivers

#number of total spaces available
carpool_capacity = cars_driven * space_in_a_car

#average number of people riding per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#Extra Credit
#1. 4.0 is used instead of the 4 because that will ensure the calculation is floating point.
#2. Floating point number is
#3. Complete
#4. = is used to initialize variables
#5. _ is an underscore character used instead of spaces in a string of text