package hashmap

func TwoSum(nums []int, target int) (int, int, bool) {
	index := map[int]int{}
	for i, v := range nums {
		if j, ok := index[target-v]; ok {
			return j, i, true
		}
		index[v] = i
	}
	return -1, -1, false
}

func TopKFrequent(nums []int, k int) []int {
	freq := map[int]int{}
	for _, v := range nums {
		freq[v]++
	}

	buckets := make([][]int, len(nums)+1)
	for v, count := range freq {
		buckets[count] = append(buckets[count], v)
	}

	result := make([]int, 0, k)
	for count := len(buckets) - 1; count >= 0 && len(result) < k; count-- {
		result = append(result, buckets[count]...)
	}
	if len(result) > k {
		result = result[:k]
	}
	return result
}

func LongestConsecutive(nums []int) int {
	seen := map[int]bool{}
	for _, v := range nums {
		seen[v] = true
	}

	best := 0
	for _, v := range nums {
		if seen[v-1] {
			continue
		}
		length := 1
		for seen[v+length] {
			length++
		}
		if length > best {
			best = length
		}
	}
	return best
}
