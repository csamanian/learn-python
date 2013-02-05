# importing two commands: argv and exists (returns true if file exists, false if not)
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# copying data from from_file to to_file
open(to_file,'w').write(open(from_file).read())

print "Copy complete."