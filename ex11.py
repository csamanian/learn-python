
# raw_input prompts the user to input and converts the input into a string
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "Where do you work?"
employer = raw_input()
print "Where do you live?"
home = raw_input()
print "Where did you go to school?"
school = raw_input()

print "Ok, so you work at %r, you live in %r, and you went to school at %r." % (employer, home, school)