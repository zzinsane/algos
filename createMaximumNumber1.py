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
			elif v2>v1:
				v = v2
				start2 += 1
			else:
				# v2 == v1, need to back check to decide
				back_start1 = start1
				back_start2 = start2
				while True:
					vv1 = n1[back_start1] if back_start1 < len1 else -1
					vv2 = n2[back_start2] if back_start2 < len2 else -1
					back_start1 += 1
					back_start2 += 1
					if vv1 != vv2 or (vv1 == vv2 and vv1 == -1):
						if vv1 >= vv2:
							v = v1
							start1 += 1
						else:
							v = v2
							start2 += 1
						break


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

		minimum1 = k - n2

		for i in range(max(0, minimum1), min(n1, k) + 1):
			re1 = self.find_max_by_length(nums1, sorted1, n1, i)
			re2 = self.find_max_by_length(nums2, sorted2, n2, k - i)
			self.merge(re1, i, re2, k - i, result)
		return result



start_time = time.time() * 1000
array1, array2 = [], []

solution = Solution()
# for i in range(0, 500):
# 	array1.append(random.randint(0, 9))
# 	array2.append(random.randint(0, 9))
# solution.maxNumber(array1, array2, 200)
# print time.time() * 1000 - start_time



print solution.maxNumber(
	[4,6,9,1,0,6,3,1,5,2,8,3,8,8,4,7,2,0,7,1,9,9,0,1,5,9,3,9,3,9,7,3,0,8,1,0,9,1,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2],
    [9,9,4,5,1,2,0,9,3,4,6,3,0,9,2,8,8,2,4,8,6,5,4,4,2,9,5,0,7,3,7,5,9,6,6,8,8,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3], 60)

print time.time() * 1000 - start_time
