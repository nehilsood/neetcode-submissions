class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minBuy = prices[0]
        for price in prices:
            max_profit = max(max_profit,price - minBuy)
            minBuy = min(price,minBuy)
        return max_profit

        