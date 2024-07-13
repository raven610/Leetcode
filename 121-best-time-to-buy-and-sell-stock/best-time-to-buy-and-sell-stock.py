class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        CurrentHigh = 0
        MaxHigh = 0
        L = 0
        for R in range(n):
            Profit = prices[R] - prices[L]
            if Profit > CurrentHigh:
                CurrentHigh = Profit
                if MaxHigh < CurrentHigh:
                    MaxHigh = CurrentHigh
            if Profit < 0:
                L = R
        return MaxHigh
            