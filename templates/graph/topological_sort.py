from collections import deque


def topo_sort_kahn(num_nodes: int, edges: list[tuple[int, int]]) -> tuple[list[int], bool]:
    graph = [[] for _ in range(num_nodes)]
    indegree = [0] * num_nodes

    for src, dst in edges:
        graph[src].append(dst)
        indegree[dst] += 1

    queue = deque(i for i in range(num_nodes) if indegree[i] == 0)
    order: list[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return order, len(order) == num_nodes
