def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def sieve(n: int) -> list[int]:
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]
