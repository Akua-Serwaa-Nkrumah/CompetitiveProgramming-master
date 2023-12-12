from collections import Counter
def Special(a):
    count = 0
    a_count = Counter(a)
    mx = max(a)
    for i in range(n):
        total = a[i]
        for j in range(i+1,n):
            total += a[j]
            if total in a_count:
                count += a_count[total]
                a_count[total] = 0
              
            if total > mx:
                break           
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(Special(a))