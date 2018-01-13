# program to determine minimum edit distance between two strings
import sys
import os

def main():

	def diff(i, j, a, b):
		# print("len a: {0} | i: {1}\nlen b: {2} | j: {3}\n".format(len(a), i, len(b), j))
		if (i >= len(a) or j >= len(b)):
			print("exeec")
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

	matrix = [[0 for j in range(m)] for i in range(n)]
	
	for i in range(n):
		matrix[i][0] = i

	for j in range(m):
		matrix[0][j] = j

	for i in range(n):
		for j in range(m):
			matrix[i][j] = min(matrix[i-1][j] + 1,
								matrix[i][j-1] + 1,
								matrix[i-1][j-1] + diff(i, j, a, b))
	print(matrix)
	for i in range(len(matrix)):
		print(matrix[i])
	# print(matrix[n-1][m-1])
	print(matrix[n - 2][m - 1])

main()