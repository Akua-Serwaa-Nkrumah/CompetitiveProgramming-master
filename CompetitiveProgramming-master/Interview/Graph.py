from collections import deque, defaultdict


adj_list = {1:[2,3,5], 2: [1,5], 3: [1,4], 4: [5,3], 5:[4,2]}
start, goal = 1, 5
arr = []
queue = [start]

def dfs(node):
    visited = set()
    path = []

    while queue:
        length = len(queue)

        for i in range(length):
            child = queue.pop()

            if child not in visited:
                path.append(child)
                visited.add(child)

                if child == goal:
                    arr.append(path)
                    path = [start]
                    visited = set([start])
                else:
                    for neighbor in adj_list[child]:
                        queue.append(neighbor)
    
dfs(start)
print(arr)