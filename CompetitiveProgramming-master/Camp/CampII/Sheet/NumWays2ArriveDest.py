from heapq import heapify, heappop, heappush
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj_list = defaultdict(list)
        paths = [(0,0)]
        heapify(paths)
        dijkstra = {}
        memo = {}
        
        for road in roads:
            adj_list[road[0]].append((road[2],road[1]))
            adj_list[road[1]].append((road[2],road[0]))

        while paths:
            cost,node = heappop(paths)

            if node not in dijkstra:
                dijkstra[node] = cost

                for child in adj_list[node]:
                    heappush(paths,(cost+child[0],child[1]))

        def dp(node,cost):
            if node == 0:
                return 1

            if node not in memo:
                cnt = 0
                for child in adj_list[node]:
                    if cost + child[0] + dijkstra[child[1]] == dijkstra[n-1]:
                        cnt += dp(child[1],cost+child[0])

                memo[node] = cnt

            return memo[node]

        return dp(n-1,0)%(1000000007)