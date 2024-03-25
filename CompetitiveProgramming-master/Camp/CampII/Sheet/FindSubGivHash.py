from collections import deque

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s = s[::-1]

        def hash(x):
            return ord(x) - ord('a') + 1

        hsh = 0
        ans = deque([])
        for i in range(k):
            hsh += hash(s[i])*pow(power,k-i-1,modulo)
            hsh %= modulo
            ans.append(s[i])

        res = ''
       
        for i in range(k,len(s)):
            if hsh%modulo == hashValue:
                res = ans.copy()

            hsh *= power
            hsh -= hash(ans[0])*pow(power,k,modulo)
            hsh += hash(s[i])
            hsh %= modulo
            ans.popleft()
            ans.append(s[i])

        if hsh%modulo == hashValue:
            res = ans.copy()

        res.reverse()
        return ''.join(res)