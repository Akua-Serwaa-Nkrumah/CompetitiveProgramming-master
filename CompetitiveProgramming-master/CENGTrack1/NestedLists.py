if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records+=[[name,score]]
        scores += [score]
    
    second = sorted(list(set(scores)))[1]
    
    for i,j in sorted(records):
        if j == second:
            print(i)
        
    
