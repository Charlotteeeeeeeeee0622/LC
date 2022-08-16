# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 找到mid,要么是正中间，要么是中间偏右边
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 后半边交换
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # 前半个链表和后半个链表merge
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next