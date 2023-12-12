def Discounts(a,qi):
    return total - a[n-qi]

n = int(input())
a = sorted(list(map(int, input().split())))

m = int(input())
q = list(map(int,input().split()))
total = sum(a)


for i in range(m):
    print(Discounts(a,q[i]))



