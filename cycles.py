# program that reads from a file of nodes and IDs,
# report if an ID demonstrates a cycle
import os
import sys

def main():
	# first make a cycle detector
	order = ["a", "b", "c", "a"]
	seen = set()
	while !(order == null):
		a = order.pop()
		if a in seen:
			print("Cycle")
			return
		else:
			seen.add(a)

main()