package main


type TreeNode struct {
        Val int
        Left *TreeNode
        Right *TreeNode
}

func wrap(root, lower, swap *TreeNode) (next, mistake *TreeNode) {
	newLower := lower

        if root.Left != nil {
		newLower, mistake = wrap(root.Left, lower, swap)
	}



	//mistake = swap
	if swap == nil {
		swap = mistake
	}

	if newLower != nil {
		if newLower.Val > root.Val {
			if swap == nil {
				swap = newLower
			} else {
				vv := swap.Val
				swap.Val = root.Val
				root.Val = vv
			}
		}
	}


	next = root

	if root.Right != nil {
		next, mistake = wrap(root.Right, root, swap)
	}


	if mistake != nil {
		swap = mistake
	}
	return next, swap
}

func recoverTree(root *TreeNode)  {
	wrap(root, nil, nil)

}

func main(){
	root := &TreeNode{
		Val:10,
		Left:&TreeNode{
			Val:12,
			Left: &TreeNode{
				Val:3,
			},
			Right:&TreeNode{
				Val:7,
			},
		},
		Right:&TreeNode{
			Val:16,
			Left:&TreeNode{
				Val:5,
			},
			Right:&TreeNode{
				Val:17,
			},
		},
	}
	recoverTree(root)
}