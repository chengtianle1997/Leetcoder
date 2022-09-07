
# Recursive
class Solution:
    def traversal(self, root):
        if root.left:
            self.traversal(root.left)
        self.list.append(root.val)
        if root.right:
            self.traversal(root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.list = []
        if not root:
            return self.list
        self.traversal(root)
        return self.list

# Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            res.append(node.val)
            right = node.right
            while right:
                stack.append(right)
                right = right.left     
        return res

# A pattern for the three kinds of traversals
# we can use a stack to simulate the recursive process

# In-order traversal: left -> root -> right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else: 
                    # left -> root -> right --- right -> root ->left
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res

# This solution is easy to be adapted to other traversals such as pre-order and post order.
# As for pre-order traversal, the 'visited' signal is unnecessary.