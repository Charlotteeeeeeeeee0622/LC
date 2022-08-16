# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # 初始值为0
        self.pre = TreeNode()

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root)
        return root

    def traversal(self, root: TreeNode):
        if root == None:
            return None

        self.traversal(root.right)

        root.val += self.pre.val
        self.pre = root

        self.traversal(root.left)
