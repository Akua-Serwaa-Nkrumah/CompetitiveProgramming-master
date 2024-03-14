class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dp(i,j):
            if i < len(word1) and j < len(word2):

                if (i,j) not in memo:
                    if word1[i] == word2[j]:
                        memo[(i,j)] = dp(i+1,j+1)

                    else:
                        memo[(i,j)] = 1 + min(dp(i+1,j+1),dp(i,j+1),dp(i+1,j))

                    
                return memo[(i,j)]

            if i >= len(word1):
                return len(word2) - j

            return len(word1) - i

        return dp(0,0)