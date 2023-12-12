from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums, k) -> int:
        left = 0
        window_sum = sum(nums[:k])
        window_freq = Counter(nums[:k])

        if len(window_freq) == k:
            maximum = window_sum
        else:
            maximum = 0

        for right in range(k,len(nums)):
            window_sum += nums[right] - nums[left]

            window_freq[nums[left]] -= 1
            window_freq[nums[right]] += 1
            
            if window_freq[nums[left]] == 0:
                del window_freq[nums[left]]
                
            if len(window_freq) == k:
                maximum = max(maximum,window_sum)

            left += 1

        return maximum


