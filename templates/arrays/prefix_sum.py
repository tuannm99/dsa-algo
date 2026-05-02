def build_prefix_sum(nums: list[int]) -> list[int]:
    prefix = [0] * (len(nums) + 1)
    for i, value in enumerate(nums):
        prefix[i + 1] = prefix[i] + value
    return prefix


def range_sum(prefix: list[int], left: int, right: int) -> int:
    return prefix[right + 1] - prefix[left]


def count_subarrays_with_sum(nums: list[int], target: int) -> int:
    count = 0
    total = 0
    freq = {0: 1}

    for value in nums:
        total += value
        count += freq.get(total - target, 0)
        freq[total] = freq.get(total, 0) + 1

    return count
