class Solution:
    def runningSum(self, nums) :
        result = [nums[0]]*(len(nums))

        for i in range(1,len(nums)):
            result[i] = result[i-1]+nums[i]

        return result