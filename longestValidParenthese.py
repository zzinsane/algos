"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Subscribe to see which companies asked this question.
"""
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
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		length = len(s)
		stack1 = Stack(length)
		stack2 = Stack(length)
		for idx, c in enumerate(s):
			top_c = stack1.top()
			if top_c == '(' and c == ')':
				stack1.pop()
				stack2.pop()
			else:
				stack1.push(c)
				stack2.push(idx)

		longest = 0

		stack = [0] + stack2.get() + [length + 1]

		for idx, v in enumerate(stack):
			if idx == 0:
				continue

			current = v - stack[idx - 1] - 1
			longest = max(current, longest)

		return longest

solution = Solution()
print solution.longestValidParentheses(")()())")
print solution.longestValidParentheses(")()()()()(((()))))")
solution.longestValidParentheses("((((()))")
print solution.longestValidParentheses("()")
print solution.longestValidParentheses("()()")
