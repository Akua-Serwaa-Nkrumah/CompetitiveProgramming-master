#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

class Solution(object):
    def twoSum(self, numbers, target):
        index1, index2 = 0, len(numbers)-1
        while index1 < index2:
            current_sum = numbers[index1]+numbers[index2]
            if current_sum == target:
                return [index1+1,index2+1]
            if current_sum < target:
                index1+=1
            if current_sum > target:
                index2-=1
        return []
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
