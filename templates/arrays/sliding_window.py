def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    total = 0
    best = len(nums) + 1

    for right, value in enumerate(nums):
        total += value
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if best == len(nums) + 1 else best


def longest_substring_without_repeat(text: str) -> int:
    last: dict[str, int] = {}
    left = 0
    best = 0

    for right, ch in enumerate(text):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)

    return best


def max_sum_fixed_window(nums: list[int], k: int) -> int:
    if k <= 0 or k > len(nums):
        return 0

    total = sum(nums[:k])
    best = total

    for i in range(k, len(nums)):
        total += nums[i] - nums[i - k]
        best = max(best, total)

    return best
