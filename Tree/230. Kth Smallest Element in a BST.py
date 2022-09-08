# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive, O(n^2)
class Solution:
    def counter(self, root):
        if not root:
            return 0
        return 1 + self.counter(root.left) + self.counter(root.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        while root:
            # nodes in the left part
            count = self.counter(root.left)
            
            # if matched
            if count == k - 1:
                return root.val
            elif count >= k:
                return self.kthSmallest(root.left, k)
            else:
                return self.kthSmallest(root.right, k - count - 1)

# Recursive, O(n), in=order traversal
class Solution:
    def traversal(self, root):
        if root.left:
            self.traversal(root.left)
        self.count -= 1
        if self.count == 0:
            self.number = root.val
            return
        if root.right:
            self.traversal(root.right)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.number = 0
        self.traversal(root)
        return self.number