from __future__ import division

from utility import *
from Node import Node
from Module import Module

nodes = {}
modules = []

if __name__ == '__main__':
	A = {}
	B = {}
	
	extract("part1.v", modules, nodes)
	A, B, count = get_primary_inputs()
	

	for i in A:
		nodes["A["+i+"]"].p = A[i]/count
	for i in B:
		nodes["B["+i+"]"].p = B[i]/count

	for i in modules:
		i.calc()

	for i in nodes:
		print(nodes[i])