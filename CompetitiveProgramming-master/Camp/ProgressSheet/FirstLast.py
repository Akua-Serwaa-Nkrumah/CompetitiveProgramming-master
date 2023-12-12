class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        def bisectLeft(nums, target):
            l, r = 0, len(nums) - 1
            first = len(nums)
            while l <= r:
                mid = (l+r)//2

                if nums[mid] >= target:
                    first = mid
                    r = mid - 1

                else:
                    l = mid + 1 

            return first

        def bisectRight(nums, target):
            l, r = 0, len(nums) - 1
            last = len(nums)
            while l <= r:
                mid = (l+r)//2

                if nums[mid] > target:
                    last = mid
                    r = mid -1

                else:
                    l = mid + 1

            return last-1
        
        l, r = 0, len(nums) - 1
        first = last = len(nums)

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return [bisectLeft(nums, target),bisectRight(nums, target)]

            elif nums[mid] > target:
                r = mid -1

            else:
                l = mid + 1

        return [-1,-1]
    