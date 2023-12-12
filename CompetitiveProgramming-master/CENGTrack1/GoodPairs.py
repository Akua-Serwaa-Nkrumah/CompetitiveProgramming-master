class Solution:
    def numIdenticalPairs(self, nums):
        good_pair = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    good_pair +=1
        return good_pair
    
akua = Solution()
print(akua.numIdenticalPairs([1,2,3,1,1,3]))
print(akua.numIdenticalPairs([1,1,1,1]))