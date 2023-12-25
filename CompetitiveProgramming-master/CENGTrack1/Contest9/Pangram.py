from collections import Counter

n = int(input())
s = input()
s = s.lower()

s_count = Counter(s)
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

a = "YES"

for i in alpha:
    if s_count[i] == 0:
        a = "NO"
        break

print(a)