from typing import Optional
import typing


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def isornot(root: object, targetSum: object) -> object:
            if root.left == None and root.right == None and targetSum == 0:
                return True

            if (not root.left) and (not root.right):
                return False  # 遇到叶子节点，计数不为0

            if root.left != None:
                targetSum -= root.left.val
                if isornot(root.left, targetSum): return True
                targetSum += root.left.val

            if root.right != None:
                targetSum -= root.right.val
                if isornot(root.right, targetSum): return True
                targetSum += root.right.val

            return False

        if root == None:
            return False
        else:
            #
            return isornot(root, targetSum - root.val)
