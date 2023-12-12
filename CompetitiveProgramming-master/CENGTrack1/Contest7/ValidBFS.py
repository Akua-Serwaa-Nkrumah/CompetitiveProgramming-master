from collections import defaultdict
from queue import deque

n = int(input())
adj_list = defaultdict(list)

for _ in range(n-1):
    a, b = map(int,input().split())

    adj_list[a].append(b)
    adj_list[b].append(a)

seq = list(map(int,input().split()))
sequence = []

queue = deque([1])
visited = set()

lev = 0
while len(queue) > 0:
    length = len(queue)
     
    child = []
    for i in range(length):
        node = queue.popleft() 

        if node not in visited:
            visited.add(node)
            child.append(node)

            for i in adj_list[node]:
                queue.append(i)

        sequence.extend(sorted(child))
    
        seq[lev:(lev+len(child))] = sorted(seq[lev:(lev+len(child))])
        
    lev += len(child)


if seq == sequence:
    print('Yes')
else: 
    print('No')








