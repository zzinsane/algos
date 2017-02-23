'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
	bool isMatch(const char *s,  const char *p)

https://leetcode.com/problems/regular-expression-matching/
'''

class Stack(object):
	def __init__(self, total):
		self.stack = [-1] * total
		self.total = total
		self.top_idx = 0

	def pop(self):
		if self.top_idx <= 0:
			return None
		self.top_idx -= 1
		return self.stack[self.top_idx]

	def push(self, value):
		self.stack[self.top_idx] = value
		self.top_idx += 1


class Solution(object):

	@classmethod
	def compress(cls, string):
		p_total = len(string)
		cp_p = []
		previous = ''
		cursor = 0
		while True:
			if cursor >= p_total:
				break
			char = string[cursor]
			next_char = string[cursor + 1] if cursor + 1 < p_total else ''
			if next_char == '*':
				if char != previous:
					previous = char
					cp_p.extend([char, '*'])

				cursor += 2
				continue
			cp_p.append(char)
			previous = ''
			cursor += 1

		return ''.join(cp_p)

	def match(self, char_s, char_p):
		if char_s == char_p or (char_p == '.'):
			return True
		return False

	def star_match(self, sub_s, char_p):
		if char_p == '.':
			return True
		for char_s in sub_s:
			if char_s != char_p:
				return False
		return True

	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""

		p = Solution.compress(p)

		s_start = 0
		p_start = 0
		s_total, p_total = len(s), len(p)

		stars = 0
		for char in p:
			if char == '*':
				stars += 1
		stack = Stack(stars)
		while True:
			if p_start + 1 < p_total and p[p_start + 1] == '*':
				stack.push((p_start, s_start, 0))
				p_start += 2
				continue

			if p_start >= p_total and s_start >= s_total:
				return True

			if p_start < p_total and s_start < s_total and self.match(s[s_start], p[p_start]):
				p_start += 1
				s_start += 1
				continue

			while True:
				last_match = stack.pop()
				# print last_match
				if last_match is None:
					return False
				star_p_start, star_s_start, match_len = last_match[0], last_match[1], last_match[2]
				match_len += 1
				s_sub = s[star_s_start:star_s_start + match_len]
				if len(s_sub) != match_len:
					continue
				if p[star_p_start] == '.' or self.star_match(s_sub, p[star_p_start]):
					# haha  get a further match
					stack.push((star_p_start, star_s_start, match_len))
					p_start = star_p_start + 2
					s_start = star_s_start + match_len
					break
				else:
					continue

solution = Solution()
# print solution.isMatch('ababa', "aba*a")
# print solution.isMatch('ababa', "aba*.*ab")
# print solution.isMatch('ababa', ".*")
# print solution.isMatch("aab", "c*a*b")
print solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*b*a*a*a*a*b")
print solution.isMatch("aaaaaaaaaaaaab", "a*b*a*b")
print solution.isMatch("aaaaaaaaaaaaab", "a*b*b*aaa*a*")
print solution.isMatch("aaaaaaaaaaaaab", "bbssa*b*a*a*a*cc")
print solution.isMatch("aaaaaaaaaaaaab", "a*b*a*b*a*b*a*b*c")
# print solution.isMatch("aaaaaaaaaaaaab", "a*b*c*d*e*a*b*x")
# print solution.isMatch("aaaaaab", "a*a*a*a*a*a*a*c")
