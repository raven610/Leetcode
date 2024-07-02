class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        count = 0
        k = 2
        n = len(nums)
        for p2 in range(n-1):
            if nums[p2] == nums[p2+1]:
                count += 1
                if count < k:
                    nums[p1] = nums[p2]
                    p1 += 1
            else:
                nums[p1] = nums[p2]
                p1 += 1
                count = 0
        nums[p1] = nums[n-1]
        p1 += 1
        return p1
