# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return []
        
        queue = []
        queue.append(root)
        res = []

        while queue:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
        
        # delete the last nulls
        while not res[-1]:
            res = res[:-1]
        
        return res
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        queue = []
        root = TreeNode(data[0])
        queue.append(root)
        idx = 1
        
        while queue and idx < len(data):
            node = queue.pop(0)
            # check the child of the node
            if idx < len(data):
                val = data[idx]
                if val:
                    left = TreeNode(val)
                    node.left = left
                    queue.append(left)
            if idx + 1 < len(data):
                val = data[idx + 1]
                if val:
                    right = TreeNode(val)
                    node.right = right
                    queue.append(right)
            # update idx
            idx += 2
        
        return root
            
            
        
        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize([1, 2, 3, None, None, 4, 5])
print(deser.serialize(ans))



# Recursive Solution
class CodecRecur:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root:
            return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)     
        else:
            return 'None'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def traversal(queue):
            if not queue:
                return None
            node = queue.pop(0)
            if node != 'None':
                return TreeNode(int(node), traversal(queue), traversal(queue))
            else:
                return None
        
        return traversal(data.split(','))


