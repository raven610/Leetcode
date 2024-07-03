class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum = []
        t = 0
        for i in nums:
            t += i
            prefixsum.append(t)
        n = len(prefixsum)
        for i in range(n):
            if i > 0:
                if prefixsum[i-1] == (prefixsum[n-1] - prefixsum[i]):
                    return i
            else:
                if prefixsum[n-1]-prefixsum[0] == 0:
                    return 0
        return -1