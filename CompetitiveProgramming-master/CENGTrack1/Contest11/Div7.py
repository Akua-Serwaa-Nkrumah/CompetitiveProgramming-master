t = int(input())
for _ in range(t):
    n = int(input())

    if n%7 == 0:
        print(n)

    else:
        n = n - n%10 
        n += 7 - n%7
        print(n)
