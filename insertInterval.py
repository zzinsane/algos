'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Subscribe to see which companies asked this question.
'''


# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

def binary_search(array, value, length):
	start, end = 0, length

	while True:
		if start >= end:
			return start

		idx = (end-start)/2 + start
		if value > array[idx]:
			start = idx + 1
		else:
			end = idx


class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[Interval]
		:type newInterval: Interval
		:rtype: List[Interval]
		"""
		interval_len = len(intervals)
		interval_idx = [0] * (interval_len * 2)


		for idx, interval in enumerate(intervals):
			interval_idx[idx * 2] = interval.start
			interval_idx[idx * 2 + 1] = interval.end

		new_s = newInterval.start
		new_e = newInterval.end

		s_pos = binary_search(interval_idx, new_s, interval_len * 2)
		e_pos = binary_search(interval_idx, new_e, interval_len * 2)

		new_list = []
		new_list.extend(intervals[0:s_pos/2])

		start, end = new_s, new_e

		if s_pos %2 == 1 and (s_pos/2) < interval_len:
			start = intervals[s_pos/2].start

		end_half_start = e_pos/2+1 if e_pos%2==1 else e_pos /2

		if e_pos %2 == 1 and (e_pos/2) < interval_len:
			end = intervals[end_half_start - 1].end

		# to handle case: [(1, 7), (8, 9)] (1, 8) => [(1, 9)]
		if e_pos %2 == 0 and (e_pos < (interval_len*2) and interval_idx[e_pos] == new_e):
			end = intervals[end_half_start].end
			end_half_start = end_half_start + 1

		new_list.append(Interval(start, end))

		new_list.extend(intervals[end_half_start:])
		return new_list

v = []
# print binary_search(v, )
intervals = []
for i in range(len(v)/2):
	intervals.append(Interval(v[i*2], v[i*2+1]))

solution = Solution()
a = solution.insert([], Interval(5, 8))
for interval in a:
	print interval.start, interval.end
