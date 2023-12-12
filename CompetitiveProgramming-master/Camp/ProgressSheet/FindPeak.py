class Solution(object):
    def findPeakElement(self, nums):
        for i in range(1,len(nums)-1):
            if  nums[i-1]< nums[i] > nums[i+1]:
                return i

        if len(nums) > 1 and nums[0] < nums[1]:
            return len(nums)-1
        else:
            return 0
        """
        :type nums: List[int]
        :rtype: int
        """