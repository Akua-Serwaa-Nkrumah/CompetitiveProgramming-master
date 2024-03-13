# Dijkstra'a Algorithm
from heapq import heapify, heappop, heappush
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for i in range(1,n+1):
            adj_list[i].append((0,i))

        for time in times:
            adj_list[time[0]].append((time[2],time[1]))        

        def bfs(start, goal):
            paths = []
            heapify(paths)
            heappush(paths,(0,k))
            visited = set()

            while paths:
                cost, node = heappop(paths)

                if node == goal:
                    return cost

                if node not in visited:
                    visited.add(node)

                    for child in adj_list[node]:
                        heappush(paths,(cost+child[0],child[1]))

            return -1

        ans = []
        for i in range(1,n+1):
            ans.append(bfs(k,i))

        if -1 in ans:
            return -1

        return max(ans)

# Floyd-Warshall's Algorithm
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
        
        for time in times:
            matrix[time[0]-1][time[1]-1] = min(matrix[time[0]-1][time[1]-1],time[2])

        for i in range(n):
            matrix[i-1][i-1] = 0

        for a in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j],matrix[i][a]+matrix[a][j])

        if float('inf') in matrix[k-1]:
            return -1

        return max(matrix[k-1])