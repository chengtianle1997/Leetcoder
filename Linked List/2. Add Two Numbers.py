# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p, q = l1, l2
        sum = 0
        head = ListNode()
        pre, cur = head, None
        while l1 or l2 or sum > 0:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            # output
            this = sum % 10
            sum = sum // 10
            cur = ListNode(this)
            pre.next = cur
            pre = cur
        return head.next
            
                