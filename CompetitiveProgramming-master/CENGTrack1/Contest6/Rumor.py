from collections import defaultdict

n, m = map(int,input().split())
c = list(map(int,input().split()))

adj_list = defaultdict(set)

for _ in range(m):
    x, y = map(int,input().split())
    adj_list[x].add(y)
    adj_list[y].add(x)
    
visited = set()


def dfs(node, visited):
    if len(adj_list[node]) == 0:
        return 
    
    for child in adj_list[node]:
        if child not in visited:
            visited.add(child)
            
            dfs(child,visited)
            
dfs(x, visited)

