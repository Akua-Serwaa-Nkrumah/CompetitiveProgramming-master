l, r = map(int,input().split())

if r != l:
    print(r ^ (r-1))
else:
    print(0)