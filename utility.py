from __future__ import division
from Node import Node
from Module import Module
import itertools    

def purify(line):
	for i in line:
		if len(i) == 0:
			line.remove(i)

def parser(line):
		key_names = ["XNOR", "XOR", "NAND", "AND", "NOR", "OR", "INV"]
		
		ports = []
		names = line.split('(')[0].split(' ')
		purify(names)
		t = names[0]
		type = ""

		for i in key_names:
			if i in t:
				type = i
				break

		purify(names)

		line = line.split('.')[1:]
		for i in line:
			s = i.split('(')[1].split(')')
			# purify(s)
			ports.append(s[0])

		return type, names[1], ports[0: -1], ports[-1]

def extract(fileName, modules, nodes):
	f = open(fileName, "r")
	for i in f:

		input_nodes = []
		lower_case = i.lower()
		
		if "inv" in lower_case or "and" in lower_case or "or" in lower_case:
			t, name, inputs, output = parser(i)

			if output not in nodes:
					nodes[output] = Node(output)

			for i in inputs:
				if i not in nodes:
					nodes[i] = Node(i)	
				input_nodes.append(nodes[i])

			output_node = nodes[output]

			modules.append(Module(t, name, input_nodes, output_node))

def calc_sums(A_input, B_input, modules, nodes):
	sums = []
	for i in A_input:
		for j in B_input:
			sum = 0
			for k in range(8):
				nodes["A["+str(k)+"]"].value = str(i[k])
				nodes["B["+str(k)+"]"].value = str(j[k])

			done = 0
			for l in modules:
				l.done = False

			while True:
				for l in modules:
					if l.done:
						continue
					elif l.calc_leakage():
						done += 1
					if done == len(modules):
						break
				if done == len(modules):
					break
			for l in modules:
				sum += l.leakage
			sums.append((sum, (i, j)))
	
	sums = sorted(sums, key=lambda x: x[0])
	return sums

def generate_inputs():
	A_input = [list(i) for i in itertools.product([0, 1], repeat=8)]
	B_input = [list(i) for i in itertools.product([0, 1], repeat=8)]
	return A_input, B_input

def print_leakage_results(sums, range):
	for i in sums[0:range]:
		print ("for A = " + str(i[1][0]) + " and B = " + str(i[1][1]) + " leakage = " + str(i[0]))
