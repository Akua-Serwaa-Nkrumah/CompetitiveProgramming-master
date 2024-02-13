t = int(input())

for _ in range(t):
    n = int(input())
    glasses = list(map(int, input().split()))
    check = "NO"
    
    odd_sum = 0
    even_sum = 0

    l, r = 0, 1
    while r < n:
        even_sum += glasses[r]
        odd_sum += glasses[l]

        if even_sum == odd_sum:
            check = "YES"
            break

        l += 2
        r += 2

   


    
    