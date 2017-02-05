import time
import random


class Solution(object):


	def find_max_by_length(self, array, sorted_array, total, length):
		if length == 0:
			return []

		result = [-1] * length
		start, end = 0, 0
		max_idx = -1
		for idx in sorted_array:
			if start >= length - end:
				break

			if idx < max_idx:
				continue

			left = total - idx
			need = length - start

			if need < left:
				result[start] = array[idx]
				start += 1
				if idx > max_idx:
					max_idx = idx
			elif need == left:
				for i in range(0, length - start):
					result[start + i] = array[idx + i]

				break
			else:
				if left > end:
					for i in range(0, left - end):
						result[length - left + i] = array[idx + i]
					end = left
		return result

	def merge(self, n1, len1, n2, len2, result):
		start1, start2 = 0, 0
		idx = 0
		renew = False
		while idx < (len1 + len2):
			v1 = n1[start1] if start1 < len1 else -1
			v2 = n2[start2] if start2 < len2 else -1

			if v1>v2:
				v = v1
				start1 += 1
			else:
				v = v2
				start2 += 1

			if renew:
				result[idx] = v
			else:
				if v > result[idx]:
					result[idx] = v
					renew = True

				elif v < result[idx]:
					return

			idx += 1


	def maxNumber(self, nums1, nums2, k):

		n1,n2 = len(nums1), len(nums2)
		if n1 > n2:
			tmp = nums1
			nums1 = nums2
			nums2 = tmp

			n1,n2 = len(nums1), len(nums2)

		sorted1 = sorted(range(n1), key=lambda v: nums1[v], reverse=True)
		sorted2 = sorted(range(n2), key=lambda v: nums2[v], reverse=True)

		result = [-1] * k
		for i in range(0, min(n1, k)):
			re1 = self.find_max_by_length(nums1, sorted1, n1, i)
			re2 = self.find_max_by_length(nums2, sorted2, n2, k - i)
			self.merge(re1, i, re2, k - i, result)
			print result


start_time = time.time() * 1000
array1, array2 = [], []

for i in range(0, 500):
	array1.append(random.randint(0, 9))
	array2.append(random.randint(0, 9))
solution = Solution()
solution.maxNumber(array1, array2, 200)
print time.time() * 1000 - start_time
