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
		