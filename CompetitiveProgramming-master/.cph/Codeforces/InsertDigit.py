t = int(input())
def max_digit(n,add_digit, digit):   
    for i in range(n):
        if int(digit[i]) < add_digit:
            return(digit[:i] + str(add_digit) + digit[i:])
    return (digit + str(add_digit))

for _ in range(t):
    n, add_digit = map(int,input().split())
    digit = input()
    print(max_digit(n,add_digit,digit))


