n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

good_pairs = 0
i = 0

while i < n:
    for j in range(i+1,n):
        if (a[i]+a[j]) > (b[i] + b[j]):
            good_pairs+= 1
            
print(good_pairs)