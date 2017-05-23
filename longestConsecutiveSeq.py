'''
Given an unsorted array of integers,  find the length of the longest consecutive elements sequence.

For example, 
Given [100,  4,  200,  1,  3,  2], 
The longest consecutive elements sequence is [1,  2,  3,  4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Subscribe to see which companies asked this question.
'''

class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:t
		ype nums: List[int]
		:rtype: int
		"""

		length = len(nums)

		next_arr = [None] * length
		start = [None] * length
		nums_map = {}
		for idx, n in enumerate(nums):
			match = nums_map.get(n+1)
			nums_map[n] = idx
			if match is None:
				continue
			next_arr[idx] = match
			start[match] = 1

		nums_map.clear()
		for i in range(length):
			idx = length - i - 1
			n = nums[idx]

			match=  nums_map.get(n+1)
			nums_map[n] = idx
			if match is None:
				continue
			next_arr[idx] = match
			start[match] = 1

		longest = 0
		for idx, a in enumerate(start):
			if a is None:
				conse_len = 0
				n_step = idx
				while True:
					conse_len += 1
					n_step = next_arr[n_step]
					if n_step is None:
						break
				if longest < conse_len:
					longest = conse_len

		return longest





solution = Solution()
print solution.longestConsecutive([100, 4, 200, 1, 3, 2])
print solution.longestConsecutive([10, 20, 9, 1, 7, 2, 5, 7, 6, 9, 8, 4, 3])


