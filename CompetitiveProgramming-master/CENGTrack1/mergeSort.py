class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        for i in range(m+n):
            if i < m:
                nums1[i] = nums1[i]
            else:
                nums1[i] = nums2[i-m]
        nums1.sort()
            
akua = Solution()
akua.merge([1,2,3,0,0,0],3,[2,5,6],3)
