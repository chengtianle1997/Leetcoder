# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        p, q = head, head
        counter = 0
        
        while q.next and counter < n:
            q = q.next
            counter += 1
            
        if counter < (n - 1):
            # there is not enought nodes in the linked list
            return head
        
        if counter == (n - 1):
            return head.next
        
        while q.next:
            p = p.next
            q = q.next
            
        # remove p.next
        p.next = p.next.next
        
        return head