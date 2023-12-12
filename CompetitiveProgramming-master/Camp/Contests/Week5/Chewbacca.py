n = int(input())
n_str = list(str(n))

if int(n_str[0]) >= 5 and int(n_str[0]) != 9:
    n_str[0]= str(9- int(n_str[0]))
    
for i in range(1,len(n_str)):
    if  int(n_str[i]) >= 5:
        n_str[i]= str(9- int(n_str[i]))
        
print(int("".join(n_str)))
