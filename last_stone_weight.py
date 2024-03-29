class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for val in stones:
            heapq.heappush(heap,-val)
        while len(heap)>1:
            y= heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,y-x)
        if len(heap)==0:
            return 0
        return -heap[0]
