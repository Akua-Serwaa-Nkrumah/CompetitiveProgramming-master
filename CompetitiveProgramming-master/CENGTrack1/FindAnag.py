from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        p_count = Counter(p)
        l = 0
        anag = []

        window = s[:len(p)]
        window_freq = Counter(window)

        if window_freq == p_count:
            anag.append(l)

        for r in range(len(p),len(s)):
            window_freq[s[r]] += 1
            window_freq[s[l]] -= 1

            l += 1

            if window_freq == p_count:
                anag.append(l)

        return anag
        