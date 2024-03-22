from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_sum = [nums[0]]*len(nums)

        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        count = 0

        pref_div = defaultdict(int)
        pref_div[0] = 1
        
        for j in range(len(prefix_sum)):
            if prefix_sum[j] % k in pref_div:
                count += pref_div[prefix_sum[j] % k]
            
            pref_div[prefix_sum[j] % k] += 1

        return count