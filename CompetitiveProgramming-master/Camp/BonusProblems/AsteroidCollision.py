class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        stack = []

        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                else:
                    break

            if stack and asteroids[i] < 0 and abs(asteroids[i]) < stack[-1]:
                continue
            
            if stack and asteroids[i] < 0 and abs(asteroids[i]) == stack[-1]:
                stack.pop()
                continue

            stack.append(asteroids[i])

        return stack