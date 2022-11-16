# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = None
        if list1 is None and list2 is None:
            return None
        
        if list1 is None:
            result = list2
            result.next = self.mergeTwoLists(list1, list2.next)
        
        elif list2 is None:
            result = list1
            result.next = self.mergeTwoLists(list1.next, list2)
        
        elif list1.val > list2.val:
            result = list2
            result.next = self.mergeTwoLists(list1, list2.next)
        else :
            result = list1
            result.next = self.mergeTwoLists(list1.next, list2)
        return result
