class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        L = 0
        CurrentSum = 0
        MaxSum = nums[L]
        for R in range(n):
            if CurrentSum < 0:
                CurrentSum = 0
                L = R
            CurrentSum += nums[R]
            if CurrentSum > MaxSum:
                MaxSum = CurrentSum
        return MaxSum