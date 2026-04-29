package sortx

import "math/rand"

func QuickSort(nums []int) {
	var sort func(int, int)
	sort = func(left, right int) {
		if left >= right {
			return
		}
		pivot := partition(nums, left, right)
		sort(left, pivot-1)
		sort(pivot+1, right)
	}
	sort(0, len(nums)-1)
}

func QuickSelect(nums []int, k int) int {
	left, right := 0, len(nums)-1
	target := k
	for left <= right {
		pivot := partition(nums, left, right)
		switch {
		case pivot == target:
			return nums[pivot]
		case pivot < target:
			left = pivot + 1
		default:
			right = pivot - 1
		}
	}
	return -1
}

func partition(nums []int, left, right int) int {
	pivotIndex := left + rand.Intn(right-left+1)
	nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
	pivot := nums[right]
	store := left
	for i := left; i < right; i++ {
		if nums[i] < pivot {
			nums[store], nums[i] = nums[i], nums[store]
			store++
		}
	}
	nums[store], nums[right] = nums[right], nums[store]
	return store
}
