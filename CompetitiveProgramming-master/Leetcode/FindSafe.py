from collections import defaultdict
from queue import deque

class Solution:
    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        queue = deque([])
        adj_list = defaultdict(list)
        outdegree = defaultdict(int)
        arr = []

        for i in range(len(graph)):
            outdegree[i] = len(graph[i])

            if outdegree[i] == 0:
                queue.append(i)

            for j in graph[i]:
                adj_list[j].append(i)

        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                arr.append(node)

                for i in adj_list[node]:
                    outdegree[i] -= 1

                    if outdegree[i] == 0:
                        queue.append(i)

        return sorted(arr)