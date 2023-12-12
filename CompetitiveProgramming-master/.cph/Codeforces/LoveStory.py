t = int(input())
string = "codeforces"
for _ in range(t):
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] != string[i]:
            count += 1
    print (count)
    