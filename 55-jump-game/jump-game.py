class Solution:
    def canJump(self, nums: List[int]) -> bool:
        L = 0
        MaxReachable = nums[0]
        n = len(nums)
        while L <= MaxReachable and L < n:
            MaxReachable = max(L + nums[L] , MaxReachable)
            L += 1
            
        return True if MaxReachable >= n-1 else False
