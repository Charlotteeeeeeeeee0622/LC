# ——————————————Solution1————————————————
# 简化版本
# Apply a recursion function dfs.
# Return 0 if it's a leaf.
# Return 1 if it's a parent of a leaf, with a camera on this node.
# Return 2 if it's covered, without a camera on this node.
#
# For each node,
# if it has a child, which is leaf (node 0), then it needs camera.
# if it has a child, which is the parent of a leaf (node 1), then it's covered.
#
# If it needs camera, then res++ and we return 1.
# If it's covered, we return 2.
# Otherwise, we return 0.

def minCameraCover(self, root):
    self.res = 0

    def dfs(root):
        if not root: return 2
        l, r = dfs(root.left), dfs(root.right)
        if l == 0 or r == 0:
            self.res += 1
            return 1
        return 2 if l == 1 or r == 1 else 0

    return (dfs(root) == 0) + self.res

# ——————————————Solution2————————————————
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 贪心思想： 希望叶子节点的父亲节点 尽量安装摄像头 并且从下到上考虑
        # 本题中节点有三种情况 0 无覆盖 1 有摄像头 2 有覆盖
        # 1.当左右节点都有覆盖时，父亲节点就放心了，就可以没有摄像头了，且无覆盖返回0（因为左右节点都无摄像头当前节点不是有覆盖）
        # 2.当左右节点有一个节点无覆盖，父亲节点就需要提供支援那么就安装摄像头  摄像头数量+1 并且有摄像头返回1
        # 3.当左右节点有一个节点有摄像头，那么当前节点返回有覆盖2
        def traversal(root):
            # 空节点，该节点有覆盖
            # 如果空节点有摄像头，那么叶子节点就是有覆盖的情况了，那么叶子节点的父亲节点就可以不安装摄像，和贪心思路矛盾
            if root == None:  # 当走到空节点的时候，如果空节点无覆盖，那么需要在叶子节点安装摄像头，就和贪心思路矛盾
                return 2  # 故空节点只能是2
            left = traversal(root.left)  # 用后续遍历 可以左右节点都处理完了 处理当前节点
            right = traversal(root.right)
            # 情况1 ，左右节点都有覆盖 只能看到孩子的情况来判断自己 而不能看到爸爸的情况 从下往上
            if left == 2 and right == 2:
                return 0

            # 情况2，有一个节点无覆盖的情况 父节点就需要有摄像头了
            # 例如 1左节点无覆盖 右节点有覆盖
            # 2左节点无覆盖，右节点有摄像头
            # 3左节点无覆盖，右节点无覆盖
            # 4左节点有覆盖，右节点无覆盖
            # 5左节点有摄像头，右节点无覆盖
            if left == 0 or right == 0:
                self.result += 1  # 摄像头数量加1
                return 1
            # 情况2 左右节点有一个节点有摄像头，那么父亲节点就是有覆盖了。
            if left == 1 or right == 1:
                return 2
            # 否则返回-1
            return -1

        self.result = 0  # 全局变量 初始化为0 代表安装摄像头的数量
        # 从下到上 后续遍历 最后遍历到的节点为根节点，函数最终返回的是根节点的情况
        if traversal(root) == 0:  # 如果根节点是无覆盖的情况下，需要将其安装摄像头。
            self.result += 1
        return self.result  # 返回整个二叉树的监控数量