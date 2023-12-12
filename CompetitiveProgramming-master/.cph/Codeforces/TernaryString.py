def MaxSubstring():
    s = input()

    min_length = 0
    if len(set(s)) < 3:
        return (0)
    elif len(set(s)) == 3:
        i = 0
        j = len(s)-1
        while i < j:
            if len(set(s[i:j])) == 3:
                min_length = min(min_length,len(s[i:j]))  
                i += 1
                j -= 1
            i+=1
    return (min_length)

t = int(input())
for _ in range(t):
    print(MaxSubstring())