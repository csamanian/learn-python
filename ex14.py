from sys import argv

script, user_name, age = argv
prompt = 'Enter your answer here: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % (user_name)
likes = raw_input(prompt)

print "Where do you live %s?" % (user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Do you enjoy being %s years old?" % (age)
age_enjoy = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You answered %r when asked if you enjoy being your age.
And you have a %r computer. Nice.
""" % (likes, lives, age_enjoy, computer)