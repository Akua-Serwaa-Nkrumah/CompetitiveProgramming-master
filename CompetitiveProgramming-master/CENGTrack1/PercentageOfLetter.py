class Solution(object):
    def percentageLetter(self, s, letter):
        count = s.count(letter)
        percentage = (count*100)/len(s)
        percentage = int(percentage)
        return percentage
        """
        :type s: str
        :type letter: str
        :rtype: int
        """

