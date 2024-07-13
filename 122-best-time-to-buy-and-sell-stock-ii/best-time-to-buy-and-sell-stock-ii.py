class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        L = 0
        CurrentHigh = 0
        MaxHigh = 0
        TotalProfit = 0
        for R in range(n):
            CurrentHigh = (prices[R] - prices[L])
            if CurrentHigh < 0:
                CurrentHigh = 0
                L = R
            if MaxHigh < CurrentHigh:
                MaxHigh = CurrentHigh
                TotalProfit += MaxHigh
                MaxHigh = 0
                L = R
        return TotalProfit