package graph

import "container/heap"

type Edge struct {
	To     int
	Weight int
}

type state struct {
	node int
	dist int
}

type minHeap []state

func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool { return h[i].dist < h[j].dist }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x any)        { *h = append(*h, x.(state)) }
func (h *minHeap) Pop() any          { old := *h; x := old[len(old)-1]; *h = old[:len(old)-1]; return x }

func Dijkstra(graph map[int][]Edge, start int) map[int]int {
	const inf = int(^uint(0) >> 1)

	dist := map[int]int{}
	for node := range graph {
		dist[node] = inf
	}
	dist[start] = 0

	pq := &minHeap{{node: start, dist: 0}}
	heap.Init(pq)

	for pq.Len() > 0 {
		cur := heap.Pop(pq).(state)
		if cur.dist != dist[cur.node] {
			continue
		}

		for _, edge := range graph[cur.node] {
			nextDist := cur.dist + edge.Weight
			old, ok := dist[edge.To]
			if !ok || nextDist < old {
				dist[edge.To] = nextDist
				heap.Push(pq, state{node: edge.To, dist: nextDist})
			}
		}
	}

	return dist
}
