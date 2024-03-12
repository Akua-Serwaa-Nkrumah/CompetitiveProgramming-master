t = int(input())

for _ in range(t):
    people = list(map(int,input().split()))

    a = people[0]
    cnt = 0
    for i in people:
        if i > a:
            cnt += 1

    print(cnt)

