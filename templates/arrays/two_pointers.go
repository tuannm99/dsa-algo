package arrays

func TwoSumSorted(nums []int, target int) (int, int, bool) {
	left, right := 0, len(nums)-1
	for left < right {
		sum := nums[left] + nums[right]
		switch {
		case sum == target:
			return left, right, true
		case sum < target:
			left++
		default:
			right--
		}
	}
	return -1, -1, false
}

func RemoveDuplicatesSorted(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	write := 1
	for read := 1; read < len(nums); read++ {
		if nums[read] != nums[read-1] {
			nums[write] = nums[read]
			write++
		}
	}
	return write
}

func MaxArea(height []int) int {
	left, right := 0, len(height)-1
	best := 0

	for left < right {
		width := right - left
		h := height[left]
		if height[right] < h {
			h = height[right]
		}
		area := width * h
		if area > best {
			best = area
		}

		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return best
}
