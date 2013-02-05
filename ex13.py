from sys import argv

script, first, second, third = argv

print "This fruit program is called:", script
print "Fruit 1: ", first
print "Fruit 2: ", second
print "Fruit 3: ", third

favorite = raw_input ("Which is your favorite fruit? ")

print "Ok, so your favorite is %s." % favorite