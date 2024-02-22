# from collections import defaultdict

# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         memo = defaultdict(int)

#         def dp(n):

#             if n >= len(nums):
#                 return 0

#             if n not in memo:
#                 memo[n] = max(nums[n] + dp(n+2),dp(n+1))

#             return memo[n]

#         return dp(0)

class Solution:
    def rob(self, nums: list[int]) -> int:
        first,sec = 0,0

        for i in range(len(nums)):
            ans = max(first+nums[i],sec)
            first = sec
            sec = ans

        return ans