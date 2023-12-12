class Solution(object):
    def checkInclusion(self, s1, s2):
        left, right = 0, len(s1)
        while right <= len(s2):
            if sorted(s2[left:right]) == sorted(s1):
                print(s2[left:right])
                return True
            left += 1
            right += 1
        return False