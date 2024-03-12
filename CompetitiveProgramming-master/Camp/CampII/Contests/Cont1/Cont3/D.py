from collections import defaultdict

n = int(input())

graph = defaultdict(list)

for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

colors = list(map(int,input().split()))

memo = {}
visited = set()

def dfs(child,visited):
    if child not in graph[i]:
    
        for child in graph[i]:
            if (child,i) not in memo:
                memo[(child,i)] = dfs(child,visited)

            visited.add(child)
            return memo[(child,i)]

check = False
for i in graph:
    for child in graph[i]:
        if dfs(child,visited):
            if not check:
                check = True
                node = i

if check:
    print('Yes')
    print(node)
else:
    
    print('No')