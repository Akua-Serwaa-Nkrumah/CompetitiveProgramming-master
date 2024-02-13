from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())

    adj_list = defaultdict(set)

    for _ in range(n):
        a, x = map(int,input().split())
        adj_list[a].add(x)

    adj_list[1] = max(adj_list[1])
    adj_list[2] = min(adj_list[2])

    n = adj_list[2] - adj_list[1]

    for i in adj_list[3]:
        if i in range(adj_list[1],adj_list[2]+1):
            n -= 1

    print(n + 1 if n >= 0 else 0)
