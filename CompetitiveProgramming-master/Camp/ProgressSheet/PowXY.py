class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n == 0:
                return 1

            if x == 0:
                return 0

            if n < 0:
                n = -n
                x = 1/x

            if n%2 == 0:
                res = power(x,n//2)
                return res*res

            else:
                res = power(x,n//2)
                return res*res*x

        return  pow(x,n)
        