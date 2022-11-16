# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        to_visit = deque()
        if root:
            to_visit.append(root)
        length = 0
        while to_visit:
            
            for i in range(len(to_visit)):
                
                node = to_visit.popleft()
                if node.right :
                    to_visit.append(node.right)
                if node.left :
                    to_visit.append(node.left)
                    
            length += 1
        return length
            
            
            
            