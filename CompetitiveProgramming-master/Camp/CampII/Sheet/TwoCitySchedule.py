class Solution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        total = 0

        costs.sort(key = lambda x : x[0] - x[1])

        for i in range(len(costs)//2):
            total += costs[i][0]

        for i in range(len(costs)//2 ,len(costs)):
            total += costs[i][1]

        return total