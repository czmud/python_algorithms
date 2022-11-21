class Solution:
    def maxProfit(self, prices):
        res = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                res = max(res, price - min_price)
        return res