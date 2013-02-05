# this way is better if you are automatically pulling the filename from another source
# imports the module called argv (argument variable) to my script
from sys import argv

# defines the 2 arguments that are held by argv, prompts for filename
script, filename = argv

# defines the file that is opened as a variable called txt
txt = open(filename)

# displays the filename that was passed as one of the arguments
print "Here's your file %r:" % filename

# displays the actual contents of the file that was passed through
# .read is actually a command / function / method 
print txt.read()



# this way is better if you want the user to be prompted to input the filename
# asks the user to input the file name again, and assigns it to variable called file_again
print "Type the filename again:"
file_again = raw_input("> ")

# defines the file that is opened as a variable called txt_again
txt_again = open(file_again)

# displays the actual contents of the file that was passed through
print txt_again.read()
