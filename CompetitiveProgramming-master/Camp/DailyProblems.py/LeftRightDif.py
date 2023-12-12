class Solution:
    def leftRightDifference(self, nums):
        p_sum = [nums[0]]*len(nums)
        s_sum = [nums[-1]]*len(nums)
        ans = [0]*len(nums)

        for i in range(1,len(nums)):
            p_sum[i] = p_sum[i-1] + nums[i]

        for j in range(len(nums)-2,-1,-1):
            s_sum[j] = s_sum[j+1] + nums[j]

        for k in range(len(nums)):
            ans[k] = abs(p_sum[k]-s_sum[k])

        return ans