# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ——————————————Solution1————————————————

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getdepth(root) == -1:
            return False
        else:
            return True

    def getdepth(self, root):
        if root == None:
            return 0
        # 判断self.getdepth是否-1
        # 不为-1就把值赋过去
        elif (left := self.getdepth(root.left)) == -1:
            return -1
        elif (right := self.getdepth(root.right)) == -1:
            return -1
        elif abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

# ——————————————Solution2————————————————
class Solution(object):
    def isBalanced(self, root):

        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

