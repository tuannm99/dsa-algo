package recursion

func Pow(x float64, n int) float64 {
	if n == 0 {
		return 1
	}
	if n < 0 {
		return 1 / Pow(x, -n)
	}
	half := Pow(x, n/2)
	if n%2 == 0 {
		return half * half
	}
	return half * half * x
}

func GenerateParenthesis(n int) []string {
	result := []string{}
	path := make([]byte, 0, 2*n)

	var dfs func(int, int)
	dfs = func(open, close int) {
		if len(path) == 2*n {
			result = append(result, string(path))
			return
		}
		if open < n {
			path = append(path, '(')
			dfs(open+1, close)
			path = path[:len(path)-1]
		}
		if close < open {
			path = append(path, ')')
			dfs(open, close+1)
			path = path[:len(path)-1]
		}
	}

	dfs(0, 0)
	return result
}
