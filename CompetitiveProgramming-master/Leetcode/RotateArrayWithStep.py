class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        temp_array = []
        temp_array[:] = reversed(nums[:])
        temp_array[:k] = reversed(temp_array[:k])
        temp_array[k:] = reversed(temp_array[k:])
        nums[:] = temp_array[:]