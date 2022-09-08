# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue, res = [], []
        if not root:
            return res
        
        queue.append(root)
        counter = 1
        
        while queue:
            node = queue.pop(0)
            counter -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if counter == 0:
                res.append(node.val)
                counter = len(queue)
        
        return res
        