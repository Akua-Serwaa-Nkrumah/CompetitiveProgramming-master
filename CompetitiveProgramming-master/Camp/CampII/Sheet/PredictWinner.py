class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        memo = {}

        def dp(i,n,flag):
            if i > n:
                return 0

            if flag:
                return max(dp(i+1,n,0) + nums[i],dp(i,n-1,0) + nums[n])

            return min(dp(i+1,n,1) - nums[i], dp(i,n-1,1)- nums[n])

        return dp(0,len(nums)-1,1) >= 0