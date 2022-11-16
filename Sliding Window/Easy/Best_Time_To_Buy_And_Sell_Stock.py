class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_price = prices[0]
        max_price = prices[0]
        for i in range(1, len(prices)) :
            if prices[i] > max_price :
                max_price = prices[i]
            elif prices[i] < min_price and i < len(prices) - 1:
                min_price = min(prices[i], min_price)
                max_price = prices[i+1] 
            
            max_profit = max(max_profit, max_price - min_price)
            
        return max_profit
                    