from collections import Counter, defaultdict

n = int(input())
t = list(map(int,input().split()))

t_dict = defaultdict(list)

t_count= Counter(t)
mn = min(t_count[1],t_count[2],t_count[3])

for i in range(n):
    t_dict[t[i]].append(i+1)

if mn == 0:
    print(0)
else:
    print(mn)
    for i in range(mn):
        ans = [t_dict[j][i] for j in t_dict]
        print(*ans)

