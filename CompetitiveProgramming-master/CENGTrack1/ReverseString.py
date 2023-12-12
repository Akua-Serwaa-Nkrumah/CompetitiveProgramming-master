class Solution(object):
    def reverseString(self, s):
        left = 0
        end = len(s) - 1
        while left < end:
            temp = s[left]
            s[left] = s[end]
            s[end] = temp
            left += 1
            end -= 1