class Solution:
    def minEatingSpeed(self, piles: [int], h: int) -> int:
        l, r = 1, max(piles)
        def check(k):
            count = 0
            for i in range(len(piles)):
                count += (piles[i]//k) + 1 if piles[i]%k != 0 else (piles[i]//k)
                if count > h:
                    break
            return count

        while l <= r:
            mid = l + (r-l)//2

            if check(mid) > h:
                l = mid + 1
            else:
                r = mid - 1

        return l
