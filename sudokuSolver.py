
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
import operator


class Stack(object):
	def __init__(self, max_len):
		self.stack = [-1] * max_len
		self.top_idx = 0

	def push(self, v):
		self.stack[self.top_idx] = v
		self.top_idx += 1

	def pop(self):
		if self.top_idx > 0:
			self.top_idx -= 1
			return self.stack[self.top_idx]
		return None

	def top(self):
		if self.top_idx > 0:
			return self.stack[self.top_idx - 1]
		return None

	def get(self):
		return self.stack[:self.top_idx]



class Solution(object):
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		all_set = 511
		num_set = set([1<<i for i in range(9)])
		numbers = []
		for i in range(9):
			numbers.append([0]*9)

		for idx, x in enumerate(board):
			missed = all_set
			for idy, y in enumerate(x):
				if y != '.':
					integer = int(y)
					v = 1<<(integer - 1)
					missed = operator.xor(missed, v)

			for idy, y in enumerate(x):
				if y == '.':
					numbers[idx][idy] = missed

		stack = Stack(81)

		for i in range(9):
			missed = all_set
			for j in range(9):
				if board[j][i] != '.':
					integer = int(board[j][i])
					v = 1 << (integer - 1)
					missed = operator.xor(missed, v)

			for j in range(9):
				if board[j][i] == '.':
					numbers[j][i] = numbers[j][i] & missed
					if numbers[j][i] in num_set:
						stack.push(j + i*10)
		for idd, x in enumerate(numbers):
			print x

		while True:
			idx_v = stack.pop()
			if idx_v is None:
				return
			i, j = idx_v %10, idx_v /10
			matched = numbers[i][j]
			print i, j, numbers[i][j]

			for idx, vv in enumerate(numbers[i]):
				if vv == 0 or idx == j:
					continue
				vv = operator.xor(vv, matched)
				numbers[i][idx] = vv
				if vv in num_set:
					stack.push((i, idx))

			for ii in range(9):
				vv = numbers[ii][j]
				if vv == 0 or ii == i:
					continue
				vv = operator.xor(vv, matched)
				numbers[ii][j] = vv
				if vv in num_set:
					stack.push((ii, j))





solution = Solution()
input = [
	['5', '3', '.', '.', '7', '.', '.', '.', '.'],
	['6', '.', '.', '1', '9', '5', '.', '.', '.'],
	['.', '9', '8', '.', '.', '.', '.', '6', '.'],
	['8', '.', '.', '.', '6', '.', '.', '.', '3'],
	['4', '.', '.', '8', '.', '3', '.', '.', '1'],
	['7', '.', '.', '.', '2', '.', '.', '.', '6'],
	['.', '6', '.', '.', '.', '.', '2', '8', '.'],
	['.', '.', '.', '4', '1', '9', '.', '.', '5'],
	['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]
solution.solveSudoku(input)
