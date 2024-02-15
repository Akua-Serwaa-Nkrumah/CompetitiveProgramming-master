class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = ''

        while n != 0:
            if binary:
                if str(n%2) == binary[-1]:
                    return False

            binary += str(n%2)
            n >>= 1

        return True