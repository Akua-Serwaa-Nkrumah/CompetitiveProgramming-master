class Solution(object):   

    def reverseString(self, s):
        left, end = 0, len(s) - 1

        def reverse(left,end):
            if end - left < 1:
                return

            s[left], s[end] = s[end], s[left]
            reverse(left+1,end-1)

        reverse(left,end)

        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """