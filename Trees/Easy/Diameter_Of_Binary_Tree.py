# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):

            nonlocal res
            
            if not root :
                return 0
            d2 = dfs(root.left)
            d1 = dfs(root.right)

            res = max(res, d2 + d1)
            return 1 + max(d1 , d2)
        
        dfs(root)
        
        return res
    