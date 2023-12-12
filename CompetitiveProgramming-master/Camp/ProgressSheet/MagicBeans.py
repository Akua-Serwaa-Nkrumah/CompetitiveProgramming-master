class Solution:
    def minimumRemoval(self, beans: [int]) -> int:
        beans.sort()
        p_sum = [beans[0]]*len(beans)

        for i in range(1,len(beans)):
            p_sum[i] = p_sum[i-1] + beans[i]

        res = (p_sum[-1]-p_sum[0]) - beans[0]*(len(beans)-1)
        for i in range(1,len(beans)):
            res = min(res,(p_sum[-1]-p_sum[i]) - beans[i]*(len(beans)-1-i) + p_sum[i-1])

        return res