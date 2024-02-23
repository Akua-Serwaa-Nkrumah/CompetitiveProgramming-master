from collections import defaultdict

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        memo = defaultdict(int)

        def dp(cur):
            if cur == target:
                return 1

            if cur not in memo:
                for num in nums:
                    if cur + num <= target:
                        memo[cur] = memo[cur] + dp(cur + num)

            return memo[cur]

        return dp(0)
