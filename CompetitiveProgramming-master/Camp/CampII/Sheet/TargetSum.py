class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}

        def dp(idx,cur):
            if idx == len(nums):
                if cur == target:
                    return 1
                else:
                    return 0

            if (idx,cur) not in memo:
                memo[(idx,cur)] = dp(idx+1,cur+nums[idx]) + dp(idx+1,cur-nums[idx])

            return memo[(idx,cur)]
            
        return dp(0,0)