package graph

func BFSLevels(graph map[int][]int, start int) []int {
	queue := []int{start}
	dist := map[int]int{start: 0}
	order := []int{}

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		order = append(order, node)

		for _, nei := range graph[node] {
			if _, seen := dist[nei]; seen {
				continue
			}
			dist[nei] = dist[node] + 1
			queue = append(queue, nei)
		}
	}
	return order
}

func DFSRecursive(graph map[int][]int, start int) []int {
	seen := map[int]bool{}
	order := []int{}

	var dfs func(int)
	dfs = func(node int) {
		seen[node] = true
		order = append(order, node)
		for _, nei := range graph[node] {
			if !seen[nei] {
				dfs(nei)
			}
		}
	}

	dfs(start)
	return order
}

func NumIslands(grid [][]byte) int {
	rows, cols := len(grid), len(grid[0])
	count := 0

	var dfs func(int, int)
	dfs = func(r, c int) {
		if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1' {
			return
		}
		grid[r][c] = '0'
		dfs(r+1, c)
		dfs(r-1, c)
		dfs(r, c+1)
		dfs(r, c-1)
	}

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] == '1' {
				count++
				dfs(r, c)
			}
		}
	}

	return count
}
