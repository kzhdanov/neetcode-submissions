# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        seccond = slow.next
        prev = None
        slow.next = None
        while seccond:
            tmp = seccond.next
            seccond.next = prev
            prev = seccond
            seccond = tmp

        # merge
        first, seccond = head, prev
        while seccond:
            tmp1, tmp2 = first.next, seccond.next
            first.next = seccond
            seccond.next = tmp1
            first = tmp1
            seccond = tmp2
