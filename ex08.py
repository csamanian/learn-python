# defines variable as a string of 4 formatted variables
formatter = "%r %r %r %r"

# print formatter and substitute variables for %r
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

# print formatter and substitute variables for %r
# double quotes are displayed in the third string because %r prints exactly as inputted 
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
