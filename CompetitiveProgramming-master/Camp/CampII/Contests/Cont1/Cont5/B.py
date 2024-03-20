t = int(input())

for _ in range(t):
    n, k = map(int,input().split())

    a = list(map(int,input().split()))
    a_sort = sorted(a)
    
    if k > 1 or a_sort == a:
        print('YES')
    else:
        print('NO')

        
                
