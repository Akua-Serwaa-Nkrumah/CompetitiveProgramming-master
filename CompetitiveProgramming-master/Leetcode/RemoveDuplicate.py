class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        
        prev = nums[0]
        k = 1  # Counter for unique elements
        
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[k] = nums[i]
                prev = nums[i]
                k += 1
        dup = k
        while k < len(nums):
            nums[k] = "_"
            k += 1
        
        return dup

        """
        :type nums: List[int]
        :rtype: int
        """