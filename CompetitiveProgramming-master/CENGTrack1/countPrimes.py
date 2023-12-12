class Solution(object):
    def countPrimes(self, l):
        count = 0
        for n in range(l):
            # b = 2
            a = 0
            for b in range(2,(n//2)+1):
                if (n % b) == 0:
                    a = b
                    break
                # b+=1
            if a or n == 1 or n == 0:
                pass  
            else:
                count += 1
        return count
akua = Solution()
print(akua.countPrimes(4))
print(akua.countPrimes(10))
print(akua.countPrimes(0))
print(akua.countPrimes(1))