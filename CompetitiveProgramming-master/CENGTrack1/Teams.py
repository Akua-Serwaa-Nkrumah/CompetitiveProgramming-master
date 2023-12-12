n = int(input())
counter = 0
array = []
for _ in range(n):
    array.append(list(map(int,input().split()))) 
for i in range (len(array)):
    if array[i].count(1) > 1:
        counter+=1
print (counter)