package greedy

import "sort"

func CanJump(nums []int) bool {
	farthest := 0
	for i, v := range nums {
		if i > farthest {
			return false
		}
		if i+v > farthest {
			farthest = i + v
		}
	}
	return true
}

func JumpGameII(nums []int) int {
	steps, left, right := 0, 0, 0
	for right < len(nums)-1 {
		farthest := right
		for i := left; i <= right; i++ {
			if i+nums[i] > farthest {
				farthest = i + nums[i]
			}
		}
		left = right + 1
		right = farthest
		steps++
	}
	return steps
}

func CanCompleteCircuit(gas, cost []int) int {
	total, tank, start := 0, 0, 0
	for i := range gas {
		diff := gas[i] - cost[i]
		total += diff
		tank += diff
		if tank < 0 {
			start = i + 1
			tank = 0
		}
	}
	if total < 0 {
		return -1
	}
	return start
}

func EraseOverlapIntervals(intervals [][2]int) int {
	if len(intervals) == 0 {
		return 0
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})
	removed := 0
	end := intervals[0][1]
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] < end {
			removed++
			continue
		}
		end = intervals[i][1]
	}
	return removed
}
