def Destroyer():
    n = int(input( ))
    l = list(map(int, input().split()))
    robot_count  = [0]*(max(l)+1)
    for i in range(n):
        robot_count[l[i]] += 1
    for i in range(len(robot_count)-1):
        if robot_count[i] < robot_count[i+1]:
            return ("NO")
    return ("YES")
    
    
    
t = int(input())
for _ in range(t):
    print(Destroyer())
    