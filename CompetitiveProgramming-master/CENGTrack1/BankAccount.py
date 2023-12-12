n = int(input())
if n < 0 :
    n = str(n)
    last = int(n[-1])
    second_last = int(n[-2])
    if last > second_last:
        n = n[:-1]
        print(int(n))
    else:
        n = n[:-2]+n[-1]
        print(int(n))
else:
    print(n)