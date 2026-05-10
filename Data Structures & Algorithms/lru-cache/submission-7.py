class ListNode:
    def __init__(self, key=0, val=0, next=None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(key)
            self.insert(key)
            return self.cache[key].val


    def remove(self, key):
        curNode = self.cache[key]
        prev, nxt = curNode.prev, curNode.next
        prev.next = nxt
        nxt.prev = prev
        

    def insert(self, key):
        #insert right
        curNode = self.cache[key]
        oldPrev = self.right.prev
        oldPrev.next = curNode
        self.right.prev = curNode
        curNode.next = self.right
        curNode.prev = oldPrev


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        newNode = ListNode(key, value)
        self.cache[key] = newNode
        self.insert(key)
        if len(self.cache) > self.cap:
            tmp = self.left.next
            self.remove(tmp.key)
            del self.cache[tmp.key]