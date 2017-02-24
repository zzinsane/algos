'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""



		len1, len2 = len(nums1), len(nums2)

		total = len1 + len2
		start1, start2 = 0, 0
		end1, end2 = len1 - 1, len2 - 1

		left = total / 2
		odd = False
		if total % 2 == 1:
			left += 1
			odd = True

		def result(idx1, idx2):
			if odd:
				if nums1[idx1] < nums2[idx2]:
					return nums1[idx1]
				else:
					return nums2[idx2]



		while True:
			if left <= 1:
				if left == 1:
					if odd:
						return min(nums1[start1], nums2[start2])
					# return (nums1[start1] + nums2[start2]) / 2.0

					one = min(nums1[start1], nums2[start2])

					next1 = max(nums1[start1], nums2[start2])
					next2 = nums2[start2 + 1] if start2 + 1<len2 else None
					next_v = next1 if next2 is None else next2 if next1 is None else min(next1, next2)
					return ">>>", nums1[start1], nums2[start2]

				raise Exception('can not happen')
			# elif end1 < start1 or end2 < start2:
			# 	pass
			# 	print "........"
			# 	print left, nums1[start1:end1], nums2[start2:end2]
			# 	break

			med1 = (end1 - start1) /2 + start1
			left1 = med1 - start1 + 1

			med2 = (left - left1) + start2 - 1
			left2 = med2 - start2 + 1

			if nums1[med1] > nums2[med2]:
				left -= left2
				start2 = med2 + 1
				end1 = med1

			elif nums1[med1] < nums2[med2]:
				left -= left1
				start1 = med1 + 1
				end2 = med2
			else:
				if odd:
					return nums1[end1]

				next1 = nums1[end1 + 1] if end1 + 1<len1 else None
				next2 = nums2[end2 + 1] if end2 + 1<len2 else None
				next_v = next1 if next2 is None else next2 if next1 is None else min(next1, next2)
				return (next_v + nums1[end1]) / 2.0



solution = Solution()
# solution.findMedianSortedArrays([1, 2, 3, 4], [5, 6, 7])
print solution.findMedianSortedArrays([1, 2, 3, 7, 9], [4, 5, 6, 7, 8])

