'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,  compute how much water it is able to trap after raining.

For example,  
Given [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],  return 6.

https://leetcode.com/problems/trapping-rain-water/
key is to find tallest value in left and right part of array for each element i, say they are Pi, Ni
and rain trapped on this ele is min(Pi, Ni) - i
'''


class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		total= len(height)
		tallest_in_right = [-1] * total
		tallest_in_left = [-1] * total

		tallest= 0
		for idx, val in enumerate(height):
			if val > tallest:
				tallest = val
			tallest_in_left[idx] = tallest

		tallest= 0
		for idx in range(total - 1, -1, -1):
			val = height[idx]
			if val > tallest:
				tallest = val
			tallest_in_right[idx] = tallest

		# print tallest_in_left
		# print tallest_in_right

		rain = 0
		for idx, val in enumerate(height):
			current= min(tallest_in_right[idx], tallest_in_left[idx]) - val
			rain += current
		return rain


solution = Solution()
print solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print solution.trap([1, 1])
print solution.trap([1, 2])
print solution.trap([1, 2, 1, 3])

