class NumArray:

    def __init__(self, nums: List[int]):
        self.NumsArray = []
        total = 0
        for i in nums:
            total += i
            self.NumsArray.append(total)

    def sumRange(self, left: int, right: int) -> int:
        l = self.NumsArray[left-1] if left > 0 else 0
        r = self.NumsArray[right] if right < len(self.NumsArray) else 0
        if left <= right:
            return r-l
        else:
            return 0