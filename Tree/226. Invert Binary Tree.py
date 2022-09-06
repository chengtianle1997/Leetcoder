# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
class Solution:
    def invert(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invert(root.left)
        self.invert(root.right)
        return root
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)

# Iterative Solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = []
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            # invert
            node.left, node.right = node.right, node.left
            # push left and right nodes into the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root