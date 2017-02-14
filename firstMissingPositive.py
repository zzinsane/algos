'''
Given an unsorted integer array,  find the first missing positive integer.

For example, 
Given [1, 2, 0] return 3, 
and [3, 4, -1, 1] return 2.

Your algorithm should run in O(n) time and uses constant space.

the key is to use  existing array to store info whether a integer has appeared

'''
class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		total = len(nums)
		if len(nums) == 0:
			return 1
		start,end = None,None
		for num in nums:
			if num < start or start is None:
				start = num
			if num > end or end is None:
				end = num

		start = 0 if start <0 else start

		for idx, num in enumerate(nums):
			if num == 0:
				nums[idx] = -1

		for idx, num in enumerate(nums):
			value = num
			while True:
				new_idx = value - 1
				if new_idx >= total or new_idx <0:
					break

				if nums[new_idx] == 0:
					break
				value = nums[new_idx]
				nums[new_idx] = 0

		for idx, num in enumerate(nums):
			if num != 0:
				return idx + 1

		if start - 1 > 0:
			return start - 1
		return end + 1


solution = Solution()
# print solution.firstMissingPositive([1,1])
# print solution.firstMissingPositive([-1,-2,1,0,2])
# print solution.firstMissingPositive([1, 2, 7, 3, 9])
# print solution.firstMissingPositive([1, 6, 3, 10000])
# print solution.firstMissingPositive([5, 6, 7])
# print solution.firstMissingPositive([-1, -2])
# print solution.firstMissingPositive([1, 2, 3, 4, 5])
print solution.firstMissingPositive([0,2,2,4,0,1,0,1,3])

