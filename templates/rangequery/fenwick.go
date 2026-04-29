package rangequery

type Fenwick struct {
	tree []int
}

func NewFenwick(n int) *Fenwick {
	return &Fenwick{tree: make([]int, n+1)}
}

func (f *Fenwick) Add(index, delta int) {
	for i := index + 1; i < len(f.tree); i += i & -i {
		f.tree[i] += delta
	}
}

func (f *Fenwick) PrefixSum(index int) int {
	sum := 0
	for i := index + 1; i > 0; i -= i & -i {
		sum += f.tree[i]
	}
	return sum
}

func (f *Fenwick) RangeSum(left, right int) int {
	if left == 0 {
		return f.PrefixSum(right)
	}
	return f.PrefixSum(right) - f.PrefixSum(left-1)
}
