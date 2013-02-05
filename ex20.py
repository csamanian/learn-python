# imports module called argv to my script
from sys import argv

# defines the 2 arguments that are held by argv, prompts for filename
script, input_file = argv

# function created to print all contents of the inputted file
def print_all(f):
	print f.read()

# function created to go back to the first character in the file
# seek (offset) - move to a new file position
def rewind(f):
	f.seek(0)

# function created to print one line at a time
def print_a_line(line_count, f):
	print line_count, f.readline()

# defines the current_file as the file indicated in the argument (input_file)	
current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

# defines current_line to equal 1, this is also called line_count in function
current_line = 1
print_a_line(current_line, current_file)

# adding 1 to indicate that the next line is line 2
current_line += 1
print_a_line(current_line, current_file)

# adding 1 to indicate that the next line is line 3
current_line += 1
print_a_line(current_line, current_file)

# note that a += b is the same as a = a + b
