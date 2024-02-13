t = int(input())

for _ in range(t):
    n = int(input())
    people = []

    for _ in range(n):
        a, b = map(int, input().split())
        people.append((a, b))

    people.sort(key=lambda x: (x[0], x[1]))

    greetings = 0
    prev_end = float('-inf')

    for person in people:
        current_end = person[1]
        if current_end > prev_end:
            greetings += 1
            prev_end = current_end

    print(greetings)