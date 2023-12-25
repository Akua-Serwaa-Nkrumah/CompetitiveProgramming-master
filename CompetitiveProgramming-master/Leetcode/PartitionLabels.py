from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> [int]:
        indices = defaultdict(list)
        ans = []

        for i in range(len(s)):
            if not indices[s[i]]:
                pos = [i+1,i+1]
                for j in range(i+1,len(s)):
                    if s[i] == s[j]:
                        pos[1] = j+1

                indices[s[i]] = pos

        start, end = indices[s[0]][0],indices[s[0]][1]

        for i in indices:
            if indices[i][1] > end:
                if indices[i][0] > end:
                    ans.append(indices[i][0] - start)
                    start = indices[i][0]
                  
                end = indices[i][1]

        ans.append(end - start + 1)

        return ans
                
