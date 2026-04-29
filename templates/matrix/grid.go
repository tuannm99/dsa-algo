package matrix

type Point struct {
	Row int
	Col int
}

var dirs4 = [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

func FloodFill(grid [][]int, sr, sc, color int) [][]int {
	orig := grid[sr][sc]
	if orig == color {
		return grid
	}

	var dfs func(int, int)
	dfs = func(r, c int) {
		if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) || grid[r][c] != orig {
			return
		}
		grid[r][c] = color
		for _, d := range dirs4 {
			dfs(r+d[0], c+d[1])
		}
	}

	dfs(sr, sc)
	return grid
}

func ShortestPathBinaryMatrix(grid [][]int) int {
	if grid[0][0] == 1 || grid[len(grid)-1][len(grid[0])-1] == 1 {
		return -1
	}

	dirs8 := [][2]int{
		{1, 0},
		{-1, 0},
		{0, 1},
		{0, -1},
		{1, 1},
		{1, -1},
		{-1, 1},
		{-1, -1},
	}

	queue := []Point{{0, 0}}
	grid[0][0] = 1

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		dist := grid[cur.Row][cur.Col]

		if cur.Row == len(grid)-1 && cur.Col == len(grid[0])-1 {
			return dist
		}

		for _, d := range dirs8 {
			nr, nc := cur.Row+d[0], cur.Col+d[1]
			if nr < 0 || nr >= len(grid) || nc < 0 || nc >= len(grid[0]) || grid[nr][nc] != 0 {
				continue
			}
			grid[nr][nc] = dist + 1
			queue = append(queue, Point{nr, nc})
		}
	}

	return -1
}
