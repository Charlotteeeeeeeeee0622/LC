# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyhead = ListNode(val=None, next=head)

        fast = head
        while n:
            fast = fast.next
            n -= 1

        # 不能用head,不然需要while fast.next,而fast为None时候，没有next这个属性
        slow = dummyhead
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        # 不能返回head，如果只有一个元素，经过slow.next=slow.next.next这个元素就没了，如果返回head，就还有一个元素，实际上是[]
        return dummyhead.next
