t = int(input())
for _ in range(t):
    n = int(input())

    binary = bin(n)[2:]
    binary = '0'*(31-len(binary)) + binary
    
    ans = ['0']*len(binary)
    for i in range(len(binary)-1,-1,-1):
        if binary[i] == '1':
            ans[i] = '1'
            break

    if int(''.join(ans),2) ^ n != 0:
        print(int(''.join(ans),2))

    else:
        for i in range(len(binary)-1,-1,-1):
            if binary[i] == '0':
                ans[i] = '1'
                break
        
        print((int(''.join(ans),2)))


