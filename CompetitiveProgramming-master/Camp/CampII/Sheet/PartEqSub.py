class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        target = sum(nums)//2
        memo = {}

        def dp(idx,cur):
            if idx == len(nums):
                return cur == target

            if (idx,cur) not in memo:
               
                memo[(idx,cur)] = dp(idx+1,cur+nums[idx]) or dp(idx+1,cur)

            return memo[(idx,cur)]

        return sum(nums)%2 == 0 and dp(0,0)