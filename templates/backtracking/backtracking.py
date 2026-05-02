def subsets(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def dfs(start: int) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return result


def permutations(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(nums)

    def dfs() -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i, value in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(value)
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return result


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def dfs(start: int, remain: int) -> None:
        if remain == 0:
            result.append(path[:])
            return
        if remain < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i, remain - candidates[i])
            path.pop()

    dfs(0, target)
    return result
