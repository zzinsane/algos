package main

/*
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

the key is tree node value could be less than 0
*/
import (
	"fmt"
	"math"
)

type TreeNode struct {
	Right *TreeNode
	Left  *TreeNode
	Val   int
}

func BuildwithRecursion(root *TreeNode, max *int) (int, int) {

	RightDepth := 0
	LeftDepth := 0

	if root.Right != nil {
		rightRight, rightLeft := BuildwithRecursion(root.Right, max)
		RightDepth = int(math.Max(float64(rightRight), float64(rightLeft)))
		if RightDepth < 0 {
			RightDepth = 0
		}
		RightDepth += root.Right.Val
	}

	if root.Left != nil {
		leftRight, leftLeft := BuildwithRecursion(root.Left, max)
		LeftDepth = int(math.Max(float64(leftRight), float64(leftLeft)))
		if LeftDepth < 0 {
			LeftDepth = 0
		}
		LeftDepth += root.Left.Val
	}

	//pathRoot := &PathNode{
	//	Right: RightPath,
	//	Left:LeftPath,
	//	RightDepth: RightDepth,
	//	LeftDepth:LeftDepth,
	//}
	rootBasedMax := RightDepth + LeftDepth + root.Val
	if *max < rootBasedMax {
		*max = rootBasedMax
	}
	rootBasedMax = RightDepth + root.Val
	if *max < rootBasedMax {
		*max = rootBasedMax
	}
	rootBasedMax = LeftDepth + root.Val
	if *max < rootBasedMax {
		*max = rootBasedMax
	}
	if *max < root.Val {
		*max = root.Val
	}
	fmt.Println("---", root.Val, *max, RightDepth, LeftDepth)

	return RightDepth, LeftDepth
}

func maxPathSum(root *TreeNode) int {
	max := root.Val
	BuildwithRecursion(root, &max)
	return max
}

func main() {
	//root := &TreeNode{
	//	Val:10,
	//	Right:&TreeNode{
	//		Val:15,
	//		Right:&TreeNode{
	//			Val:200,
	//		},
	//		Left:&TreeNode{
	//			Val:110,
	//		},
	//	},
	//	Left:&TreeNode{
	//		Val:7,
	//		Right:&TreeNode{
	//			Val:9,
	//		},
	//		Left:&TreeNode{
	//			Val:5,
	//			Right:&TreeNode{
	//				Val:8,
	//			},
	//			Left:&TreeNode{
	//				Val:1,
	//			},
	//		},
	//	},
	//}
	root := &TreeNode{
		Val: 9,
		Left: &TreeNode{
			Val: 6,
		},
		Right: &TreeNode{
			Val: -3,
			Left: &TreeNode{
				Val: -6,
			},
			Right: &TreeNode{
				Val: 2,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: -6,
						Left: &TreeNode{
							Val: -6,
						},
					},
					Right: &TreeNode{
						Val: -6,
					},
				},
			},
		},
	}
	fmt.Println(maxPathSum(root))
}
