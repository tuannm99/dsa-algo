import random


def quick_sort(nums: list[int]) -> None:
    def sort(left: int, right: int) -> None:
        if left >= right:
            return
        pivot = _partition(nums, left, right)
        sort(left, pivot - 1)
        sort(pivot + 1, right)

    sort(0, len(nums) - 1)


def quick_select(nums: list[int], k: int) -> int:
    left, right = 0, len(nums) - 1
    target = k

    while left <= right:
        pivot = _partition(nums, left, right)
        if pivot == target:
            return nums[pivot]
        if pivot < target:
            left = pivot + 1
        else:
            right = pivot - 1

    return -1


def _partition(nums: list[int], left: int, right: int) -> int:
    pivot_index = random.randint(left, right)
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    pivot = nums[right]
    store = left

    for i in range(left, right):
        if nums[i] < pivot:
            nums[store], nums[i] = nums[i], nums[store]
            store += 1

    nums[store], nums[right] = nums[right], nums[store]
    return store
