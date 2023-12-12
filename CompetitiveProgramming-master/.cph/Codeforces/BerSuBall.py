def max_pairs(n, boys_skills, m, girls_skills):
    i, j = 0, 0
    pairs = 0
    while i < n and j < m:
        if abs(boys_skills[i] - girls_skills[j]) <= 1:
            pairs += 1
            i += 1
            j += 1
        elif boys_skills[i] < girls_skills[j]:
            i += 1
        else:
            j += 1
    return pairs

n = int(input())
boys_skills = sorted(list(map(int, input().split())))
m = int(input())
girls_skills = sorted(list(map(int, input().split())))

result = max_pairs(n, boys_skills, m, girls_skills)
print(result)
