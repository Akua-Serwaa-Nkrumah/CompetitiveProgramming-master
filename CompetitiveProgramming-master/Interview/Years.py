def solution(years):
    time = 0
    for i in range(len(years)-1):
        if years[i] > years[i+1]:
            time += 2
        elif years[i] < years[i+1]:
            time += 1
    return time