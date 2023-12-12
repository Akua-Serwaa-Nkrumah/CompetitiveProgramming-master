class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        i = len(piles)/3
        you = 0
        while i < len(piles):
            you += piles[i]
            i += 2
        return you
                    
        """
        :type piles: List[int]
        :rtype: int
        """