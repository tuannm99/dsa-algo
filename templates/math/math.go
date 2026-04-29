package mathx

func GCD(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func LCM(a, b int) int {
	return a / GCD(a, b) * b
}

func Sieve(n int) []int {
	if n < 2 {
		return nil
	}
	isPrime := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		isPrime[i] = true
	}
	for i := 2; i*i <= n; i++ {
		if !isPrime[i] {
			continue
		}
		for j := i * i; j <= n; j += i {
			isPrime[j] = false
		}
	}
	primes := []int{}
	for i := 2; i <= n; i++ {
		if isPrime[i] {
			primes = append(primes, i)
		}
	}
	return primes
}
