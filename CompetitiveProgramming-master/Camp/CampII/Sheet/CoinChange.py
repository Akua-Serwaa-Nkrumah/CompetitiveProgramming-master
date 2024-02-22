class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        memo = {}

        def dp(target):
            if target < 0:
                return -1

            if target == 0:
                return 0

            if target not in memo:
                memo[target] = float('inf')
                for coin in coins:
                    if dp(target-coin) >= 0:
                        memo[target] = min(memo[target],dp(target-coin)+1)

            return memo[target] if memo[target] != float('inf') else -1

        return dp(amount)
