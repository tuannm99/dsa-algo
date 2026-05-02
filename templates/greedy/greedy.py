def can_jump(nums: list[int]) -> bool:
    farthest = 0
    for i, value in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + value)
    return True


def jump_game_ii(nums: list[int]) -> int:
    steps = left = right = 0
    while right < len(nums) - 1:
        farthest = right
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        steps += 1
    return steps


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    total = tank = start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0
    return -1 if total < 0 else start


def erase_overlap_intervals(intervals: list[tuple[int, int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda item: item[1])
    removed = 0
    end = intervals[0][1]
    for start, finish in intervals[1:]:
        if start < end:
            removed += 1
        else:
            end = finish
    return removed
