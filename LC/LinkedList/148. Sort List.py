# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, l: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l, r):
            if l is None:
                return r
            elif r is None:
                return l

            dummy = ListNode(0)
            head = dummy

            while l and r:
                if l.val <= r.val:
                    head.next = l
                    l = l.next
                else:
                    head.next = r
                    r = r.next
                head = head.next

            head.next = l if r is None else r

            return dummy.next

        # edge case
        if not l or not l.next: return l

        # divide it into two part
        fast = l.next;
        slow = l
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        # every two nodes
        l = self.sortList(l)
        r = self.sortList(second)

        return merge(l, r)
