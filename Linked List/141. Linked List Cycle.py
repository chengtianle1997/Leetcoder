# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        # fast and slow pointers
        fast = head
        slow = head
        # check only the path fast pointer is valid, 
        # then the slow pointer will point to these positions repeatedly
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
        