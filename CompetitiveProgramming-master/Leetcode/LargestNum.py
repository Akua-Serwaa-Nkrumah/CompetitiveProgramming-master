class Solution:
    def largestNumber(self, nums: [int]) -> str:
        nums = [str(num) for num in nums]

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) < (nums[j] + nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]

        res = str(int(''.join(nums)))

        return res

        
