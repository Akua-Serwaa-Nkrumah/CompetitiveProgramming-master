n = int(input())
numbers = list(map(int,input().split()))
# print(numbers)
def checkOddDivisor():
    for number in numbers:
        if number == 2:
            print("NO")
        for j in range(3,number,2):
            if number%j == 0:
                print('YES')
checkOddDivisor()