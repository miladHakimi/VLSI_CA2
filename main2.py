from __future__ import division

from utility import *
import itertools    

nodes = {}
modules = []

if __name__ == '__main__':
	
	extract("part2.v", modules, nodes)
	A_input, B_input = generate_inputs()
	
	print_leakage_results(calc_leakages(A_input, B_input, modules, nodes), 5)
