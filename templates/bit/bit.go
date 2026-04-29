package bit

func CountBits(n int) []int {
	result := make([]int, n+1)
	for i := 1; i <= n; i++ {
		result[i] = result[i>>1] + (i & 1)
	}
	return result
}

func SingleNumber(nums []int) int {
	x := 0
	for _, v := range nums {
		x ^= v
	}
	return x
}

func SubsetsBitmask(nums []int) [][]int {
	result := [][]int{}
	total := 1 << len(nums)

	for mask := 0; mask < total; mask++ {
		subset := []int{}
		for i := 0; i < len(nums); i++ {
			if mask&(1<<i) != 0 {
				subset = append(subset, nums[i])
			}
		}
		result = append(result, subset)
	}

	return result
}
