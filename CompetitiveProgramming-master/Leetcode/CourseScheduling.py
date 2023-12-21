from collections import defaultdict
from queue import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        adj_list = defaultdict(list)
        courses = {course:0 for course in range(numCourses)}

        sorted_arr = []

        for i in prerequisites:
            courses[i[0]] += 1
            adj_list[i[1]].append(i[0])

            
        queue = deque([])

        for i in courses:
            if courses[i] == 0:
                queue.append(i)

        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                sorted_arr.append(node)

                for j in adj_list[node]:
                    courses[j] -= 1

                    if courses[j] == 0:
                        queue.append(j)


        return sorted_arr if len(sorted_arr) == numCourses else []
