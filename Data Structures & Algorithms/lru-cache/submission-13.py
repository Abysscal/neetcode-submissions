class DoublyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = DoublyNode(0,0), DoublyNode(0,0) 
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        
    def insert(self, node):
        #insert to the MRU
        prev = self.right.prev
        prev.next, self.right.prev = node, node
        node.prev, node.next = prev, self.right
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = DoublyNode(key, value)
        self.cache[key] = newNode
        self.insert(newNode)
        if self.cap < len(self.cache):
            tmp = self.left.next
            self.remove(tmp)
            del self.cache[tmp.key]
        
            
      