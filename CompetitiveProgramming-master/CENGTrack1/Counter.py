from collections import Counter
X = int(input())
shoe = Counter(map(int, input().split()))
N = int(input())

total_earn = 0
for i in range(N):
    size, price = map(int, input().split())
    if shoe[size]: 
        shoe[size] -= 1
        total_earn += price
print(total_earn)
