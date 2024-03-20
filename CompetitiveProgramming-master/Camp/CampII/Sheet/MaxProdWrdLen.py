class Solution:
    def maxProduct(self, words: list[str]) -> int:
        wrd_int = [0]*len(words)
        wrd_len = [0]*len(words)

        for i in range(len(words)):
            check = 0
            for j in range(len(words[i])):
                check |= 1 << (ord(words[i][j]) - ord('a'))

            wrd_int[i] = check
            wrd_len[i] = len(words[i])

        mx = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if (wrd_int[i] & wrd_int[j]) == 0:
                    mx = max(mx,wrd_len[i]*wrd_len[j])

        return mx