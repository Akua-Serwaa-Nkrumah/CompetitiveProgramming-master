def Dangerous(s):
    l, r = 0, 1
    while l < r and r < len(s):
            if s[l] == s[r]:
                if r - l + 1 >= 7:
                    return "YES"
                r += 1
            else: 
                l = r
                r += 1
        
               
    return "NO"

s = input()
print(Dangerous(s))
