from __future__ import division

from utility import *
from Node import Node
from Module import Module
import itertools    

nodes = {}
modules = []

if __name__ == '__main__':
	
	f = open("part2.v", "r")
	
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


	A_input = [list(i) for i in itertools.product([0, 1], repeat=8)]
	B_input = [list(i) for i in itertools.product([0, 1], repeat=8)]
	count = 0

	A = {}
	B = {}
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
	for i in sums[0:5]:
		print ("for A = " + str(i[1][0]) + " and B = " + str(i[1][1]) + " leakage = " + str(i[0]))
