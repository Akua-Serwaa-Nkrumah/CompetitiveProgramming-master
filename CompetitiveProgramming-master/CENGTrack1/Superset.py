A = set(map(int,input().split()))
n = int(input())
sets = []
for _ in range(n):
    sets.append(set(map(int,input().split())))
    
check = []
for s in sets:
    if A.intersection(s) == s:
        check.append("TRUE")
    else:
        check.append("FALSE")
if "FALSE" in check:
    print("False")
else:
    print("True")