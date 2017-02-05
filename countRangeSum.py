import time
class Solution(object):

	cache_mapping = {}
	max_idx = []
	min_idx = []


	def get_from_cach(self, limit, lower, upper):
		cache = self.cache_mapping.get(limit, {})
		return cache.get((lower, upper), None)

	def recursive(self, nums, limit, lower, upper):
		self.total += 1
		if limit < 0:
			return 0


		if self.max_idx[limit] < lower or self.min_idx[limit] > upper:
			return 0

		v = self.get_from_cach(limit, lower, upper)
		if v is not None:
			return v
		if limit == 0:
			if lower<=nums[0]<=upper:
				return 1
			else:
				return 0

		ranges1 = self.recursive(nums, limit-1, lower, upper)
		ranges2 = self.recursive(nums, limit-1, lower-nums[limit], upper-nums[limit])
		if lower<=nums[limit]<=upper:
			ranges2 +=1

		final = ranges1 + ranges2

		cache = self.cache_mapping.get(limit, {})
		cache[(lower, upper)] = final
		self.cache_mapping[limit] = cache

		return final

	def countRangeSum(self, nums, lower, upper):
		"""
		:type nums: List[int]
		:type lower: int
		:type upper: int
		:rtype: int
		"""
		self.total = 0
		nums = sorted(nums)
		if len(nums) > 0:
			self.max_idx = range(0, len(nums))
			self.min_idx = range(0, len(nums))
			minimal = 0
			for idx, i in enumerate(nums):
				if i <0:
					self.max_idx[idx] = i
					self.min_idx[idx] = self.min_idx[idx-1] + i if idx >0 else i
					minimal += i
				else:
					self.max_idx[idx] = max(self.max_idx[idx-1] + i if idx > 0 else i, i)
					self.min_idx[idx] = minimal

		value = self.recursive(nums, len(nums) - 1, lower, upper)
		print self.total
		return value

solution = Solution()
array = [14, -30, 22, 8, 3, 20, -11, 8, 7, -9, -7, -13, -5, -22, 11, 23, 15, 29, -17, -27, -2, 14, 14, 11, 22, -14, -27, -5, -9, -21, 22, 3, 12, 7, -13, 14, -23, -16, 12, -4, 21, -8, -18, 22, 17, -19, -22, 8, 2, -2, 24, -12, -24, -16, -2, 19, 7, 7, -20, 8]
start = int(time.time()*1000)
print solution.countRangeSum(array, 39, 88)
print  int(time.time()*1000) - start

array = [1135,-1067,-557,1629,-136,151,676,-1470,-1031,-1973,1120,291,-35,2923,1313,-105,-878,2201,1123,-1283,-263,-500,87,-2735,538,2582,2866,-1587,-1118,1201,-2280,-2372,2106,1527,-2671,-1446,-2139,-47,-218,1879,-2411,1687,-1125,-406,2155,566,600,-814,-903,-144,453,-1976,-1898,-2802,-2031,-816,2253,1456,623,847]
start = int(time.time()*1000)
print solution.countRangeSum(array, -5604, -3813)

print  int(time.time()*1000) - start

print solution.countRangeSum([], 0, 0)
print solution.countRangeSum([-2, 5, 1], -2, 2)
