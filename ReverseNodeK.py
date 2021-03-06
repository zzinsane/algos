'''
Given a linked list,  reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes,  only nodes itself may be changed.

Only constant memory is allowed.

For example, 
Given this linked list: 1->2->3->4->5

For k = 2,  you should return: 2->1->4->3->5

For k = 3,  you should return: 3->2->1->4->5

Subscribe to see which companies asked this question.
'''

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def print_all(self, l):
		array = []
		a = l
		while a:
			array.append("%s" %a.val)
			a = a.next
		print "==>".join(array)

	def reverse(self, head):

		before, after = head, head.next
		before.next = None
		sofar = 0

		while True:
			tmp = None
			if after.next:
				tmp = after.next
			after.next = before

			sofar += 1
			if sofar == k:
				pass

			before = after
			if tmp is None:
				break
			else:
				after = tmp
		return after


	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		start = head
		total = 0
		while start:
			total += 1
			start = start.next
		if total < k:
			return head

		iterate = total / k

		head = head
		first, last = None, None
		last_round_last = None

		for i in range(iterate):
			before, after = head, head.next
			before.next = None
			before_cp = before
			sofar = 1
			while True:
				if sofar == k:
					break

				tmp = None
				if after.next:
					tmp = after.next
				after.next = before

				sofar += 1

				before = after
				if tmp is None:
					break
				else:
					after = tmp

			if i == 0:
				first = before

			if last_round_last:
				last_round_last.next = before

			last_round_last = before_cp
			head = after
		if total % k != 0:
			last_round_last.next= head

		return first


l = ListNode(1)
s = l
for i in range(2, 3):
	l.next = ListNode(i)
	l = l.next

solution = Solution()
# solution.print_all(l)

s = solution.reverseKGroup(s, 2)
solution.print_all(s)


