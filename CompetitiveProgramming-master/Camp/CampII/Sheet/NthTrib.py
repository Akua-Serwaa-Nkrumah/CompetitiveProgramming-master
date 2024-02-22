# from collections import defaultdict

# class Solution:
#     def tribonacci(self, n: int) -> int:
#         memo = defaultdict(int)

#         def dp(n):
#             if n == 0:
#                 return 0

#             if n < 3:
#                 return 1

#             if n not in memo:
#                 memo[n] = dp(n-1) + dp(n-2) + dp(n-3)

#             return memo[n]
 
#         return dp(n)

class Solution:
    def tribonacci(self, n: int) -> int:
        first, sec, third = 0, 1, 1
        if n < 2:
            return n
        
        if n == 2:
            return 1

        for i in range(n-2):
            ans = first + sec + third
            first = sec
            sec = third
            third = ans

        return ans