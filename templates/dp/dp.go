package dp

func ClimbStairs(n int) int {
	if n <= 2 {
		return n
	}
	a, b := 1, 2
	for i := 3; i <= n; i++ {
		a, b = b, a+b
	}
	return b
}

func CoinChange(coins []int, amount int) int {
	const inf = int(^uint(0) >> 1)
	dp := make([]int, amount+1)
	for i := 1; i <= amount; i++ {
		dp[i] = inf
	}

	for _, coin := range coins {
		for x := coin; x <= amount; x++ {
			if dp[x-coin]+1 < dp[x] {
				dp[x] = dp[x-coin] + 1
			}
		}
	}

	if dp[amount] == inf {
		return -1
	}
	return dp[amount]
}

func LengthOfLIS(nums []int) int {
	tails := []int{}
	for _, num := range nums {
		left, right := 0, len(tails)
		for left < right {
			mid := left + (right-left)/2
			if tails[mid] < num {
				left = mid + 1
			} else {
				right = mid
			}
		}
		if left == len(tails) {
			tails = append(tails, num)
		} else {
			tails[left] = num
		}
	}
	return len(tails)
}

func Knapsack01(weights, values []int, capacity int) int {
	dp := make([]int, capacity+1)
	for i := 0; i < len(weights); i++ {
		for cap := capacity; cap >= weights[i]; cap-- {
			candidate := dp[cap-weights[i]] + values[i]
			if candidate > dp[cap] {
				dp[cap] = candidate
			}
		}
	}
	return dp[capacity]
}
