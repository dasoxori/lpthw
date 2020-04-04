tenThings = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = tenThings.split(' ') # return a list of strings by breaking the given string by the specified separator
moreStuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    nextOne = moreStuff.pop() # is an inbuilt function thar removes and returns last value from the list
    print "Adding: ", nextOne
    stuff.append(nextOne)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #returns the last from the list
print stuff.pop()
print ' '.join(stuff) # returns a string concatenated with the separator before the dot.
print '#'.join(stuff[3:5]) # returns a string concatenated with the separator before the dot from the specific range.
