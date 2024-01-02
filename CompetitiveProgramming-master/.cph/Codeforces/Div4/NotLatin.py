t = int(input())
for _ in range(t):
    a = []
    for _ in range(3):
        let = input()
        
        a.append(let)
     
    for i in a:
        if "A" not in i:
            print("A")
            break
        elif "B" not in i:
            print("B")
            break
        elif 'C' not in i:
            print('C')
            break

    
    