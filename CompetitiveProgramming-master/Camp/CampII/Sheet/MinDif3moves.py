class Solution:
    def minDifference(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        
        if n < 4:
            return 0

        first = nums[n-4] - nums[0]
        second = nums[n-1] - nums[3]
        third = nums[n-3] - nums[1]
        fourth = nums[n-2] - nums[2]

        return (min(first,second,third,fourth))
