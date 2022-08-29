import null as null


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':

    def rob(root: TreeNode) -> int:
        def dfs(node):
            if not node: return 0, 0
            l = dfs(node.left)
            r = dfs(node.right)
            selected = node.val + l[1] + r[1]
            notSelected = max(l[0], l[1]) + max(r[0], r[1])
            return selected, notSelected

        return max(dfs(root))


    rob([3,2,3,null,3,null,1])