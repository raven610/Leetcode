class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        t = 0
        d = {0:1}
        c = 0
        for i in range(len(nums)):
            t = t + nums[i]
            if t-k in d:
                c += d[t-k]
            if t not in d:
                d[t] = 1
            else:
                d[t] +=1
        return c
