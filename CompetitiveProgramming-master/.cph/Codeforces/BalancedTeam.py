n = int(input())
arr = sorted(list(map(int, input().split())))

max_team = 0
i = 0
j = 0

while i < n:
    while j < n and arr[j] - arr[i] <= 5:
        j += 1
    max_team = max(max_team, j - i)
    i += 1

print(max_team)



