class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        pos = len(nums)

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            
            if nums[mid] >= target:
                pos = mid
                r = mid -1

            else:
                l = mid + 1

        return pos