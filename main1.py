from utility import *
from Node import Node
from Module import Module

nodes = {}
modules = []

if __name__ == '__main__':
	
	f = open("part1.v", "r")
	
	for i in f:
		lower_case = i.lower()
		if "inv" in lower_case or "and" in lower_case or "or" in lower_case:
			type, name, inputs, output = parser(i)
			for i in inputs:
				input_nodes = []
				if i not in nodes:
					nodes[i] = Node(i)	

				output_node = Node(output)
				nodes[output] = output_node
				input_nodes.append(nodes[i])

			modules.append(Module(type, name, input_nodes, output_node))

	# f = open("input.txt", "r")

	# for i in f:
		