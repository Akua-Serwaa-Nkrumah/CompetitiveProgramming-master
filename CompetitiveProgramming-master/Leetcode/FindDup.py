# Binary Search
class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        l, r = 0, len(nums) - 1

        def check(target):
            count = 0
            for i in range(len(nums)):
                if nums[i] <= target:
                    count += 1
            return count

        while l <= r:
            mid = l + (r-l)//2

            if check(mid) > mid:
                r = mid - 1
            else:
                l = mid + 1

        return l

# Cyclic sort
    
class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        i = 0

        while i < len(nums):
            idx = nums[i] - 1

            if idx != i:
                if nums[idx] != nums[i]:
                    nums[idx], nums[i] = nums[i], nums[idx]

                else:
                    i += 1

            else:
                i += 1

        return nums[-1]








        




