package graph

func DetectCycleDirected(numNodes int, edges [][2]int) bool {
	graph := make([][]int, numNodes)
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], e[1])
	}

	state := make([]int, numNodes)
	var dfs func(int) bool
	dfs = func(node int) bool {
		if state[node] == 1 {
			return true
		}
		if state[node] == 2 {
			return false
		}
		state[node] = 1
		for _, nei := range graph[node] {
			if dfs(nei) {
				return true
			}
		}
		state[node] = 2
		return false
	}

	for i := 0; i < numNodes; i++ {
		if state[i] == 0 && dfs(i) {
			return true
		}
	}
	return false
}

func MultiSourceBFS(grid [][]int, starts [][2]int) [][]int {
	rows, cols := len(grid), len(grid[0])
	dist := make([][]int, rows)
	for r := range dist {
		dist[r] = make([]int, cols)
		for c := range dist[r] {
			dist[r][c] = -1
		}
	}

	queue := make([][2]int, len(starts))
	copy(queue, starts)
	for _, p := range starts {
		dist[p[0]][p[1]] = 0
	}

	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, d := range dirs {
			nr, nc := cur[0]+d[0], cur[1]+d[1]
			if nr < 0 || nr >= rows || nc < 0 || nc >= cols || dist[nr][nc] != -1 {
				continue
			}
			dist[nr][nc] = dist[cur[0]][cur[1]] + 1
			queue = append(queue, [2]int{nr, nc})
		}
	}
	return dist
}
