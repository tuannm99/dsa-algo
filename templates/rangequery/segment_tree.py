class SegmentTree:
    def __init__(self, nums: list[int]) -> None:
        self.n = len(nums)
        self.tree = [0] * (4 * max(1, self.n))
        if nums:
            self._build(1, 0, self.n - 1, nums)

    def _build(self, node: int, left: int, right: int, nums: list[int]) -> None:
        if left == right:
            self.tree[node] = nums[left]
            return
        mid = left + (right - left) // 2
        self._build(node * 2, left, mid, nums)
        self._build(node * 2 + 1, mid + 1, right, nums)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, index: int, value: int) -> None:
        self._update(1, 0, self.n - 1, index, value)

    def _update(self, node: int, left: int, right: int, index: int, value: int) -> None:
        if left == right:
            self.tree[node] = value
            return
        mid = left + (right - left) // 2
        if index <= mid:
            self._update(node * 2, left, mid, index, value)
        else:
            self._update(node * 2 + 1, mid + 1, right, index, value)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, query_left: int, query_right: int) -> int:
        return self._query(1, 0, self.n - 1, query_left, query_right)

    def _query(self, node: int, left: int, right: int, query_left: int, query_right: int) -> int:
        if query_left <= left and right <= query_right:
            return self.tree[node]
        if right < query_left or query_right < left:
            return 0
        mid = left + (right - left) // 2
        return self._query(node * 2, left, mid, query_left, query_right) + self._query(
            node * 2 + 1, mid + 1, right, query_left, query_right
        )
