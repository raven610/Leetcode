class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        for i in s:
            if i-1 not in s:
                le = 0
                k = 0
                while i+k in s:
                    le += 1
                    k += 1
                l = max(l,le)
        return l
