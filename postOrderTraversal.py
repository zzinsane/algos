'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def postorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""

'''
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Stack(object):
	def __init__(self, max_len):
		self.stack = [-1] * max_len
		self.top_idx = 0
		self.total = max_len

	def push(self, v):
		if self.top_idx >= self.total:
			self.stack.extend([-1] * 1000)
			self.total += 1000

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

	NODE = 1
	VALUE = 2

	def postorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""

		result = []
		if root is None:
			return result

		stack = Stack(1000)
		stack.push((root, Solution.NODE))
		while True:
			v = stack.pop()
			if v is None:
				break

			node, t = v[0], v[1]
			if t == Solution.NODE:
				stack.push((node, Solution.VALUE))
				if node.right:
					stack.push((node.right, Solution.NODE))
				if node.left:
					stack.push((node.left, Solution.NODE))
			else:
				result.append(node.val)

		return result


