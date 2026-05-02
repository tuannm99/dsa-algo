def pow_fast(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        return 1 / pow_fast(x, -n)
    half = pow_fast(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x


def generate_parenthesis(n: int) -> list[str]:
    result: list[str] = []
    path: list[str] = []

    def dfs(opened: int, closed: int) -> None:
        if len(path) == 2 * n:
            result.append("".join(path))
            return
        if opened < n:
            path.append("(")
            dfs(opened + 1, closed)
            path.pop()
        if closed < opened:
            path.append(")")
            dfs(opened, closed + 1)
            path.pop()

    dfs(0, 0)
    return result
