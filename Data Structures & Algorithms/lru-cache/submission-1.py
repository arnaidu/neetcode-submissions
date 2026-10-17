class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity
        self.end = None
        self.start = None

    def get(self, key: int) -> int:     
        if key in self.lru:
            if len(self.lru) > 1:
                self._move_to_end(key)
            return self.lru[key].value
        return -1   

    def put(self, key: int, value: int) -> None:   
        if key in self.lru:
            self.lru[key].value = value
            if len(self.lru) > 1:
                self._move_to_end(key)
            return

        if len(self.lru) == self.capacity:
            del self.lru[self.start.key]
            self.start = self.start.next

            if not self.start:
                self.end = None
            else:
                self.start.prev = None

        node = Node(key, value)

        if not self.end:
            self.end = node
            self.start = node
            self.lru[key] = node
            return

        self.lru[key] = node
        self.end.next = node
        node.prev = self.end
        self.end = node 
    
    def _move_to_end(self, key: int) -> None:
        node = self.lru[key]
        if node == self.end:
            return

        # if node is start, then move to end and handle
        if node == self.start:
            self.start = self.start.next
            self.start.prev = None
        else:
            prev = node.prev
            next_node = node.next
            prev.next, next_node.prev = next_node, prev

        self.end.next = node
        node.prev = self.end
        self.end = node
        node.next = None


class Node:
    def __init__(self, key: int, value: int):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


        
