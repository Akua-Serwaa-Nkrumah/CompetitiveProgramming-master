from heapq import heappush, heappop,heapify
from collections import deque

adj_list = {}
start = 'A'
goal = 'B'
paths = []
heapify(paths)
visited = set()

heappush(paths,(0,start))
while paths:
    cost, node = heappop(paths)

    if node == goal:
        print(cost)
        break

    if node not in visited:
        visited.add(node)

        for child in adj_list[node]:
            heappush(paths,(cost+child[0],child[1]))

print(heappop(paths))