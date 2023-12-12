class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        sub = set()
        mx = 0

        while r < len(s):
            if s[r] in sub:
                mx = max(mx,len(sub))
                sub.remove(s[l])
                l += 1
                
            else:
                sub.add(s[r])
                r += 1

        mx = max(mx,len(sub))

        return mx

