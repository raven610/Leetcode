class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        vol = 0
        maxL = height[0]
        maxR = height[R]
        while L <= R:
            if maxR >= maxL:
                vol += max(0,maxL-height[L])
                maxL = max(maxL,height[L])
                L += 1
            else:
                vol += max(0,maxR-height[R])
                maxR = max(maxR,height[R])
                R -= 1
        return vol
