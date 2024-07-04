class LinkedList:
    def __init__(self,data,count):
        self.data = data
        self.count = count
        self.next = None
class Solution:
    def insert(self,start,node):
        while start.next != None and start.next.count > node.count :
            start = start.next
        node.next = start.next
        start.next = node
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        ans = []
        for i in nums:
            d[i] += 1
        start = LinkedList(0,0)
        for i in d.keys():
            self.insert(start,LinkedList(i,d[i]))
        n = start
        for i in range(k):
            ans.append(n.next.data)
            n = n.next
        return ans