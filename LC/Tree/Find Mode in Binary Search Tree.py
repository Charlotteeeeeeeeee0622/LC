class Solution:
    def __init__(self):
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.result = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return None
        self.BST(root)
        return self.result

    def BST(self, cur):
        if cur == None: return None

        self.BST(cur.left)

        if self.pre == None:
            self.count = 1

        elif self.pre.val == cur.val:
            self.count += 1

        else:
            self.count = 1

        self.pre = cur

        if self.count == self.max_count:
            self.result.append(cur.val)

        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [cur.val]

        self.BST(cur.right)