# Definition for a binary tree node.
# class TreeNode:\U0001f60d\U0001f60d
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms

# ——————————————Solution1————————————————
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, 1, res)
        return res

    def dfs(self, root, depth, res):
        if root == None:
            return []

        if len(res) < depth:
            res.append(root.val)

        # 遍历右子树
        if root.right:
            self.dfs(root.right, depth + 1, res)

        # 遍历左子树
        if root.left:
            self.dfs(root.left, depth + 1, res)

# ——————————————Solution2————————————————


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def collect(root, depth):
            if root == None:
                return
            if len(res) == depth:
                res.append(root.val)

            collect(root.right, depth + 1)
            collect(root.left, depth + 1)

        res = []
        collect(root, 0)
        return res

   # 迭代没明白，这啥被方法

    #         res = []
    #         q = collections.deque([root])

    #         while q:
    #             rightSide = None
    #             qLen = len(q)

    #             for i in range(qLen):
    #                 node = q.popleft()
    #                 if node:
    #                     rightSide = node
    #                     q.append(node.left)
    #                     q.append(node.right)
    #             if rightSide:
    #                 res.append(rightSide.val)
    #         return res