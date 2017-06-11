package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func wrap(root, lower, swap *TreeNode) (next, mistake *TreeNode, done bool) {

	if root.Left != nil {
		leftNext, leftMis, done := wrap(root.Left, lower, swap)
		// if in left branch, swap has been done, then exit
		if done {
			return nil, nil, done
		}
		lower = leftNext
		swap = leftMis
	}

	// find a wrong order value
	if lower != nil && lower.Val > root.Val {
		// there is another wrong value before, so just swap them
		if swap != nil {
			temV := swap.Val
			swap.Val = root.Val
			root.Val = temV
			// mark swap has been done
			return nil, nil, true
		}
		swap = lower
	}
	lower = root

	if root.Right != nil {
		rightNext, rightMis, done := wrap(root.Right, root, swap)
		if done {
			return nil, nil, done
		}
		swap = rightMis
		lower = rightNext
	}
	return lower, swap, false

}

func swapImmediately(root *TreeNode, lower *TreeNode, swap *TreeNode) *TreeNode {

	if root.Left != nil {
		next := swapImmediately(root.Left, lower, swap)
		lower = next
	}

	if lower == swap && lower != nil {
		temV := swap.Val
		swap.Val = root.Val
		root.Val = temV
	}

	lower = root

	if root.Right != nil {
		lower = swapImmediately(root.Right, lower, swap)
	}
	return lower
}

func recoverTree(root *TreeNode) {
	_, swap, done := wrap(root, nil, nil)

	if !done {
		swapImmediately(root, nil, swap)
	}
}

func main() {
	root := &TreeNode{
		Val: 10,
		Left: &TreeNode{
			Val: 5,
			Left: &TreeNode{
				Val: 3,
			},
			Right: &TreeNode{
				Val: 7,
			},
		},
		Right: &TreeNode{
			Val: 12,
			Left: &TreeNode{
				Val: 16,
			},
			Right: &TreeNode{
				Val: 17,
			},
		},
	}
	//root = &TreeNode{
	//	Val:2,
	//	Left:&TreeNode{
	//		Val:0,
	//	},
	//	Right:&TreeNode{
	//		Val:1,
	//	},
	//}

	recoverTree(root)
}
