# create a mapping of state to abbreviation
states = {
    'Oregon':'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities ={
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviations is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every steate abbreviation
print '-' * 10
for firstPart, secondPart in states.items():
    print "%s is abbreviated %s" % (firstPart, secondPart)

# print every city in state
print '-' * 10
for firstPart, secondPart in cities.items():
    print "%s has the city %s" % (firstPart, secondPart)

# now do both at the same time
print '-' * 10
for firstPart, secondPart in states.items():
    print "%s state is abbreviated %s and has city %s" % (firstPart, secondPart, cities[secondPart])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)
if not state:
    print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city






