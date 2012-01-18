
#!/usr/local/bin/python
# -*- coding:utf-8 -*-
from sys import exit
from random import randint
import ex43_room

class Engine(object):
	def __init__(self, start):
		self.quips = ["You died. You kinda suck at this.",
				"Your mom would be proud. If she were smater.",
				"Such a loser."
				"I have a small puppu that's better at this."]
		self.rooms = [ex43_room.PrincessRoom(),
					ex43_room.GoldKoiRoom(),
					ex43_room.BigIronGate(),
					ex43_room.BearWithSword()]
		self.map = {'death':self.death,
					'princess_lives_here':self.rooms[0].run,
					'gold_koi_pond':self.rooms[1].run,
					'big_iron_gate':self.rooms[2].run,
					'bear_with_sword':self.rooms[3].run}
		self.start = start
	
	def death(self):
		print self.quips[randint(0,len(self.quips)-1)] 
		#exit(0)
		
	def run(self):
		next = self.start
		while next:
			room = self.map[next]
			print "\n--------------"
			next = room()
			
game_engine = Engine('princess_lives_here')
game_engine.run()