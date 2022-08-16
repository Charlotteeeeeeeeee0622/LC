# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)

        def construct(nums, left, right):
            if left > right:
                return
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = construct(nums, left, mid - 1)
            root.right = construct(nums, mid + 1, right)
            return root

        res = []
        traversal(root)
        return construct(res, 0, len(res) - 1)