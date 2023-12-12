n = int(input()) 
for _ in range(n):
    first = list(map(int,input().split()))
    second = list(map(int,input().split()))
    first = sorted(first)
    second = sorted(second)
    square = []
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                square.append(first[i])
                
    square = sorted(square)
    if square != []:
        if (first[0] + second[0]) == square[-1] and first[0] != 0 and second[0] != 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
        
