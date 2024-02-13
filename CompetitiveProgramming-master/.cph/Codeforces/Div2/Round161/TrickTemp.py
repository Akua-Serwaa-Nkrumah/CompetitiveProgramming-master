def solve():
    for i in range(n):
        if a[i].lower() and b[i].lower():
            if a[i] != c[i] and b[i] != c[i]:
                return "YES"
            
        else:
            if a[i].lower()== c[i].lower() and b[i] == c[i].lower():
                return "YES"
            
    return 'NO'
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    c = input()

    print(solve())