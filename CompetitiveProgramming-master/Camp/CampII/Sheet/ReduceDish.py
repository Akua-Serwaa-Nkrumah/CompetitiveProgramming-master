class Solution:
    def maxSatisfaction(self, satisfaction: [int]) -> int:
        satisfaction.sort()
        res = satisfaction[-1]

        lis = [satisfaction[-1]]

        for i in range(len(satisfaction)-2,-1,-1):
            tot = sum(lis)

            if res + tot + satisfaction[i] > res:
                res += satisfaction[i] + tot

                lis.append(satisfaction[i])

        return max(0,res)

