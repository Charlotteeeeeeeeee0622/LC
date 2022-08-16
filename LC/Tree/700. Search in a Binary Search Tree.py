class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None or root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)

        if root.val > val:
            return self.searchBST(root.left, val)