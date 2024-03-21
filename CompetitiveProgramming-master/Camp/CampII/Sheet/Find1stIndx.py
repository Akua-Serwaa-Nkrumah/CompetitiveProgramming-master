class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,m = len(needle), len(haystack)
        hasher = 0

        def hash(x):
            return ord(x) - ord('a') + 1

        hsh = 0
        for i in range(n):
            hsh += (hash(needle[i])*31**(n-1-i))
            hsh %= 1000000007

        for i in range(m):
            if i == n:
                break
            hasher += (hash(haystack[i])*31**(n-1-i))
            hasher %= 1000000007

        if hasher == hsh:
            return 0

        for i in range(m-n):
            if hasher == hsh:
                return i
            
            hasher *= 31
            hasher += (hash(haystack[i+n])-(hash(haystack[i])*31**n))
            hasher %= 1000000007

        if hasher == hsh:
            return i+1

        return -1