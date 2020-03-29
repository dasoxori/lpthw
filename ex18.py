# this on is like your script with argv

def printTwo(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this

def printTwoAgain(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just take one argument

def printOne(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments

def printNome():
    print "I got nothing"

printTwo("Zed", "Shaw")
printTwoAgain ("Zed", "Shaw")
printOne ("First")
printNome()