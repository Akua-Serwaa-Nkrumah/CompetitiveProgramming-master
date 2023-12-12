from collections import defaultdict

class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        prefix_sum = [nums[0]]*len(nums)

        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        count = 0

        pref_dict = defaultdict(int)
        pref_dict[0] = 1

        for j in range(len(prefix_sum)):
            if prefix_sum[j]-k in pref_dict:
                count += pref_dict[prefix_sum[j]-k]
                
            pref_dict[prefix_sum[j]] += 1
        
        return count