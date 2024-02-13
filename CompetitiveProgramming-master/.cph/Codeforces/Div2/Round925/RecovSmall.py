t = int(input())
for _ in range(t):
    n = int(input())
    s = ''
    if n > 27:
        for i in range(n//26):
            s += 'z'

        if len(s) == 3:
            print(s[:-1])
        else:
            if len(s) == 2:
                n = n%26
                rem = chr(n+64)
                rem = rem.lower()
                s += rem
                print(s[::-1])
            else:
                rem = 'a'
                rem += chr(64+n-1)
                rem = rem.lower()

                s =rem + s
                print(s)

    else:
        rem = 'aa'
        n -= 2
        rem += chr(n+64)
        rem = rem.lower()
        print(rem)


    


