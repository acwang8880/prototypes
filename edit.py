# program to determine minimum edit distance between two strings
import sys
import os


def edit(n, m):
	# a_len = len(a)
	# b_len = len(b)
	# lemon = 0

	# a_start = 0
	# b_start = 0

	if (b_len > a_len):
		lemon = b_len
	else:
		lemon = a_len

	for i in range(m):
		for j in range(n):

			return 

def main():

	def diff(i, j, a, b):
		print("len a: {0} | i: {1}\nlen b: {2} | j: {3}\n".format(len(a), i, len(b), j))
		if (i >= len(a) or j >= len(b)):
			return 1
		elif (a[i] == b[j]):
			return 0
		else:
			return 1
	# a = sys.args[0]
	# b = sys.args[1]
	a = "tree"
	b = "tee"

	m = len(b)
	n = len(a)

	matrix = [[0 for j in range(len(a))] for i in range(len(b))]
	
	for i in range(m):
		matrix[i][0] = i

	for j in range(n):
		matrix[0][j] = j

	for i in range(m):
		for j in range(n):
			matrix[i][j] = min(matrix[i-1][j] + 1,
								matrix[i][j-1] + 1,
								matrix[i-1][j-1] + diff(i, j, a, b))
	print(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if j == len(matrix[i]) - 1:
				print(matrix[i])
			print()
	print(matrix[m-1][n-1])

main()