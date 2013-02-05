from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# hitting return enables the code to continue running
# defining "target" as the name of the file we are opening
# using 'w' to indicate that we're opening the file in write mode
print "Opening the file..."
target = open(filename,'w')

# truncate empties the file completely
# this is redundant to have in write mode because editing the file will overwrite it anyways
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# prompts the user to input content for the three lines of text
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# writes the content to the file
print "I'm going to write these to the file."
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# closes the file
print "And finally, we close it."
target.close()
