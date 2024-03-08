class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        total = 0
        ans = 0

        for r in range(len(nums)):
            total += nums[r]
            ans = max(ans,ceil(total/(r+1)))

        return ans 