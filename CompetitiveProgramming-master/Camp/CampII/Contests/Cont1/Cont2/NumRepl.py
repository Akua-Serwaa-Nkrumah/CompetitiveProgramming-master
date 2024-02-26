from collections import defaultdict

def solve(a,s):
    diction = defaultdict(int)
    for i in range(n):
        if diction[a[i]] == 0:
            diction[a[i]] = s[i]

        else:
            if  diction[a[i]] != s[i]:
                return 'NO'

    return "YES"
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = input()

    print(solve(a,s))