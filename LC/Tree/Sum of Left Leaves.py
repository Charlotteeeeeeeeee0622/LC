class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        current_value = 0

        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)

        if root.left != None and root.left.left == None and root.left.right == None:
            current_value += root.left.val

        return current_value + left + right