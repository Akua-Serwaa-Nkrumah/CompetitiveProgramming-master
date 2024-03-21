class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        matrix = [[float('inf') for _ in range(numCourses)] for _ in range(numCourses)]

        for i in prerequisites:
            matrix[i[0]][i[1]] = 1

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        boolean = [0]*len(queries)

        for i in range(len(queries)):
            if matrix[queries[i][0]][queries[i][1]] == float('inf'):
                boolean[i] = False
            else:
                boolean[i] = True

        return boolean