﻿
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
ten_things = "Apples oranges crows telephone light sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff =  ten_things.split(" ")
more_stuff = ["Day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some thinks with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
print " \t".join(stuff[:2:])
print " \t".join(stuff[1:8:2]) #first:end:step, unlike matlab