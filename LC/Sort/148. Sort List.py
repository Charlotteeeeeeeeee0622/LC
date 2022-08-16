# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(second)

        return self.merge(l, r)

    def merge(self, l, r):
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

