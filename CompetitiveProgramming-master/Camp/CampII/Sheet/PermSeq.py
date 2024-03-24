class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = []
        for i in range(1,n+1):
            s.append(i)

        def getPerm(s):
            i = len(s) - 1
            while i > 0 and s[i-1] > s[i]:
                i -= 1

            i-= 1
            j = len(s) - 1

            while j > i and s[j] < s[i]:
                j -= 1

            s[j], s[i] = s[i], s[j]
            i += 1
            j = len(s)-1

            while i < j:
                s[j], s[i] = s[i], s[j]
                i += 1
                j -= 1

            return s

        for i in range(k-1):
            getPerm(s)

        for i in range(len(s)):
            s[i] = str(s[i])

        return ''.join(s)