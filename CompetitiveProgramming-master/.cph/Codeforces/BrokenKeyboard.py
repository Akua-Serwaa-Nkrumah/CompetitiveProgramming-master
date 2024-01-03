t = int(input())
for _ in range(t):
    s = input()

    faulty = []
    res = ''  

    for i in s:
        if faulty and i == faulty[-1]:
            faulty.pop()
            res += "".join(faulty)

            continue
        faulty.append(i)

    res += "".join(faulty)
    res = sorted(set(res))
    
    print("".join(res))
    

