tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "I am %r." % 29

# escape double-quote inside string
# need to do this or else the second " would be mistaken for the end of the string
print "I am %s tall." % "6'2\""

# escape single-quote inside string
# need to do this or else the second ' would be mistaken for the end of the string
print 'I am 6\'2" tall.'