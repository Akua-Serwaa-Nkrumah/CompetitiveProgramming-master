from heapq import heapify, heappop, heappush
from collections import defaultdict

n,m = map(int,input().split())
adj_list = defaultdict(list) 

heap = [1]
heapify(heap)
res = []
visited = set()

for _ in range(m):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

while heap:
    node = heappop(heap)

    if node not in visited:
        visited.add(node)
        res.append(node)

        for child in adj_list[node]:
            heappush(heap,child)

print(*res)