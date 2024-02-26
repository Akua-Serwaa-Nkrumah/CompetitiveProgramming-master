class Solution:
    def rob(self, nums: list[int]) -> int:
        first1 , sec1 = 0, 0
        first2, sec2 = 0, 0
        ans1,ans2 = nums[0], nums[-1]

        for i in range(len(nums)-1):
            ans1 = max(first1+nums[i],sec1)
            first1 = sec1
            sec1 = ans1

        for i in range(1,len(nums)):
            ans2 = max(first2+nums[i],sec2)
            first2 = sec2
            sec2 = ans2

        return max(first1,ans2,first2,ans1)
