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

solution:

get prefix arrays of len m, n of each array, m + n is half of total length (trackier for even total number)


'''

class Solution(object):

	def findMedianSortedArrays(self, nums1, nums2):
		self.nums1 = nums1
		self.nums2 = nums2
		self.len1, self.len2 = len(self.nums1), len(self.nums2)
		self.total = self.len1 + self.len2
		if self.total % 2 == 1:
			return self.findKthSortedArrays(self.total/2 + 1)

		v1 = self.findKthSortedArrays(self.total/2)
		v2 = self.findKthSortedArrays(self.total/2 + 1)
		return (v1+v2)/2.0

	def findKthSortedArrays(self, k):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""

		start1, start2 = 0, 0
		end1, end2 = self.len1 - 1, self.len2 - 1

		left = k

		while True:
			if start1 > end1:
				return self.nums2[start2 + left - 1]
			if start2 > end2:
				return self.nums1[start1 + left - 1]
			if left == 1:
				return min(self.nums1[start1], self.nums2[start2])

			if end1 - start1 > end2 - start2:
				med2 = (end2 - start2) /2 + start2
				left2 = med2 - start2 + 1
				med1 = (left - left2) + start1 - 1
				left1 = med1 - start1 + 1
			else:
				med1 = (end1 - start1) /2 + start1
				left1 = med1 - start1 + 1
				med2 = (left - left1) + start2 - 1
				left2 = med2 - start2 + 1

			if med2 < start2:
				raise Exception('not possible')

			# since the sum length of nums1[start:med1+1]  and nums2[start2:med2+1] is equal to left
			# we can discard the "lower" half array, and update left
			if self.nums1[med1] > self.nums2[med2]:
				left -= left2
				start2 = med2 + 1
				end1 = med1

			elif self.nums1[med1] < self.nums2[med2]:
				left -= left1
				start1 = med1 + 1
				end2 = med2
			else:
				return self.nums1[med1]

				# next1 = nums1[end1 + 1] if end1 + 1<len1 else None
				# next2 = nums2[end2 + 1] if end2 + 1<len2 else None
				# next_v = next1 if next2 is None else next2 if next1 is None else min(next1, next2)
				# return (next_v + nums1[end1]) / 2.0



solution = Solution()
# print solution.findMedianSortedArrays([1, 2, 3, 4], [5, 6, 7])
# print solution.findMedianSortedArrays([0, 1, 2, 3, 12, 17, 19, 23, 28, 30, 32, 62, 74, 76, 78, 83, 85, 88, 97, 97], [0, 12, 16, 23, 24, 47, 48, 54, 73])
# print solution.findMedianSortedArrays([8, 9, 10, 11], [6])
# print solution.findMedianSortedArrays([8], [6])
# print solution.findMedianSortedArrays([0, 8, 10, 20, 34, 38, 44, 47, 55, 64, 74, 78, 79, 80, 81, 89], [46, 60, 69, 81, 90])
# print solution.findMedianSortedArrays([45, 94], [8, 16, 19, 50, 63, 92])
# print solution.findMedianSortedArrays([0, 2, 8, 28, 29, 33, 40, 41, 41, 44, 47, 56, 56, 59, 74, 86, 93, 96], [15, 60, 84, 91])
# print solution.findMedianSortedArrays([4, 12, 16, 21, 22, 31, 31, 65, 82, 84, 87, 98], [18, 38, 42, 94])
# print solution.findMedianSortedArrays([48], [7, 33])


import random
import time
a = 0
b = 0
for i in range(0, 500):
	l1 = random.randint(0, 20000)
	l2 = random.randint(0, 20000)
	if l1 == 0 and l2 == 0:
		continue

	list1 = [random.randint(0, 100) for i in range(l1)]
	list2 = [random.randint(0, 100) for i in range(l2)]

	list1 = sorted(list1)
	list2 = sorted(list2)

	start = time.time() * 1000
	re1= solution.findMedianSortedArrays(list1, list2)
	a += time.time() * 1000 -start

	start = time.time() * 1000
	list1.extend(list2)
	list1 = sorted(list1)
	total = len(list1)
	if total % 2 == 0:
		re2 = (list1[total/2 - 1] + list1[total/2])/2.0
	else:
		re2 = list1[total/2]

	b += time.time() * 1000 -start

	if re1 != re2:
		print list1, list2
		print re1, re2

print a, b
