t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a = sorted(a)
    left, right = 0, n-1
    total_cost = 0
    while left < right:
        total_cost += abs(a[left] - a[right])
        left += 1
        right -= 1
    print(total_cost)