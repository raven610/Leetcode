class Solution:
    def canJump(self, nums: List[int]) -> bool:
        L = 0
        MaxReachable = nums[0]
        n = len(nums)
        while L <= MaxReachable and L < n:
            MaxReachable = max(L + nums[L] , MaxReachable)
            if MaxReachable >= n-1:
                return True
            L += 1
            
        return False
