from collections import defaultdict
n, m = map(int,input().split())

s = list(map(int,input().split()))
adj_list = defaultdict(list)

for _ in range(n-1):
    a, b = map(int,input().split())

    adj_list[a].append(b)
    adj_list[b].append(a)

visited = set()
# arr = []
# # tot
# def dfs(node):
#     if len(adj_list[node]) == 0:
#         # arr.append(total)
#     if node not in visited:
#         visited.add(node)

#     dfs()

