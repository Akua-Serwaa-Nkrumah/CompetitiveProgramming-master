n = int(input())
s = []
for i in range(n):
    word = input()
    s.append(word)


for j in s:
    if(3<=len(j)<=100):
        print(j[0:2]+"... "+ j+"?") 
    else:
        print("Length of words should be between 3 and 100")  
