from math import ceil

class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [1]*(n)
        if n < 2:
            return 0

        for i in range(2,ceil(n**0.5)):
            if arr[i] == 1:
                for j in range(i*i,n,i):
                    arr[j] = 0

        return sum(arr[2:n])
