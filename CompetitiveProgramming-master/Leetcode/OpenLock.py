from queue import deque

class Solution:
    def openLock(self, deadends: [str], target: str) -> int:
        level = 0
        visited = set()

        queue = deque([['0000',level]])

        while queue:
            length = len(queue)

            node,level = queue.popleft()

            if node == target:
                return level

            if (node not in deadends) and (node not in visited):
                visited.add(node)
                level += 1
                for i in range(4):
                    queue.append([node[:i] + str((int(node[i])+1)%10) + node[i+1:], level])
                    queue.append([node[:i] + str((int(node[i])-1)%10) + node[i+1:], level])

        return -1
        