# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #先确定好两棵树为none的情况
        if root==None:
            return False
        if subRoot==None:
            return True
        #在确定两颗整树相同的情况
        if self.isSame(root,subRoot):
            return True
        #这一步已经不需要了
        # if root==None and subRoot==None:
        #     return True
        #记得是或不是与
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSame(self,p,q):
        if p==None and q==None:
            return True
        if p and q and q.val==q.val:
            return self.isSame(p.left,q.left) and self.isSame(p.right,q.right)
        return False