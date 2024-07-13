class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        L = 0
        cm = nums[L]
        m = nums[L]
        for R in range(1,n):
            if cm < 0:
                cm = 0
                L = R
            cm += nums[R]
            if cm > m:
                m = cm
        return m