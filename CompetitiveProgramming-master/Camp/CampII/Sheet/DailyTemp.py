class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return answer
