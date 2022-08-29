# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, l: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1
            # [1,3,4] [2,6]
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = merge(l1.next, l2)
            return l1

        if not l:
            return None
        if len(l) == 1:
            return l[0]

        # l1[1,4,5]
        # l21 [1,3,4]
        # l22 [2,6]
        mid = len(l) // 2
        l1 = self.mergeKLists(l[:mid])
        l2 = self.mergeKLists(l[mid:])
        return merge(l1, l2)