t = int(input())
for _ in range(t):
    n = int(input())
    lang = input()

    a = []
    C = ['b','c','d']
    V = ['a','e']
    
    for i in range(n-1):
        if lang[i] in C:
            if lang[i+1] in C:
                a.append(lang[i])
                a.append('.')
            else: 
                if a and a[-1] in V:
                   a.append('.')
                   a.append(lang[i])
                else:
                    a.append(lang[i])

        else:
            a.append(lang[i])

    a.append(lang[n-1])
    print(''.join(a))

