def next_greater_elements(nums: list[int]) -> list[int]:
    result = [-1] * len(nums)
    stack: list[int] = []

    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            idx = stack.pop()
            result[idx] = value
        stack.append(i)

    return result


def daily_temperatures(temps: list[int]) -> list[int]:
    result = [0] * len(temps)
    stack: list[int] = []

    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result


def largest_rectangle_area(heights: list[int]) -> int:
    best = 0
    stack: list[int] = []
    extended = heights + [0]

    for i, height in enumerate(extended):
        while stack and extended[stack[-1]] > height:
            popped_height = extended[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, popped_height * width)
        stack.append(i)

    return best
