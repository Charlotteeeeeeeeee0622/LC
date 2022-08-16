class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -float("INF")
        leftmost_val = 0

        def traverse(root, cur_depth):
            #
            nonlocal leftmost_val, max_depth

            if (root.left == None) and (root.right == None):
                if cur_depth > max_depth:
                    max_depth = cur_depth
                    leftmost_val = root.val

            if root.left != None:
                cur_depth += 1
                traverse(root.left, cur_depth)
                cur_depth -= 1

            if root.right != None:
                cur_depth += 1
                traverse(root.right, cur_depth)
                cur_depth -= 1

        traverse(root, 0)
        return leftmost_val
