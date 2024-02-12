class Solution:
    def missingNumber(self, nums: [int]) -> int:
        nums.append(len(nums))

        i = 0

        while i < len(nums):
            idx = nums[i]

            if idx != i:
                if nums[i] != nums[idx]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                
                else:
                    i += 1

            else:
                i += 1
        
   
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return i