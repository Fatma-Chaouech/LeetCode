# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # memorize the first value of the subroot
        # search for each occurence of that value in the root
            # when found, apply the "sameTree" algorithm
            # If False, continue searching, else return True
        
        
        subRoot_value = subRoot.val
        def sameTree(p, q):
            
            if not p and not q:
                return True
            
            if p and q:
                return p.val == q.val and sameTree(p.right, q.right) and sameTree(p.left, q.left)
            
            return p is q
        
        
        def search_value(p, value, q):
            if not p:
                return False
            
            if p.val == value:
                if sameTree(p, q):
                    return True
            
            return search_value(p.right, value, q) or search_value(p.left, value, q)
            
        
        return search_value(root, subRoot_value, subRoot)
        