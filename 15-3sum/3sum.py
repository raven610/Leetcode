class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        print(nums)
        if n == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
            return []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = n - 1
            while L<R:
                su = nums[L] + nums[R] + nums[i]
                if su > 0:
                    R = R - 1
                elif su < 0:
                    L = L + 1
                else:
                    ans.append([nums[i],nums[L],nums[R]])
                    L += 1
                    while (L<R) and (nums[L] == nums[L-1]):
                        L += 1
        return ans