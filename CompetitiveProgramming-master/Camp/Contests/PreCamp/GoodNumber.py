from collections import Counter

n, k = map(int,input().split())
count = 0
for _ in range(n):
    i = sorted(list(input()))
    for j in range(len(i)):
        i[j] = int(i[j])
        
    i_count = Counter(i)
    print(i_count)
    

    if max(i_count) == k and len(i_count) == k+1:
        count += 1

print(count)