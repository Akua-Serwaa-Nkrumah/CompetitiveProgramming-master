class Solution(object):
    def moveZeroes(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero] = nums[i]
                zero += 1

        while zero < len (nums):
            nums[zero] = 0
            zero += 1   

