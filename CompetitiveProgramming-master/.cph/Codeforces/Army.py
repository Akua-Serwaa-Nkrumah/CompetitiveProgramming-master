n = int(input())
d = list(map(int, input().split()))
a, b = map(int,input().split())

d_sum = [0]*(n)
for i in range(1,n):
    d_sum[i] = d_sum[i-1] + d[i-1]
    
print(d_sum[b-1]-d_sum[a-1])
