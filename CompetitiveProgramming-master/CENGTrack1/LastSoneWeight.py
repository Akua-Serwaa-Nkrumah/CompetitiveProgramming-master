from heapq import heapify, heappop
class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        while len(stones) > 1:
            heapify(stones)
            heap = []
            for i in range(len(stones)-2):
                heap.append(heappop(stones))

            if stones[-1] - stones[0] > 0:
                heap.append(stones[-1] - stones[0])
            
            stones = heap

        return stones[0] if len(stones) > 0 else 0
        