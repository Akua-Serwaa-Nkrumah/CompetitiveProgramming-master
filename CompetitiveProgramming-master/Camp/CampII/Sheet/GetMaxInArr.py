# from collections import defaultdict

# class Solution:
#     def getMaximumGenerated(self, n: int) -> int:
#         memo = defaultdict(int)
#         mx = -1

#         def dp(n):
#             if n < 2:
#                 return n

#             if n not in memo:
#                 if n%2 == 0:
#                     memo[n] = dp(n//2)
#                 else:
#                     memo[n] = dp((n-1)//2) + dp((n+1)//2)

#             return memo[n]

#         for i in range(n+1):
#             mx = max(mx,dp(i))
        
#         return mx
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n < 2:
            return n

        dp = [0]*(n+1)
        dp[1] = 1
        mx = 0

        for i in range(2,n+1):
            if i%2 == 0:
                dp[i] = dp[i//2]

            else:
                dp[i] = dp[(i-1)//2] + dp[(i+1)//2]

            mx = max(mx,dp[i])
        
        return mx
        
        