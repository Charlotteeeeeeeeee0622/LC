# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, sum):
        res = []
        ls=[]
        self.dfs(root, sum, ls, res)
        return res

    def dfs(self, root, sum, ls, res):
        if root:
            #最后一层
            if not root.left and not root.right and sum == root.val:
                ls.append(root.val)
                res.append(ls)
            self.dfs(root.left, sum - root.val, ls + [root.val], res)
            self.dfs(root.right, sum - root.val, ls + [root.val], res)

#     def pathSum(self, root: TreeNode, targetsum: int) -> list[list[int]]:
#         def traversal(cur_node, remain):
#             if not cur_node.left and not cur_node.right:
#                 if remain == 0:
#                     result.append(path[:])
#             return

#             if cur_node.left:
#                 path.append(cur_node.left.val)
#                 traversal(cur_node.left, remain-cur_node.left.val)
#                 path.pop()

#             if cur_node.right:
#                 path.append(cur_node.right.val)
#                 traversal(cur_node.right, remain-cur_node.right.val)
#                 path.pop()

#         result, path = [], []
#         if not root:
#             return []
#         path.append(root.val)
#         traversal(root, targetsum - root.val)
#         return result

