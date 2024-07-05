class DLL:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LRUCache:
    def insertAtBegin(self,node):
        node.next = self.start.next
        self.start.next.prev = node
        node.prev = self.start
        self.start.next = node

    def insertAtEnd(self,node):
        node.prev = self.end.prev
        node.next = self.end
        self.end.prev.next = node
        self.end.prev = node
    
    def removeAtEnd(self):
        if self.end.prev == self.start:
            return -1
        removed = self.end.prev.data
        self.end.prev = self.end.prev.prev
        self.end.prev.next = self.end
        return removed

    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def search(self,key):
        pointer = self.start.next
        while pointer.next != None and pointer != self.end:
            if pointer.data == key:
                pointer.next.prev = pointer.prev
                pointer.prev.next = pointer.next
                return pointer
            pointer = pointer.next
        return None

    def printLL(self):
        pointer = self.start
        while pointer.next!=None:
            print(pointer.data,end=' -> ')
            pointer = pointer.next
        print()
        print(self.LRUCache)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUCache = {}
        self.LRUNode = {}
        self.start = DLL(0)
        self.end = DLL(0)
        self.start.next = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            self.remove(self.LRUNode[key])
            node = DLL(key)
            self.insertAtBegin(node)
            self.LRUNode[key] = node
            return self.LRUCache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.remove(self.LRUNode[key])
            node = DLL(key)
            self.insertAtBegin(node)
            self.LRUCache[key] = value
            self.LRUNode[key] = node
        else:
            if len(self.LRUCache.keys()) >= self.capacity:
                x = self.removeAtEnd()
                del self.LRUCache[x]
                del self.LRUNode[x]
            node = DLL(key)
            self.insertAtBegin(node)
            self.LRUCache[key] = value
            self.LRUNode[key] = node
