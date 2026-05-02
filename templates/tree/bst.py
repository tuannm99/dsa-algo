from .tree import TreeNode


def is_valid_bst(root: TreeNode | None) -> bool:
    def dfs(node: TreeNode | None, low: int | None, high: int | None) -> bool:
        if node is None:
            return True
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, None, None)


def kth_smallest(root: TreeNode | None, k: int) -> int:
    stack: list[TreeNode] = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val
        current = current.right

    return -1
