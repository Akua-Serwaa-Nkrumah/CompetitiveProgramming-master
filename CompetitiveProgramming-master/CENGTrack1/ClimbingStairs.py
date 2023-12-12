from collections import defaultdict

class Solution:

    def __init__(self):
        self.stair = defaultdict(int) 

    def climbStairs(self, n: int) -> int:
        if n in self.stair:
            return self.stair[n]

        if n < 4:
            return n

        self.stair[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.stair[n]

        