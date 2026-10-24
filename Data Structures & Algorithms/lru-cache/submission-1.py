class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} 

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            new = Node(key, value)
            self.cache[key] = new
            self.insert(self.cache[key])

        self.cache[key].value = value

        if len(self.cache) > self.cap:
            temp = self.left.next
            self.remove(temp)
            del self.cache[temp.key]

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev = self.right.prev   
        prev.next = node
        self.right.prev = node
        node.prev = prev
        node.next = self.right

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
