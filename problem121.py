class Solution(object):
    def maxProfit(self, prices):
        max=0
        buy=prices[0]
        price=prices[1:]
        for sell in price:
            if (sell<buy):
                buy=sell
            if (sell-buy>max):
                max=sell-buy
        return max
