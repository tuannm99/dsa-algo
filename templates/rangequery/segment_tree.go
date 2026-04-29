package rangequery

type SegmentTree struct {
	n    int
	tree []int
}

func NewSegmentTree(nums []int) *SegmentTree {
	st := &SegmentTree{
		n:    len(nums),
		tree: make([]int, 4*len(nums)),
	}
	if len(nums) > 0 {
		st.build(1, 0, len(nums)-1, nums)
	}
	return st
}

func (st *SegmentTree) build(node, left, right int, nums []int) {
	if left == right {
		st.tree[node] = nums[left]
		return
	}
	mid := left + (right-left)/2
	st.build(node*2, left, mid, nums)
	st.build(node*2+1, mid+1, right, nums)
	st.tree[node] = st.tree[node*2] + st.tree[node*2+1]
}

func (st *SegmentTree) Update(index, value int) {
	st.update(1, 0, st.n-1, index, value)
}

func (st *SegmentTree) update(node, left, right, index, value int) {
	if left == right {
		st.tree[node] = value
		return
	}
	mid := left + (right-left)/2
	if index <= mid {
		st.update(node*2, left, mid, index, value)
	} else {
		st.update(node*2+1, mid+1, right, index, value)
	}
	st.tree[node] = st.tree[node*2] + st.tree[node*2+1]
}

func (st *SegmentTree) Query(qLeft, qRight int) int {
	return st.query(1, 0, st.n-1, qLeft, qRight)
}

func (st *SegmentTree) query(node, left, right, qLeft, qRight int) int {
	if qLeft <= left && right <= qRight {
		return st.tree[node]
	}
	if right < qLeft || qRight < left {
		return 0
	}
	mid := left + (right-left)/2
	return st.query(node*2, left, mid, qLeft, qRight) +
		st.query(node*2+1, mid+1, right, qLeft, qRight)
}
