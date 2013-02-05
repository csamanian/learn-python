# %d is used as a variable name for the number 10; since it is a number value and not a string, quotes are not used.
x = "There are %d types of people." % 10

# define the variable name binary to equal the string value called "binary"
binary = "binary"

# define the variable name do_not to equal the string value called "don't"
do_not = "don't"

# %s is used as a placeholder for two string variables with values initialized above
# string within a string - two times
y = "Those who know %s and those who %s." % (binary, do_not)

# display the string values of x and y
print x
print y

# display the string value below and use the variable named x; show the quotes because we're using the %r formatted variable
# string within a string
print "I said: %r." % x

# display the string value below and use the variable named y; show the string because we're using the %s formatted variable
# quotes are also shown because they are part of the print string 
# string within a string
print "I also said: '%s'." % y

# define the variable called hilarious to equal False value
hilarious = False

# define the variable called joke_evaluation to equal a string with the %r formatted variable
joke_evaluation = "Isn't that joke so funny?! %r"

# print the value set by the variable joke_evaluation and replace %r with the value defined for hilarious variable
print joke_evaluation % hilarious

# define w and e variables
w = "This is the left side of..."
e = "a string with a right side."

# display the separate string values of w and e as one longer connected string (adds them together)
# string within a string
print w + e


