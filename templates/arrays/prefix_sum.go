package arrays

func BuildPrefixSum(nums []int) []int {
	prefix := make([]int, len(nums)+1)
	for i, v := range nums {
		prefix[i+1] = prefix[i] + v
	}
	return prefix
}

func RangeSum(prefix []int, left, right int) int {
	return prefix[right+1] - prefix[left]
}

func CountSubarraysWithSum(nums []int, target int) int {
	count := 0
	sum := 0
	freq := map[int]int{0: 1}

	for _, v := range nums {
		sum += v
		count += freq[sum-target]
		freq[sum]++
	}

	return count
}
