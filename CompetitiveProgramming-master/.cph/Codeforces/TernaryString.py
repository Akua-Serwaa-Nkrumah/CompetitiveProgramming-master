def MaxSubstring():
    s = input()

    l, r = 0, 0

    mn = float('inf')
    
    one, two, three = 0, 0, 0
    while l <= r and r < len(s):
        if s[r] == '1':
            one += 1
        elif s[r] == '2':
            two += 1
        else:
            three += 1

        if one != 0 and two != 0 and three != 0:
            mn = min(mn, r-l+1)
            
            if s[l] == '1':
                one -= 1
            elif s[l] == '2':
                two -= 1
            else:
                three -= 1

            l += 1
            continue
        
        r += 1

    return mn if mn != float('inf') else 0

t = int(input())
for _ in range(t):
    print(MaxSubstring())