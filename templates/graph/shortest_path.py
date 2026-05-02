import heapq
from dataclasses import dataclass


@dataclass(frozen=True)
class Edge:
    to: int
    weight: int


def dijkstra(graph: dict[int, list[Edge]], start: int) -> dict[int, int]:
    inf = float("inf")
    dist = {node: inf for node in graph}
    dist[start] = 0
    pq: list[tuple[int, int]] = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)
        if current_dist != dist[node]:
            continue

        for edge in graph.get(node, []):
            next_dist = current_dist + edge.weight
            if next_dist < dist.get(edge.to, inf):
                dist[edge.to] = next_dist
                heapq.heappush(pq, (next_dist, edge.to))

    return dist
