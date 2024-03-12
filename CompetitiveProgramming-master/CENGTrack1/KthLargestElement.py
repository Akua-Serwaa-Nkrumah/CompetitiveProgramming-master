from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        i = 0
        heapify(nums)

        while i <= (len(nums)-k):
            heappop(nums)
            i += 1
        print(i)
        return nums[0]