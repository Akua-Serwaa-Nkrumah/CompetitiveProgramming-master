t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    if (len(set(s)) == 2 and s.count(">") == s.count("<")):
        print(len(set(s)) + 1)
    elif len(set(s)) == 1:
        print(len(s)+1)
    else:
        print(abs(s.count("<")-s.count(">")+1))
    