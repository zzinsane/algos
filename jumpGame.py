'''
Jump Game II
Given an array of non-negative integers,  you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
	Given array A = [2, 3, 1, 1, 4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1,  then 3 steps to the last index.)
the key is that by each step n, can cover a range of ele of array.
for example, first step covers range [1, 2],  second step covers range[3, 4]
'''

class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		total= len(nums)
		steps = 0
		start, end = 0, 0
		n_start, n_end = 0, 0
		if total <= 1:
			return 0

		while True:
			for i in range(start, min(end + 1, total)):
				value = nums[i]
				reach = value + i
				if reach >= total - 1:
					return steps + 1
				n_end = max(n_end,  reach)

			start = end + 1
			end = n_end
			steps += 1

solution = Solution()
print solution.jump([2, 3, 1, 1, 4])
print solution.jump([2, 3, 6, 6, 2, 1, 1])
print solution.jump([5, 1, 6, 7, 4, 9, 7, 6, 7, 7, 4, 0, 10, 0, 4, 0, 6, 10, 8, 4, 5, 9, 8, 10, 6, 8, 8, 4, 2, 3, 6, 2, 1, 4, 9, 6, 6, 4, 1, 6, 8, 9, 10, 9, 9, 3, 8, 10, 8, 4, 9, 9, 8, 2, 4, 2, 1, 2, 9, 7, 4, 3, 6, 10, 4, 2, 2, 10, 4, 0, 0, 3, 9, 8, 0, 0, 5, 3, 5, 5, 7, 9, 9, 2, 0, 3, 7, 4, 8, 10, 5, 0, 10, 9, 0, 9, 0, 7, 4, 5])
