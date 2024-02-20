from collections import defaultdict

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        costs = defaultdict(int)

        def minCost(n):

            if n >= len(cost):
                return 0

            if n not in costs:
                costs[n] = cost[n] + min(minCost(n+1), minCost(n+2))

            return costs[n]

        return min(minCost(0),minCost(1))


