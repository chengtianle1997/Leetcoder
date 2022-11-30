# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findValue(self, root, x):
        res = self.search(root, root, 0, x)
        return res[0], res[1]
    
    def search(self, par, node, step, x):
        if node:
            if x != node.val:
                left = self.search(node, node.left, step + 1, x)
                right = self.search(node, node.right, step + 1, x)
                if left:
                    return left
                if right:
                    return right
            if x == node.val:
                return [par, step]
        else:
            return None
        
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        par_x, step_x = self.findValue(root, x)
        par_y, step_y = self.findValue(root, y)
        
        if par_x != par_y and step_x == step_y:
            return True
        else:
            return False