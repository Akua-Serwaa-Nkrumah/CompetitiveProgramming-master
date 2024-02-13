t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    odds = []
    evens = []

    for i in range(0,len(a),2):
        odds.append(a[i])

    for i in range(1,len(a),2):
        evens.append(a[i])

    if a[0]%2 == 0:
        # for i in odds if all(i%2 == 0):
            print()
    