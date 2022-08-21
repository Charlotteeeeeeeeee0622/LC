# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        if len(lists) == 1: return lists[0]

        def mergeTwo(x: ListNode, y: ListNode) -> ListNode:
            if not x: return y
            if not y: return x
            if x.val > y.val: x, y = y, x
            x.next = mergeTwo(x.next, y)
            return x

        mid = len(lists) // 2  # 0123->2, 012->1
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return mergeTwo(l, r)i

        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        class Solution:
            def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
                def merge(l1, l2):
                    if not l1:
                        return l2
                    if not l2:
                        return l1
                    # [1,2,3] [4,6]
                    if l1.val > l2.val:
                        l1, l2 = l2, l1
                    l1.next = merge(l1.next, l2)
                    return l1

                if not lists:
                    return None
                if len(lists) == 1:
                    return lists[0]

                # o(nlogn)
                # [1,4,5]
                # l1 [1,3,4]
                # l2 [2,6]
                mid = len(lists) // 2
                l1 = self.mergeKLists(lists[:mid])
                l2 = self.mergeKLists(lists[mid:])
                return merge(l1, l2)