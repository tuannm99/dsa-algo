from collections import deque


def bfs_levels(graph: dict[int, list[int]], start: int) -> list[int]:
    queue = deque([start])
    dist = {start: 0}
    order: list[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph.get(node, []):
            if nei in dist:
                continue
            dist[nei] = dist[node] + 1
            queue.append(nei)

    return order


def dfs_recursive(graph: dict[int, list[int]], start: int) -> list[int]:
    seen: set[int] = set()
    order: list[int] = []

    def dfs(node: int) -> None:
        seen.add(node)
        order.append(node)
        for nei in graph.get(node, []):
            if nei not in seen:
                dfs(nei)

    dfs(start)
    return order


def num_islands(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(row: int, col: int) -> None:
        if row < 0 \
            or row >= rows \
            or col < 0 \
            or col >= cols \
            or grid[row][col] != "1":
            return
        grid[row][col] = "0"
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                count += 1
                dfs(row, col)

    return count
