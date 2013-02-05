from sys import argv

script, filename = argv

# open the file
txt = open(filename)


# read the file
print txt.read()

# close the file
txt.close()
