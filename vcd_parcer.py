from Variable import Variable
node_map = {}
modules = []

def parser():
	f = open("testII.vcd", "r")
	for i in f:
		if "$scope module" in i:
			modules.append(i.split("$scope module ")[1].split("$end")[0])
		elif "$upscope" in i:
			modules.pop()
		elif "$var" in i:
			var = Variable(i, modules[-1])
			node_map[var.mapped_name] = var
		elif i[0] == "0" or i[0] == "1":
			data = i.split('\n')[0].split('\r')[0]
			if data[1:] not in node_map:
				print("Node " + data[1:] + " not found!")
			else:
				node_map[data[1:]].update(data[0])

if __name__ == '__main__':
	parser()
	for i in node_map:
		print(node_map[i])

		
