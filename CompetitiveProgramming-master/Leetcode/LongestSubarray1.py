class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        max_length = 0
        deleted = False
        for right in range(len(nums)):
            if nums[right] == 0:
                if not deleted:
                    deleted = True
                else:
                    while nums[left] == 1:
                        left += 1
                    left += 1
            max_length = max(max_length, right - left)
        return max_length
        
        """
        :type nums: List[int]
        :rtype: int
        """