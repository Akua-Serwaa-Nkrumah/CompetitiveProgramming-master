from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        heapify(self.nums)
        for i in range(len(self.nums)-self.k):
            heappop(self.nums)
        return self.nums[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)