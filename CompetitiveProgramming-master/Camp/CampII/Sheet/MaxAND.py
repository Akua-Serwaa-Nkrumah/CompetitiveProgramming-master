from collections import defaultdict
t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    binary =[]
    for x in nums:
        y=bin(x)
        binary.append(y[2:].zfill(31))  
    
    # print(binary)
    zipp = binary.copy()
    zippp = list(zip(*zipp))
    count = defaultdict(int)
    for i in range(len(zippp)) :
        count[i] += zippp[i].count('0')
    
    for i in range(len(zippp)):
        if count[i] <= k:
            zippp[i] = '1'*n
            k-=count[i]
    
    ans = list(zip(*zippp))
    
    for i in range(len(ans)):
        ans[i] = int(''.join(ans[i]),2)

    res = ans[0]

    for i in ans[1:]:
        res = res & i

    print(res)
