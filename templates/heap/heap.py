import heapq


def kth_largest(nums: list[int], k: int) -> int:
    heap: list[int] = []
    for value in nums:
        heapq.heappush(heap, value)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
