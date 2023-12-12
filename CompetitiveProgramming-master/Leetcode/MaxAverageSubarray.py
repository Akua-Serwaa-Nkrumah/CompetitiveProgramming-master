class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        window_sum = float(sum(nums[:k]))
        max_sum = window_sum
        for right in range(k,len(nums)):
            window_sum += nums[right] - nums[left]
            max_sum = max(max_sum,window_sum)
            left += 1

        return (max_sum/k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """