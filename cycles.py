# program that reads from a file of nodes and IDs,
# report if an ID demonstrates a cycle
import os
import sys

def check(dict, ID):
	temp = dict[ID]
	while (not temp is null):
		a = temp.pop()
		if a in seen:
			print("Cycle with plate: {0} | Cycle: {1}".format(ID, dict[ID]))
			return
		else:
			seen.add(a)

def main():
	# first make a cycle detector
	order = {}
	
	seen = set()

	f = os.open("routes.in")
	line = f.nextLine()
	while (line is not null):
		vals = line.split(" ")
		node = vals[0]
		plate = vals[1]
		if plate not in order.keys():
			order[plate] = [node]
		else:
			order[plate].append(node)

		
	for key in order.keys():
		check(order, key)
main()