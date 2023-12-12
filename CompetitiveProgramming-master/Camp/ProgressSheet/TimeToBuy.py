from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: [int], k: int) -> int:
        total = 0
        queue = deque()

        for index, num in enumerate(tickets):
            queue.append([index,num])

        print(queue)
        while queue:
            index, num = queue.popleft()
            if num > 0:
                total += 1
                num -= 1

            if index == k and num == 0:
                return total

            if num >= 0:
                queue.append([index,num])

        return

            

        