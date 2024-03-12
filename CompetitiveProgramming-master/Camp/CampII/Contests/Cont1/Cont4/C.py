from collections import defaultdict
n = int(input())

string = input()
amb = list(map(int,input().split()))
diction = defaultdict(int)

stack = []

for i in range(n):
    if stack:
        if stack[-1] == string[i]:
            stack.append(string[i])
            diction[string[i]] += amb[i]
        else:
            if (stack[-1] == 'h' and string[i] == 'a') or ( stack[-1] == 'a' and string[i] == 'r') or ( stack[-1] == 'r' and string[i] == 'd'):
                stack.append(string[i])
                diction[string[i]] += amb[i]
    else:
        stack.append(string[i])
        diction[string[i]] += amb[i]


print(diction)
if len(diction) < 4:
    print(0)

else:
    diction = dict(sorted(diction.items(), key= lambda x:x[1]))

    print(list(diction.values())[0])


