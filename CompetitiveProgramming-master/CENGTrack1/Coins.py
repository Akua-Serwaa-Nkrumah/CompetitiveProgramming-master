t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    if ((n-k)%2 == 0 or n%k == 0 or n%2 == 0) and n>=k:
        print('YES')
    else: 
        print("NO")