
# Recursive Solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        
        if (root.val - p.val) * (root.val - q.val) <= 0:
            return root
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # root.val > p.val and root.val > q.val
            return self.lowestCommonAncestor(root.left, p, q)

# Iterative Solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        node = root
        
        while node:
            # check node
            if (node.val - p.val) * (node.val - q.val) <= 0:
                return node
            elif node.val < p.val and node.val < q.val:
                node = node.right
            elif node.val > p.val and node.val > q.val:
                node = node.left
        
        return node