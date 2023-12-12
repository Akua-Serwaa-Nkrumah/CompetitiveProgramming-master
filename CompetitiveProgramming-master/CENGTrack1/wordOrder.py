# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = []
for _ in range(n):
    words.append(input())
    
print(len(set(words)))

counts = []
for word in words:
    count = words.count(word)
    counts.append(count)
    if(count > 1):
        words.remove(word)
print(*counts)