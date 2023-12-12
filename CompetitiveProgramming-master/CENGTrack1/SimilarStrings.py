class Solution:
    def similarPairs(self, words):
        similar_pairs = 0
        words = sorted(words)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i]) == set(words[j]):
                    similar_pairs += 1
        return similar_pairs
    
akua = Solution()
print(akua.similarPairs(["aba","aabb","abcd","bac","aabc"]))
print(akua.similarPairs(["aabb","ab","ba"]))
print(akua.similarPairs(["nba","cba","dba"]))
