

class Solution(object):
	def candy(self, ratings):
		"""
		:type ratings: List[int]
		:rtype: int
		"""
		length = len(ratings)
		sorted_idx = sorted(range(0, length), key=lambda a:ratings[a])
		candyes = [1] * length
		for v in sorted_idx:
			rating = ratings[v]
			if v > 0:
				max1 = candyes[v - 1] if ratings[v - 1] < rating else 0
			else:
				max1 = 0

			if v + 1 < length:
				max2 = candyes[v + 1] if ratings[v + 1] < rating else 0
			else:
				max2 = 0

			candyes[v] = max(max(max1, max2) + 1, candyes[v])

		return sum(candyes)


solution = Solution()

print solution.candy([5, 1, 5, 7, 2])
