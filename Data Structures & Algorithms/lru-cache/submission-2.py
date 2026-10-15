class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        
        node = self.hash_map[key]
        self.remove_node(node)
        self.append_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].val = value
            self.get(key)
            return

        new_node = Node(key=key, val=value)
        if len(self.hash_map) == self.capacity:
            lru_node = self.head.next
            self.remove_node(lru_node)

            del self.hash_map[lru_node.key]
        
        self.append_node(new_node)
        self.hash_map[key] = new_node


    def remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def append_node(self, new_node: Node) -> None:
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node

        new_node.next = self.tail
        self.tail.prev = new_node
"""
size = 2

hash_map of current one still the cache
key -> actual node

double linked list
head                                            tail
least -used         x       ->      x         recently used
                    3,30            2,20


1, 1        > 2, 2      >       4,4
"""