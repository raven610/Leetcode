class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        CurrentHigh = 0
        MaxHigh = 0
        L = 0
        for R in range(n):
            CurrentHigh = (prices[R] - prices[L])
            if CurrentHigh < 0:
                CurrentHigh = 0
                L = R
            if MaxHigh < CurrentHigh:
                MaxHigh = CurrentHigh
            print(L,R)
        return MaxHigh
            