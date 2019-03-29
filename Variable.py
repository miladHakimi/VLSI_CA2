from __future__ import division

class Variable:
	def __init__(self, line, module):
		line = line.split(' ')

		self.var_type 	= line[1]
		self.size 		= line[2]
		self.mapped_name = line[3]
		self.name 		= line[4]
		self.index  		= ""

		if len(line) == 7:
			self.index = line[5]

		self.module = module
		
		self.values = {
			"0" : 0,
			"1" : 0
		}

	def update(self, val):
		self.values[val] += 1

	def __str__(self):

		ind = " : "
		pz = 0

		if self.index is not "":
			ind = self.index + " : "
		
		if (self.values["0"] + self.values["1"]) > 0:
			pz = self.values["0"]/(self.values["0"] + self.values["1"])
			
		return self.module + " -> " + self.name + ind + str(pz * ( 1 - pz ))