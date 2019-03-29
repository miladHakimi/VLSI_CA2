def purify(line):
	for i in line:
		if len(i) == 0:
			line.remove(i)

def parser(line):
		ports = []
		names = line.split('(')[0].split(' ')
		
		t = names[0]
		type = ""
		if "XNOR" in t or "XOR" in t:
			type = "XOR"
		elif "AND" in t:
			type = "AND"
		elif "OR" in t:
			type = "OR"

		purify(names)

		line = line.split('.')[1:]
		for i in line:
			s = i.split('(')[1].split(')')
			# purify(s)
			ports.append(s[0])

		return type, names[1], ports[0: -1], ports[-1] 