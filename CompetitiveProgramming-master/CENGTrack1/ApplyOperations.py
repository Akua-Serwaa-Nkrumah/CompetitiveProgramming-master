class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]=0

        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero] = nums[i]
                zero += 1

        while zero < len (nums):
            nums[zero] = 0
            zero += 1  
        return nums  