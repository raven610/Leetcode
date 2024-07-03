class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t1 = 1
        t2 = 1
        l1 = []
        l2 = []
        n = len(nums)
        for i in range(n):
            t1 *= nums[i]
            t2 *= nums[n-1-i]
            l1.append(t1)
            l2.append(t2)
        ans = []
        for i in range(n):
            if i == 0:
                ans.append(l2[n-i-2])
            elif i == n-1:
                ans.append(l1[i-1])
            else:
                ans.append(l1[i-1]*l2[n-i-2])
            
        return ans
