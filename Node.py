from __future__ import division

class Node:
	def __init__(self, name):
		self.name = name
		self.p = 0
		self.value = -1

	def get_activity():
		return self.p*(1-self.p)
	
	def __str__(self):
		return self.name + '{\n' + '	P(n=1) = ' + str(self.p) + '\n	P(n=0) = ' + str(1-self.p) + '\n	P(0->1) = ' + str(self.p*(1-self.p)) + '\n}'