class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mn, mx = min(nums), max(nums)

        def gcd(mn,mx):
            if mx == 0:
                return mn

            return gcd(mx,mn%mx)

        return gcd(mn,mx)