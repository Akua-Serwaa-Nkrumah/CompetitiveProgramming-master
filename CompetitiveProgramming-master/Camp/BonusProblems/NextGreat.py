from collections import defaultdict 

class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        stack = []
        res = defaultdict(lambda : -1)
        for num in nums2:
            while stack and stack[-1] < num:
                res[stack[-1]] = num
                stack.pop()

            stack.append(num)

        return [res[num] for num in nums1]