class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        mn1, mn2 = nums[0], float('inf')

        for i in range(1,len(nums)):
            if nums[i] <= mn2:
                if nums[i] <= mn1:
                    mn1 = nums[i]

                else:
                    mn2 = nums[i]

            else:
                return True
                
        return False