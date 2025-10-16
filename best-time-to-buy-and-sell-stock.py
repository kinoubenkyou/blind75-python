class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0
        buying_price: int = prices[0]
        selling_price: int = prices[0]
        for price in prices[1:]:
            if price < buying_price:
                profit = selling_price - buying_price
                if max_profit < profit:
                    max_profit = profit
                buying_price = price
                selling_price = price
            elif price > selling_price:
                selling_price = price
        profit = selling_price - buying_price
        return max_profit if max_profit > profit else profit
