class NumArray:

    def __init__(self, nums):
        self.nums = nums 
        self.prefix_sum = [self.nums[0]]*(len(self.nums))
        for i in range(1,len(self.nums)):
            self.prefix_sum[i] = self.prefix_sum[i-1] + self.nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return (self.prefix_sum[right] - self.prefix_sum[left-1]) if left!= 0 else self.prefix_sum[right] 
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)