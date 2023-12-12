class Solution(object):
    def judgeSquareSum(self, c):
        def is_perfect_square(n):
            root = int(n ** 0.5)
            return root * root == n

        for a in range(int(c ** 0.5) + 1):
            b_squared = c - a * a
            if is_perfect_square(b_squared):
                return True

        return False