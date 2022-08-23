class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # add a new node
    def _add(self, key, value):
        new_node = Node(key, value)
        next_node = self.head.next
        # insert new_node between head and next_node
        new_node.next = next_node
        next_node.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node
        return new_node
    
    # remove the least recent node
    def _remove(self):
        last_node = self.tail.prev
        pre_last_node = last_node.prev
        pre_last_node.next = self.tail
        self.tail.prev = pre_last_node
        # remove the key from the table
        del self.table[last_node.key]
        
    # update a node
    def _update(self, node, new_value):
        # delete the node from the chain
        pre_node = node.prev
        next_node = node.next
        pre_node.next = next_node
        next_node.prev = pre_node
        # add the node to the front
        node = self._add(node.key, new_value)
        return node
        
    def get(self, key: int) -> int:
        if key in self.table.keys():
            # update
            self.table[key] = self._update(self.table[key], self.table[key].value)
            return self.table[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table.keys():
            # update
            self.table[key] = self._update(self.table[key], value)
        else:
            # a new node
            self.table[key] = self._add(key, value)
            # check capacity
            self.capacity -= 1
            if self.capacity < 0:
                # remove the least recent node
                self._remove()
                self.capacity += 1
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)