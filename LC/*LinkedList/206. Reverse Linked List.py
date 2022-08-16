# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         #先从dummyhead开始
#         cur=head
#         prev=None
#         while(cur!=None):
#             temp=cur.next
#             cur.next=prev
#             prev=cur
#             cur=temp
#         return prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            # head,prev,head.next=head.next,head,prev
            head.next, prev, head = prev, head, head.next

        return prev