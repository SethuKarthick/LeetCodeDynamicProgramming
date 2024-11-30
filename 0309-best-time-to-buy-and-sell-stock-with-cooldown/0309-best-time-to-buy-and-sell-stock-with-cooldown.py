class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        def dfs(i, ToBuy):

            if i >= len(prices):
                return 0

            if (i, ToBuy) in dp:
                return dp[i, ToBuy]


            coolDown = dfs(i+1, ToBuy)

            if ToBuy:
                buy = dfs(i+1, not ToBuy) - prices[i]
                dp[(i, ToBuy)] = max(buy, coolDown)
            else:
                sell = dfs(i+2, not ToBuy) + prices[i]
                dp[(i, ToBuy)] = max(sell, coolDown)

            return dp[(i, ToBuy)]

        return dfs(0, True)

            
