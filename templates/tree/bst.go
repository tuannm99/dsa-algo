package tree

func IsValidBST(root *TreeNode) bool {
	var dfs func(*TreeNode, *int, *int) bool
	dfs = func(node *TreeNode, low, high *int) bool {
		if node == nil {
			return true
		}
		if low != nil && node.Val <= *low {
			return false
		}
		if high != nil && node.Val >= *high {
			return false
		}
		return dfs(node.Left, low, &node.Val) && dfs(node.Right, &node.Val, high)
	}
	return dfs(root, nil, nil)
}

func KthSmallest(root *TreeNode, k int) int {
	st := []*TreeNode{}
	cur := root
	for cur != nil || len(st) > 0 {
		for cur != nil {
			st = append(st, cur)
			cur = cur.Left
		}
		cur = st[len(st)-1]
		st = st[:len(st)-1]
		k--
		if k == 0 {
			return cur.Val
		}
		cur = cur.Right
	}
	return -1
}
