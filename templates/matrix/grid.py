from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    row: int
    col: int


DIRS4 = ((1, 0), (-1, 0), (0, 1), (0, -1))


def flood_fill(grid: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    original = grid[sr][sc]
    if original == color:
        return grid

    def dfs(row: int, col: int) -> None:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != original:
            return
        grid[row][col] = color
        for dr, dc in DIRS4:
            dfs(row + dr, col + dc)

    dfs(sr, sc)
    return grid


def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1

    dirs8 = (
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1),
    )
    queue = deque([Point(0, 0)])
    grid[0][0] = 1

    while queue:
        current = queue.popleft()
        dist = grid[current.row][current.col]

        if current.row == len(grid) - 1 and current.col == len(grid[0]) - 1:
            return dist

        for dr, dc in dirs8:
            nr, nc = current.row + dr, current.col + dc
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] != 0:
                continue
            grid[nr][nc] = dist + 1
            queue.append(Point(nr, nc))

    return -1
