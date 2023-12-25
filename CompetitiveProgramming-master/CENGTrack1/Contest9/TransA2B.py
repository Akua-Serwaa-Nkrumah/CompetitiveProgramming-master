a , b = map(int,input().split())

check = 'YES'
if a == b:
     print("NO")
else:
    res = [b]
    while b > a:
        if b%2 == 1:
            b = (b-1)//10

        else:
            b = b//2

        if b >= a:
            res.append(b)

    res = res[::-1]
   
    if res[0] == a:
        for i in range(len(res)-1):
            if (res[i+1] == 2*(res[i])) or (res[i+1] == (10*res[i] + 1)):
                continue
            else: 
                check = 'NO'
                break

        if check == 'YES':
            print(check)
            print(len(res))
            print(*res)
        else: 
            print('NO')

    else:
        print("NO")