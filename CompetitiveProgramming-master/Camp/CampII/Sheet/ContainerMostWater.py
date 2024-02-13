class Solution:
    def maxArea(self, height: [int]) -> int:
        mx = 0
        l, r = 0, len(height)-1

        while l < r:
            if height[l] < height[r]:
                mx = max(mx,(r-l)*height[l])
                l += 1

            else:
                mx = max(mx,(r-l)*height[r])
                r -= 1

        return mx