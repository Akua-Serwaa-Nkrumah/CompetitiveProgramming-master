from collections import defaultdict

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = defaultdict(int)
        mx = -1

        def dp(n):
            if n < 2:
                return n

            if n not in memo:
                if n%2 == 0:
                    memo[n] = dp(n//2)
                else:
                    memo[n] = dp((n-1)//2) + dp((n+1)//2)

            return memo[n]

        for i in range(n+1):
            mx = max(mx,dp(i))
        
        return mx
        