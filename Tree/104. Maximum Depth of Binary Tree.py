# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # check root
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        
# Iterative Solution, which is faster
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        # create a queue
        queue = []
        queue.append((root, 1))
        
        max_depth = 0
        
        # iterate through the tree
        while queue:
            node, depth = queue.pop(0)
            if depth > max_depth:
                max_depth = depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth
            
            
            
        