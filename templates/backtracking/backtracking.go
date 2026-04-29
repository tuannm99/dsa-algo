package backtracking

func Subsets(nums []int) [][]int {
	result := [][]int{}
	path := []int{}

	var dfs func(int)
	dfs = func(start int) {
		snapshot := append([]int{}, path...)
		result = append(result, snapshot)

		for i := start; i < len(nums); i++ {
			path = append(path, nums[i])
			dfs(i + 1)
			path = path[:len(path)-1]
		}
	}

	dfs(0)
	return result
}

func Permutations(nums []int) [][]int {
	result := [][]int{}
	path := []int{}
	used := make([]bool, len(nums))

	var dfs func()
	dfs = func() {
		if len(path) == len(nums) {
			result = append(result, append([]int{}, path...))
			return
		}

		for i := range nums {
			if used[i] {
				continue
			}
			used[i] = true
			path = append(path, nums[i])
			dfs()
			path = path[:len(path)-1]
			used[i] = false
		}
	}

	dfs()
	return result
}

func CombinationSum(candidates []int, target int) [][]int {
	result := [][]int{}
	path := []int{}

	var dfs func(int, int)
	dfs = func(start, remain int) {
		if remain == 0 {
			result = append(result, append([]int{}, path...))
			return
		}
		if remain < 0 {
			return
		}

		for i := start; i < len(candidates); i++ {
			path = append(path, candidates[i])
			dfs(i, remain-candidates[i])
			path = path[:len(path)-1]
		}
	}

	dfs(0, target)
	return result
}
