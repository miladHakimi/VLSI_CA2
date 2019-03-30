from utility import *

class Module:
	def __init__(self, type, name, input_nodes, output_node):
		
		self.name = name
		self.type = type
		self.input_nodes = input_nodes
		self.output_node = output_node
		self.leakage = 0

		self.funcs = {
			"INV": self.INV,
			"OR" : self.OR,
			"AND": self.AND,
			"XOR": self.XOR,
			"XNOR": self.XNOR,
			"NAND": self.NANAD,
			"NOR": self.NOR
		}

		self.leakage_funcs = {
			"NAND": self.leakage_nand,
			"INV": self.leakage_inv,
			"NOR": self.leakage_nor
		}

		self.done = False

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

	def leakage_nand(self):
		if int(self.input_nodes[0].value) ^ int(self.input_nodes[1].value) == 1:
			data = "01"
		else:
			data = self.input_nodes[0].value*2

		nanadMap = {
			"00": 11,
			"01": 38,
			"11": 58
		}
		return nanadMap[data], str(int(not (self.input_nodes[0].value and self.input_nodes[1].value)))
	def leakage_inv(self):
		data = self.input_nodes[0].value
		invMap = {
			"0": 19,
			"1": 18
		}

		return invMap[data], str(int(not self.input_nodes[0].value))
	def leakage_nor(self):
		if int(self.input_nodes[0].value) ^ int(self.input_nodes[1].value) == 1:
			data = "01"
		else:
			data = self.input_nodes[0].value*2

		norMap = {
			"00": 47,
			"01": 30,
			"11": 25
		}
		return norMap[data], str(int(not (self.input_nodes[0].value or self.input_nodes[1].value)))

	def calc_leakage(self):
		
		for i in self.input_nodes:
			if i.value == -1:
				return False		
		self.leakage, self.output_node.value = self.leakage_funcs[self.type]()
		self.done = True
		return True