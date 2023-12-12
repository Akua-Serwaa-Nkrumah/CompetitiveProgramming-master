class Solution(object):
    def targetIndices(self, nums, target):
        nums = sorted(nums)
        target_position = []
        for i in range(len(nums)):
            if nums[i] == target:
                target_position.append(i)

        return target_position