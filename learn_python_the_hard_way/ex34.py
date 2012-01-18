
#!/usr/local/bin/python
# -*- coding:utf-8 -*-
from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input("> ")
	
	# better use try catch for ValueError
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead( "Man, you learn to type a number!")
		
	if how_much < 50:
		print "You are not greedy. You Win!"
		exit(0)
	else:
		dead( "You greedy bastard!")
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move?"
	bear_move = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead( "The bear look at you and pimp slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can move now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead( "The bear gets pissed off and chew you crotch off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I have got no idea about it means."
			
def cthulu_room():
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for life or eat your head?"
	
	next = raw_input("> ")
	if "flee" in next:
		start()
	elif "head" in next:
	    dead("Well, that was tasty!")
	else:
		cthulu_room()
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your left and right."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()