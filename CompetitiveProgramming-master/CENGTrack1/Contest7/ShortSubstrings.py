t = int(input())
for _ in range(t):
    a = input()
    b = []
    for i in range(0,len(a),2):
        b.append(a[i])

    print(''.join(b))