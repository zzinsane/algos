class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""

		start = ListNode(0)
		cp_start = start
		kNodes = [ll for ll in lists if ll is not None]


		kNodes = sorted(kNodes, key=lambda v:v.val)

		while len(kNodes) > 0:
			first = kNodes.pop(0)
			start.next = first
			start = start.next

			if start.next:
				pos = len(kNodes)
				for idx, node in enumerate(kNodes):
					if start.next.val <= node.val:
						pos = idx
						break
				kNodes.insert(pos, start.next)


		return cp_start.next










solution = Solution()


# l1 = ListNode()
a= [1, 2]
a.insert(2, 4)
print a