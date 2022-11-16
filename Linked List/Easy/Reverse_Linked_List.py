# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    _result = 5
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rev(None, head)
        
        
    def rev(self, prev: Optional[ListNode], cur: Optional[ListNode]):
        
        if cur is None:
            return prev
        if cur.next is None:
            cur.next = prev
            self._result = cur
            return cur
        
        self.rev(cur, cur.next)
        cur.next = prev
        
        if prev is None:
            return self._result
        
        