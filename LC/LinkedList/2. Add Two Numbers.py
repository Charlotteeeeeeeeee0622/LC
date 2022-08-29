# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=None)
        # 指针
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            # 先给l1和l2赋值
            # 防止不一样长，要有if else
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            # 先定义一个头存val，在用cur.next=这个头
            head = ListNode(val)
            cur.next = head
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next