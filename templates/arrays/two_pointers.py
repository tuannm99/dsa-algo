def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int, bool]:
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return left, right, True
        if current < target:
            left += 1
        else:
            right -= 1
    return -1, -1, False


def remove_duplicates_sorted(nums: list[int]) -> int:
    if not nums:
        return 0

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        width = right - left
        area = width * min(height[left], height[right])
        best = max(best, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best
