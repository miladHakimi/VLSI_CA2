from utility import *

class Module:
	def __init__(self, type, name, input_nodes, output_node):
		self.name = name
		self.type = type
		self.input_nodes = input_nodes
		self.output_node = output_node

		self.funcs = {
			"INV": self.INV,
			"OR" : self.OR,
			"AND": self.AND,
			"XOR": self.XOR,
			"XNOR": self.XNOR,
			"NAND": self.NANAD,
			"NOR": self.NOR
		}
	def INV(self):
		return 1-self.input_nodes[0].p

	def AND(self):
		p = 1
		for i in self.input_nodes:
			p*= i.p
		return p
	
	def NANAD(self):
		return 1-self.AND()	

	def OR(self):
		p = 1
		for i in self.input_nodes:
			p*= (1-i.p)
		return 1-p

	def NOR(self):
		return 1-self.OR()

	def XOR(self):
		pA = self.input_nodes[0].p 
		pB = self.input_nodes[1].p
		p = pA + pB - 2 * pA * pB		
		return p

	def XNOR(self):
		return 1-self.XOR()

	def calc(self):
		self.output_node.p = self.funcs[self.type]()