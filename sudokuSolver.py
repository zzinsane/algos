
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
import operator, copy


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

	def length(self):
		return self.top_idx



class Solution(object):
	all_set= 511
	num_set = {1<<i:i+1 for i in range(9)}

	def find_bits(self, i, j):
		bits = []
		for k in range(9):
			if self.numbers[i][j] & (1<<k):
				bits.append(k)
		return bits


	def set_bits(self, idx_list):
		missed = Solution.all_set
		for idx, idy in idx_list:
			value = self.cp_board[idx][idy]
			if value != '.':
				integer = int(value)
				v = 1<<(integer - 1)
				missed = operator.xor(missed, v)
		for idx, idy in idx_list:
			value = self.cp_board[idx][idy]
			if value == '.':
				self.numbers[idx][idy] = self.numbers[idx][idy] & missed

	def propogate(self, i, j, idx_list):
		xored = self.numbers[i][j]
		for idx, idy in idx_list:
			composed = idx + idy * 10
			value = self.numbers[idx][idy]
			if self.cp_board[idx][idy] !='.' or self.bits_set_array[idx][idy]:
				if value == xored and not (idx == i and idy == j):
					return False

				continue
			value = value & ~ xored

			self.numbers[idx][idy] = value
			if value in Solution.num_set:
				self.stack.push(composed)
				self.bits_set_array[idx][idy] = True
		return True

	def fill_board(self):
		while True:
			idx_v = self.stack.pop()
			if idx_v is None:
				break

			i, j = idx_v %10, idx_v /10
			self.board[i][j] = '%s' % self.num_set.get(self.numbers[i][j])
			if not self.propogate(i, j, [(i, jj) for jj in range(9)]):
				return False

			if not self.propogate(i, j, [(ii, j) for ii in range(9)]):
				return False

			idx_list = []
			i_start, j_start = (i / 3)*3, (j/3)*3
			for i1 in range(3):
				for j1 in range(3):
					idx_list.append((i_start+i1, j_start+j1))
			if not self.propogate(i, j, idx_list):
				return False
		return True

	def print_all(self):

		for i in range(9):
			ele = []
			for j in range(9):
				if self.board[i][j] == '.':
					candidates = []
					for k in range(9):
						if self.numbers[i][j] & (1<<k):

							candidates.append("%s" % (k+1))
					ele.append(''.join(candidates))
				else:
					ele.append(self.board[i][j])
			ele_cp = ["%5s"%n for n in ele]
			print ele_cp


	def solveSudoku(self, board):
		numebrs = []
		self.bits_set_array = []
		for i in range(9):
			numebrs.append([Solution.all_set] * 9)
			self.bits_set_array.append([False] * 9)
		self.numbers = numebrs
		self.final_board = board
		self.board = board

		self.cp_board = copy.deepcopy(board)
		for i in range(9):
			self.set_bits([(i, j) for j in range(9)])
		for j in range(9):
			self.set_bits([(i, j) for i in range(9)])

		for i in range(3):
			for j in range(3):
				idx_list = []
				for i1 in range(3):
					for j1 in range(3):
						idx_list.append((i*3+i1, j*3+j1))
				self.set_bits(idx_list)

		self.stack = Stack(81)
		for i in range(9):
			for j in range(9):
				if numebrs[i][j] in Solution.num_set:
					self.stack.push(i + j*10)
					self.bits_set_array[i][j] = True

		self.fill_board()
		self.stak2 = Stack(81)

		while True:
			next_i, next_j = -1, -1
			min_sofar = 1000

			for i in range(9):
				for j in range(9):
					if self.board[i][j] == '.':
						candidates = self.find_bits(i, j)
						if len(candidates) < min_sofar:
							min_sofar = len(candidates)
							next_i, next_j = i, j
			if next_i == -1:
				for i in range(9):
					for j in range(9):
						self.final_board[i][j] = self.board[i][j]
				break

			candidates = self.find_bits(next_i, next_j)
			self.stak2.push([(next_i, next_j), candidates, 0, copy.deepcopy(self.numbers), copy.deepcopy(self.bits_set_array), copy.deepcopy(self.board), self.stack.length()])
			self.numbers[next_i][next_j] = 1<<candidates[0]
			self.stack.push(next_i + next_j * 10)
			self.bits_set_array[next_i][next_j] = True

			re = self.fill_board()
			if not re:
				while True:
					ele = self.stak2.pop()
					if ele is None:
						print "not possible!!!"
					[idxes, candidates, candidates_dix, numebrs_cp, bits_set_cp, board_cp, stack_len] = ele
					if candidates_dix < len(candidates) - 1:
						ele[2] += 1
						self.numbers = numebrs_cp
						self.bits_set_array = bits_set_cp
						self.board = board_cp
						while self.stack.length() > stack_len:
							self.stack.pop()
						self.numbers[idxes[0]][idxes[1]] = 1<<candidates[ele[2]]
						self.stack.push(idxes[0] + idxes[1] * 10)
						self.bits_set_array[idxes[0]][idxes[1]] = True
						re = self.fill_board()
						if re:
							break
						else:
							self.stak2.push(ele)
					else:
						continue


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

input = [
	"..9748...",
	"7........",
	".2.1.9...",
	"..7...24.",
	".64.1.59.",
	".98...3..",
	"...8.3.2.",
	"........6",
	"...2759.."]
c_input = []
for s in input:
	c_input.append([s[i:i+1] for i in range(9)])


solution.solveSudoku(c_input)
for x in c_input:
	print x

#["..9748...","7..6.2...",".2.1.9...","..7986241","264317598","198524367","...863.2.","...491..6","...2759.."]
#["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]

