# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def depth(root):
            if root is None:
                return 0
            
            return 1 + max(depth(root.left), depth(root.right))
        
        
        if not root:
            return True
        return abs(depth(root.left) - depth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        