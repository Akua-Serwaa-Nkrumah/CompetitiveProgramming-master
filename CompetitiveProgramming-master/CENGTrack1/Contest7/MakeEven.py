def solve():
    if int(n)%2 == 0:
        return 0

    if int(n[0])%2 == 0:
        return 1

    for i in range(len(n_list)):
        if (n_list[i])%2 == 1:
            return 2
    
    return -1
    
t = int(input())
for _ in range(t):
    n = input()
    n_list = []
    for i in n:
        n_list.append(i)
    print(solve())
