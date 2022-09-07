# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Beat 90%+
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the previous for the head is None
        prev = None
        # iterate the nodes
        while head:
            cur = head
            # save the next node to iterate
            head = head.next
            # change the pointer
            cur.next = prev
            # move forward
            prev = cur
        return prev
            
            
            