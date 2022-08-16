# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 没找到要删除的节点
        if root == None: return root
        # 左右孩子都为空，直接删除节点，返回NULL为空节点
        if root.val == key and root.left == None and root.right == None:
            del root
            return None
        # 其左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
        if root.val == key and root.left == None and root.right != None:
            temp = root
            root = root.right
            del temp
            return root
        # 其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
        if root.val == key and root.left != None and root.right == None:
            temp = root
            root = root.left
            del temp
            return root
        # 左右孩子都不为空
        if root.val == key and root.left != None and root.right != None:
            v = root.right
            while v.left:
                v = v.left
            v.left = root.left
            temp = root
            root = root.right
            del temp
            return root
        if root.val > key: root.left = self.deleteNode(root.left, key)
        if root.val < key: root.right = self.deleteNode(root.right, key)
        return root
