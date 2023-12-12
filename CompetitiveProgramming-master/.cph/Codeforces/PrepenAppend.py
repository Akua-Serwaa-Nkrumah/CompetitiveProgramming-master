def PrepApp(n,s):
    left, right = 0, n-1
    while left < right and ((s[left] == '0' and s[right] == '1') or (s[left]== '1' and s[right] == '0')):
            left += 1
            right -= 1
            
    return (right-left+1)
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(PrepApp(n,s))
        

