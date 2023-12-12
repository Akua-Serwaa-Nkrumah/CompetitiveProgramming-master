n, t = map(int,input().split())
a = list(map(int,input().split()))

l = 0
max_books = 0
window = 0

for r in range(n):
    window += a[r]
    while window > t:
        window -= a[l]
        l += 1
        
    max_books = max(max_books,r-l+1)

print(max_books)
    
    