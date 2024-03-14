class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        
        def dp(i,j):
            if i < len(text1) and j < len(text2):

                if (i,j) not in memo:
                    if text1[i] == text2[j]:
                        memo [(i,j)] = 1 + dp(i+1,j+1)
                    
                    else:
                        memo[(i,j)] = max(dp(i,j+1),dp(i+1,j))

                return memo[(i,j)]

            return 0

        return dp(0,0)