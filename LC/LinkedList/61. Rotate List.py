# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #         fast,slow=head,head
        #         while k:
        #             fast=fast.next
        #             k-=1
        #         while fast:
        #             slow=slow.next
        #             fast=fast.next
        #         slow.next=None
        #         fast.next=head

        #         return head

        end = head
        length = 1
        if k == 0 or head == None:
            return head

        while end.next != None:
            length += 1
            end = end.next

        end.next = head

        k = k % length
        for i in range(length - k - 1):
            head = head.next

        newhead = head.next
        head.next = None

        return newhead
