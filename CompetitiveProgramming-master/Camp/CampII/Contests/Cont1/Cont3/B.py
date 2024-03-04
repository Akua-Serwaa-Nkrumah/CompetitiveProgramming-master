t = int(input())

for _ in range(t):
    n = int(input())

    bin_str = list(bin(n)[2:])

    bin_str[0] = '0'
    for i in range(1,len(bin_str)):
        bin_str[i] = '1'

    print(int(''.join(bin_str),2))
