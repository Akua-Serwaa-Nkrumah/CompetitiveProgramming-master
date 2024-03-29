class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        i = 0

        while i < len(nums):
            idx = nums[i] - 1

            if idx != i:
                if nums[idx] != nums[i]:
                    nums[i], nums[idx] = nums[idx], nums[i]

                else:
                    i += 1

            else:
                i += 1

        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i+1)

        return res