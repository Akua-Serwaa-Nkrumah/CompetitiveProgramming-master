grandpa = []
print('How many elements do you have? ')
n = int(input())
for i in range(n):
    element = input()
    grandpa.append(element)
    
grandpa = set(grandpa)
if len(grandpa) < 5:
    print('NO')
else:
    print('YES')
