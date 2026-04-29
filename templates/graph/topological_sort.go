package graph

func TopoSortKahn(numNodes int, edges [][2]int) ([]int, bool) {
	graph := make([][]int, numNodes)
	indegree := make([]int, numNodes)

	for _, e := range edges {
		from, to := e[0], e[1]
		graph[from] = append(graph[from], to)
		indegree[to]++
	}

	queue := []int{}
	for i := 0; i < numNodes; i++ {
		if indegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	order := make([]int, 0, numNodes)
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		order = append(order, node)

		for _, nei := range graph[node] {
			indegree[nei]--
			if indegree[nei] == 0 {
				queue = append(queue, nei)
			}
		}
	}

	return order, len(order) == numNodes
}
