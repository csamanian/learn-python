def add (a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract (a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply (a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide (a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
	
	
print "Let's do some math with just functions!"

age = add(25, 5)
height = subtract (78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it anyways.
print "Here is a puzzle."

# original version
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))	
what = age + (height - (weight * (iq/2)))

print "That becomes: ", what, "Can you do it by hand?"

# extra credit - write my own simple formula
# what_2 = fish * eggs - weight / apples
fish = add(10, 2)
eggs = subtract (20, 0)
weight = multiply (100, 2)
apples = divide (40,2)

what_2 = multiply(fish, subtract(eggs, (divide (weight, apples))))

print "That becomes: ", what_2, "Can you do it by hand?"


