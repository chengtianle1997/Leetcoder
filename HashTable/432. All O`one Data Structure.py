class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.table = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # add node between pre_node and next_node
    def _add(self, node, pre_node, next_node):
        pre_node.next = node
        node.next = next_node
        node.prev = pre_node
        next_node.prev = node
        
    # delete node
    def _remove(self, node):
        pre_node, next_node = node.prev, node.next
        pre_node.next = next_node
        next_node.prev = pre_node

    def inc(self, key: str) -> None:
        if key in self.table.keys():
            # increase
            node = self.table[key]
            node.value += 1
            # find a larger element
            node_pre = node.prev
            while node_pre.value < node.value and node_pre.prev is not None:
                node_pre = node_pre.prev
            # insert the node
            self._remove(node)
            self._add(node, node_pre, node_pre.next)
        else:
            # add new key
            new_node = Node(key, 1)
            self.table[key] = new_node
            self._add(self.table[key], self.tail.prev, self.tail)

    def dec(self, key: str) -> None:
        # the key is guaranteed to be existed
        node = self.table[key]
        node.value -= 1
        # check if the node is still valid
        if node.value <= 0:
            # delete the node
            self._remove(node)
            # remove the key from the dict
            del self.table[node.key]
            return
        # find a lower element
        node_next = node.next
        while node_next.value > node.value and node_next.next is not None:
            node_next = node_next.next
        # insert the node
        self._remove(node)
        self._add(node, node_next.prev, node_next)
        
    def getMaxKey(self) -> str:
        # return the first node
        if self.head.next == self.tail or self.head.next is None:
            return ""
        return self.head.next.key

    def getMinKey(self) -> str:
        # return the last node
        if self.tail.prev == self.head or self.tail.prev is None:
            return ""
        return self.tail.prev.key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# Unit test
# obj = AllOne()
# obj.inc('hello')
# obj.inc('goodbye')
# obj.inc('hello')
# print(obj.getMaxKey())
# obj.inc('leet')
# obj.inc('code')
# obj.inc('leet')
# obj.dec('hello')
# obj.inc('leet')
# obj.inc('code')
# obj.inc('code')
# print(obj.getMaxKey())

obj = AllOne()
obj.inc('a')
obj.inc('b')
obj.inc('b')
obj.inc('c')
obj.inc('c')
obj.inc('c')
obj.dec('b')
obj.dec('b')
print(obj.getMinKey())
obj.dec('a')
print(obj.getMaxKey())
print(obj.getMinKey())