package stack

func NextGreaterElements(nums []int) []int {
	result := make([]int, len(nums))
	for i := range result {
		result[i] = -1
	}

	st := []int{}
	for i, v := range nums {
		for len(st) > 0 && nums[st[len(st)-1]] < v {
			idx := st[len(st)-1]
			st = st[:len(st)-1]
			result[idx] = v
		}
		st = append(st, i)
	}
	return result
}

func DailyTemperatures(temps []int) []int {
	result := make([]int, len(temps))
	st := []int{}

	for i, t := range temps {
		for len(st) > 0 && temps[st[len(st)-1]] < t {
			idx := st[len(st)-1]
			st = st[:len(st)-1]
			result[idx] = i - idx
		}
		st = append(st, i)
	}
	return result
}

func LargestRectangleArea(heights []int) int {
	best := 0
	st := []int{}
	extended := append(append([]int{}, heights...), 0)

	for i, h := range extended {
		for len(st) > 0 && extended[st[len(st)-1]] > h {
			height := extended[st[len(st)-1]]
			st = st[:len(st)-1]

			left := -1
			if len(st) > 0 {
				left = st[len(st)-1]
			}
			width := i - left - 1
			area := height * width
			if area > best {
				best = area
			}
		}
		st = append(st, i)
	}
	return best
}
