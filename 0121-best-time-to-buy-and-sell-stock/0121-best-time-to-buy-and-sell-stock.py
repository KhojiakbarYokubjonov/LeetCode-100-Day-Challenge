class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minp = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - minp
            max_profit = max(max_profit, profit)
            minp = min(minp, prices[i])
            
        return max_profit
        