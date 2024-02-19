t = int(input())
for _ in range(t):
    x = int(input())

    for i in range(1,10000000):
        if (i & x > 0) and (i ^ x > 0):
            print(i)
            break
