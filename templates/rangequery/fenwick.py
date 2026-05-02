class Fenwick:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, index: int) -> int:
        total = 0
        i = index + 1
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def range_sum(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum(right)
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
