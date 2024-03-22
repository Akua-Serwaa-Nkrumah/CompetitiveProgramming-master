class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        modulo = total%p
        
        if modulo == 0:
            return 0

        dic = {0:-1}

        prefix = [nums[0]]*len(nums)

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        for i in range(len(prefix)):
            prefix[i] %= p

        mn = len(nums)
       
        for i in range(len(prefix)):
            key = prefix[i] - modulo
            if key < 0:
                key += p

            if key in dic:
                mn = min(mn,i - dic[key])

            dic[prefix[i]] = i

        return mn if mn < len(nums) else -1