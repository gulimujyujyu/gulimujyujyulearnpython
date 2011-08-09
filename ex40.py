
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#part 1
things = ['a', 'b', 'c', 'd']
print things[1]

things[1] = 'z'
print things[1]

print things

#part 2
stuff = {'name': "Zed", 'age':36, 'height': 6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = "San Francisco"
print stuff['city']
stuff[1] = "wow"
stuff[2] = "Neato"
print stuff[1]
print stuff[2]

print stuff

del stuff[1]
del stuff[2]

print stuff

#part 3
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL':'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap: #find keys
		return themap[state]
	else:
		return "Not found"

cities['_find'] = find_city

while True:
	print "State? (ENTER to quit)", #this will not break the line
	state = raw_input("> ")
	
	if not state: break
	
	city_found = cities['_find'](cities, state)
	print city_found