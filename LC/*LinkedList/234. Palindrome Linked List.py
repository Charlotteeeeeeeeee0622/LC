# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            # pre记录反转的前半个列表，slow一直是原表一步步走

            slow = slow.next
            fast = fast.next.next

        if fast:  # 长度是奇数还是偶数对应不同情况
            slow = slow.next

        prev = None
        cur = slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        first = head
        second = prev
        while second:
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                return False
        return True