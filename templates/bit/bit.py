def count_bits(n: int) -> list[int]:
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    return result


def single_number(nums: list[int]) -> int:
    value = 0
    for num in nums:
        value ^= num
    return value


def subsets_bitmask(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    total = 1 << len(nums)

    for mask in range(total):
        subset = [nums[i] for i in range(len(nums)) if mask & (1 << i)]
        result.append(subset)

    return result
