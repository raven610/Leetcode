class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = nums1[:m]
        l1 = len(nums1)
        l2 = len(nums2)
        ans = []
        i = 0
        j = 0
        for x in range(l1+l2):
            if i > l1 - 1 or j > l2 - 1:
                break
            else:
                if nums1[i]<nums2[j]:
                    ans.append(nums1[i])
                    i+=1
                else:
                    ans.append(nums2[j])
                    j+=1
        if i<l1:
            for x in range(i,l1):
                ans.append(nums1[x])
                
        if j<l2:
            for x in range(j,l2):
                ans.append(nums2[x])
        nums1[:] =  ans