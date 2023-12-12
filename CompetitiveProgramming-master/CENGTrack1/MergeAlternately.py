class Solution(object):
    def mergeAlternately(self, word1, word2):
        if(1<=len(word1),len(word2) <=100):
            min_length = min(len(word1),len(word2))
            result = ""
            for i in range(min_length):
                result += word1[i]
                result += word2[i]
            i = i + 1
            if i > len(word1)-1:
                for j in range(i,len(word2)):
                    result += word2[j]
            elif i > len(word2)-1:
                for j in range (i, len(word1)):
                    result += word1[j]
        return result
