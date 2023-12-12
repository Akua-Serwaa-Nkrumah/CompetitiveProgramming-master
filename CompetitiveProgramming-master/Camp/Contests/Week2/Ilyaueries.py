s = input().strip()
n = len(s)
m = int(input())
queries = []

consecutive_count = [0] * n
for i in range(1, n):
    if s[i] == s[i - 1]:
        consecutive_count[i] = consecutive_count[i - 1] + 1
    else:
        consecutive_count[i] = consecutive_count[i - 1]

for _ in range(m):
    li, ri = map(int, input().split())
    answer = consecutive_count[ri - 1] - consecutive_count[li - 1]
    print(answer)
