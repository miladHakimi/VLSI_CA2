from __future__ import division

from utility import *
from Node import Node
from Module import Module

nodes = {}
modules = []

if __name__ == '__main__':
	
	f = open("part1.v", "r")
	
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

				nodes[output] = output_node
				input_nodes.append(nodes[i])
			
			output_node = nodes[output]
			modules.append(Module(t, name, input_nodes, output_node))

	f = open("input.txt", "r")

	A = {}
	B = {}
	count = 0

	for i in f:
		count += 1
		for j in range(8):
			index = str(j)
			if index not in A:
				A[index] = 0
				B[index] = 0

			A[index] += int(i[j])
			B[index] += int(i[j+8])

	for i in A:
		nodes["A["+i+"]"].p = A[i]/count
	for i in B:
		nodes["B["+i+"]"].p = B[i]/count

	for i in modules:
		i.calc()

	for i in nodes:
		print(nodes[i])