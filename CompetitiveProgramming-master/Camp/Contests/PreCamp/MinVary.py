t = int(input())
for _ in range(t):
    n = int(input())
    a = ''
    orig = n
    cur = 9
    tot = 0

    while n > 0:
        
        if tot + cur <= orig:
            tot += cur


            a += str(cur)

            if tot == orig:
                a = a[::-1]
                print(int(a))
                break
            

            n -= cur

        cur -= 1

        
      