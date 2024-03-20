class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        mx = 0
        memo = {}

        for i in nums:
            mx |= i

        def dp(i,orr):
            if i == len(nums):
                if orr == mx:
                    return 1

                return 0
            
            if (i,orr) not in memo:
                memo[(i,orr)] = dp(i+1,orr) + dp(i+1,orr|nums[i])

            return memo[(i,orr)]

        return dp(0,0)