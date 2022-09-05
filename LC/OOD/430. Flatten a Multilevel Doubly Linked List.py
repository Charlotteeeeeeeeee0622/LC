"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        dummy.next = head
        while head:
            if not head.child:
                head = head.next
            else:
                tmp = head.next # 4 # 9
                cNode = self.flatten(head.child) # 7 新开节点 # 11 新开节点
                head.next = cNode # head是8
                cNode.prev = head # 8和11
                head.child = None # 把8的child去掉
                while head.next:# 9,10
                    head = head.next
                head.next = tmp # 10的next是 4
                if tmp:
                    tmp.prev = head # 10 接着 4
                head = head.next
        return dummy.next


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                nxt = curr.next  # 4 # 9
                child = curr.child  # 7 # 11

                curr.next = child  # 3->7 # 8->11
                curr.child = None
                child.prev = curr  # 7->3 # 11->8

                while child.next:
                    child = child.next  # 10 # 12

                if nxt:
                    nxt.prev = child  # 4.prev=10 # 9.prev=12

                child.next = nxt  # 10.next=4 # 12.next=9

            else:
                curr = curr.next  # 8 # 12

        return head