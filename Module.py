from utility import *

class Module:
	def __init__(self, type, name, input_nodes, output_node):

		self.name = name
		self.type = type
		self.input_nodes = input_nodes
		self.output_node = output_node

		self.funcs = {
			"OR" : self.OR,
			"AND": self.AND,
			"XOR": self.XOR
		}

	def AND(self):
		p = 1
		for i in self.input_nodes:
			p*= i.p
		return p*(1-p)
	
	def OR(self):
		p = 1
		for i in self.input_nodes:
			p*= (1-i.p)
		return p*(1-p)

	def XOR(self):
		pA = self.input_nodes[0].p 
		pB = self.input_nodes[1].p
		p = pA + pB - 2 * Pa * pB		
		return p*(1-p)

	def calc():
		output_node.p = self.funcs[self.type]()			