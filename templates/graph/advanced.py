from collections import deque


def detect_cycle_directed(num_nodes: int, edges: list[tuple[int, int]]) -> bool:
    graph = [[] for _ in range(num_nodes)]
    for src, dst in edges:
        graph[src].append(dst)

    state = [0] * num_nodes

    def dfs(node: int) -> bool:
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        state[node] = 1
        for nei in graph[node]:
            if dfs(nei):
                return True
        state[node] = 2
        return False

    return any(state[i] == 0 and dfs(i) for i in range(num_nodes))


def multi_source_bfs(grid: list[list[int]], starts: list[tuple[int, int]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque(starts)

    for row, col in starts:
        dist[row][col] = 0

    for row, col in queue:
        dist[row][col] = 0

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[row][col] + 1
            queue.append((nr, nc))

    return dist
