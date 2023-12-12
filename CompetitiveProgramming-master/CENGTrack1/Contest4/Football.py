s = input()
def football(s):
    l,r = 0, 0
    count = 0
    while r < len(s):
        if s[l] == s[r]:
            count += 1
            r += 1
            
        else:
            count = 0
            l = r
            
        if count >= 7:
            return 'YES'
            
               
    return "NO"

print(football(s))

    