"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """

        if not root:
            return None
        cur  = root
        next = root.left

        while cur.left :
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next
                next = cur.left


class Solution(object):
    def connect(self, root):
        def dfs(root):
            if root == None:
                return
            left = root.left
            right = root.right
            while left:
                left.next = right
                left = left.right
                right = right.left
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root