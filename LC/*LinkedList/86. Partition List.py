# https://leetcode.com/problems/partition-list/discuss/29174/Python-concise-solution-with-dummy-nodes.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = left_head = ListNode(None)
        right = right_head = ListNode(None)
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        right.next = None
        left.next = right_head.next
        return left_head.next