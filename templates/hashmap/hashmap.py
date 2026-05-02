def two_sum(nums: list[int], target: int) -> tuple[int, int, bool]:
    index: dict[int, int] = {}
    for i, value in enumerate(nums):
        if target - value in index:
            return index[target - value], i, True
        index[value] = i
    return -1, -1, False


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq: dict[int, int] = {}
    for value in nums:
        freq[value] = freq.get(value, 0) + 1

    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for value, count in freq.items():
        buckets[count].append(value)

    result: list[int] = []
    for count in range(len(buckets) - 1, -1, -1):
        result.extend(buckets[count])
        if len(result) >= k:
            return result[:k]
    return result


def longest_consecutive(nums: list[int]) -> int:
    seen = set(nums)
    best = 0

    for value in nums:
        if value - 1 in seen:
            continue
        length = 1
        while value + length in seen:
            length += 1
        best = max(best, length)

    return best
