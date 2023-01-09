import collections
# solution using built-in datatype OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict([])
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# same concept, but with user-defined node class for DLL
class Node:
    def __init__(self, key, value, next_node=None, prev_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

class LRUCache:

    def __init__(self, capacity):
        self.cache = {} # key:node pairs
        self.capacity = capacity
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.tail.prev_node = self.head
        self.head.next_node = self.tail

    def get(self, key):
        if key not in self.cache:
            return -1
        
        current_node = self.cache[key]
        
        self.moveToTail(current_node)

        return current_node.value
    
    def moveToTail(self, current_node):
        if current_node.next_node is self.tail:
            print("same")
            return

        # remove current_node from starting position
        current_node.prev_node.next_node = current_node.next_node
        current_node.prev_node.next_node.prev_node = current_node.prev_node

        # place it in back
        current_node.next_node = self.tail
        self.tail.prev_node.next_node = current_node
        current_node.prev_node = self.tail.prev_node
        self.tail.prev_node = current_node

    def addNewNode(self, new_node):
        self.size += 1

        new_node.next_node = self.tail
        self.tail.prev_node.next_node = new_node
        new_node.prev_node = self.tail.prev_node
        self.tail.prev_node = new_node

    def popNodeLeft(self):
        if self.size < 1:
            return None

        self.size -= 1

        popped_node = self.head.next_node
        self.head.next_node = popped_node.next_node
        self.head.next_node.prev_node = self.head

        return popped_node

    def put(self, key, value):
        if key in self.cache:
            current_node = self.cache[key]
            current_node.value = value
            self.moveToTail(current_node)
        else:
            if self.size == self.capacity:
                popped_key = self.popNodeLeft().key
                del self.cache[popped_key]
            
            current_node = Node(key, value)
            self.addNewNode(current_node)
            self.cache[key] = current_node