from queue import deque

class Solution:
    def canVisitAllRooms(self, rooms: [[int]]) -> bool:
        visited = set([0])
        queue = deque([0])

        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                visited.add(node)

                for j in rooms[node]:
                    if j not in visited:
                        queue.append(j)

        return len(visited) == len(rooms)

        