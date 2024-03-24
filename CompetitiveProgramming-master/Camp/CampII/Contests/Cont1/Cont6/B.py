t = int(input())
for _ in range(t):
    n = int(input())
    a = ''
    orig = n
    cur = 9
    total = 0

    while n > 0:
        
        if total + cur <= orig:
            total += cur

            a += str(cur)

            if total == orig:
                a = a[::-1]
                print(int(a))
                break
            
            n -= cur

        cur -= 1

        
      