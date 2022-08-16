# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ——————————————Solution1————————————————
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur_max = -float('INF')

        def traverse(root):
            nonlocal cur_max

            if root == None:
                return True

            left_is_valid = traverse(root.left)
            if cur_max < root.val:
                cur_max = root.val
            else:
                return False
            right_is_valid = traverse(root.right)

            return left_is_valid and right_is_valid

        return traverse(root)

#改写的，没明白为啥错
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curmax=-float('inf')

        if root==None:
            return True

        left=self.isValidBST(root.left)

        if root.val>curmax:
            curmax=root.val
        else:
            return False

        right=self.isValidBST(root.right)

        return left and right


# ——————————————Solution2————————————————
class Solution:
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)

# 换行小技巧
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor=float('-inf'), ceiling=float('inf')) -> bool:
        if root == None:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        return self.isValidBST(root.left, floor, root.val) \
               and self.isValidBST(root.right, root.val, ceiling)
