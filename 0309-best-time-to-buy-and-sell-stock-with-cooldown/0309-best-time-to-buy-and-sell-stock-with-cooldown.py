class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {} # key = (i, buy or sell) -> val = max profit
        
        def dfs(i, shouldBuy):
            if i >= len(prices): return 0
            
            if (i, shouldBuy) in dp:
                return dp[(i, shouldBuy)]
            
            if shouldBuy:
                buy = dfs(i+1, not shouldBuy) - prices[i]
                cooldown = dfs(i+1, shouldBuy)
                dp[(i, shouldBuy)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not shouldBuy) + prices[i]
                cooldown = dfs(i+1, shouldBuy)
                dp[(i, shouldBuy)] = max(sell, cooldown)
                
            return dp[(i, shouldBuy)]
        return dfs(0, True)
        