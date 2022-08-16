#https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        dummy=ListNode(None,next=head)
        p=dummy
        for i in range(left-1):
            p=p.next
        tail=p.next
        for i in range(right-left):
            temp=p.next
            p.next=tail.next
            tail.next=tail.next.next
            p.next.next=temp
        return dummy.next