class Solution:
    def maxProfit1(self, prices):
        profit = 0
        for i in range(1,len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit

    def __init__(self):
        self.memo = {
            0: 0,
            1: 0
        }
    # Let's use DP to brute force the solution just for fun
    def maxProfit(self, prices):
        if len(prices) not in self.memo:
            buy = prices[0]
            max_added = 0
            for i in range(1, len(prices)):
                # buy
                max_added = max(max_added, prices[i] - buy + self.maxProfit(prices[i+1:]))
                # don't buy
                max_added = max(max_added, self.maxProfit(prices[i:]))
            self.memo[len(prices)] = max_added
        
        return self.memo[len(prices)]




