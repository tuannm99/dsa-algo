package arrays

func MinSubarrayLen(target int, nums []int) int {
	left := 0
	sum := 0
	best := len(nums) + 1

	for right, v := range nums {
		sum += v
		for sum >= target {
			length := right - left + 1
			if length < best {
				best = length
			}
			sum -= nums[left]
			left++
		}
	}

	if best == len(nums)+1 {
		return 0
	}
	return best
}

func LongestSubstringWithoutRepeat(s string) int {
	last := map[byte]int{}
	left := 0
	best := 0

	for right := 0; right < len(s); right++ {
		if idx, ok := last[s[right]]; ok && idx >= left {
			left = idx + 1
		}
		last[s[right]] = right
		if right-left+1 > best {
			best = right - left + 1
		}
	}

	return best
}

func MaxSumFixedWindow(nums []int, k int) int {
	if k <= 0 || k > len(nums) {
		return 0
	}

	sum := 0
	for i := 0; i < k; i++ {
		sum += nums[i]
	}
	best := sum

	for i := k; i < len(nums); i++ {
		sum += nums[i] - nums[i-k]
		if sum > best {
			best = sum
		}
	}
	return best
}
