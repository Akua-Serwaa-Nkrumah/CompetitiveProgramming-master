class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        i = 0
        while i < len(nums):
            idx = nums[i] - 1

            if idx != i:
                if nums[i] != nums[idx]:
                    nums[i], nums[idx] = nums[idx], nums[i]

                else:
                    i += 1

            else:
                i += 1


        for i in range(len(nums)):
            if nums[i] != i + 1:
                res = [nums[i],i+1]

        return res

       

       
