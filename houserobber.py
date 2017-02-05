class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def get_max_robbery_wrapper(r):
            if r is None:
                return 0, False

            if hasattr(r, 'total'):
                return r.total, r.occupy
            total, occupy = get_max_robbery(r)
            r.total = total
            r.occupy = occupy

            return total, occupy


        def get_max_robbery(r):

            if r.left:
                leftTotal, rootLeft = get_max_robbery_wrapper(r.left)
            else:
                leftTotal, rootLeft = 0,  False

            if r.right:
                rightTotal, rootRight = get_max_robbery_wrapper(r.right)
            else:
                rightTotal, rootRight = 0,  False

            if not rootLeft and not rootRight:
                return r.val + leftTotal + rightTotal, True

            maxVal = 0

            checkroots = []
            if rootLeft:
                checkroots.extend([r.left.left, r.left.right])
            else:
                maxVal += leftTotal

            if rootRight:
                checkroots.extend([r.right.left, r.right.right])
            else:
                maxVal += rightTotal

            for aroot in checkroots:
                v, _ = get_max_robbery_wrapper(aroot)
                maxVal += v

            return max(maxVal + r.val, leftTotal + rightTotal), True if (maxVal + r.val) > (leftTotal + rightTotal) else False


        total, _ = get_max_robbery_wrapper(root)
        return total



array = [3,2,3,None,3,None,1]
length = len(array)
treeNodeArray = [0] * length
for idx, a in enumerate(array):
    treeNodeArray[idx] = TreeNode(a) if a else None

for idx, node in enumerate(treeNodeArray):
    if node:
		node.left = treeNodeArray[2 * idx + 1] if (2*idx+1) <length else None
		node.right = treeNodeArray[2 * idx + 2] if (2*idx+2) <length else None

root = treeNodeArray[0]

solution = Solution()
print solution.rob(root)
