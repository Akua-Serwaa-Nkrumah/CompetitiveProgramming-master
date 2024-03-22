class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        memo = {}

        def dp(i,status):
            if (i,status) in memo:
                return memo[(i,status)]

            if i == len(prices):
                return 0

            if status:
                buy =  -prices[i] + dp(i+1,0)
                notBuy = dp(i+1, 1)
                memo[(i,status)] = max(buy,notBuy)
            else:
                sell = prices[i] + dp(i+1,1) - fee
                notSell = dp(i+1,0)
                memo[(i,status)] = max(sell, notSell)
            
            return memo[(i,status)]

        return dp(0,1)

            

