# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self,root):
        nodes = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, pos = queue.popleft()
            if not node:
                continue
            nodes[pos].append(node.val)
            queue.append((node.left, pos-1))
            queue.append((node.right, pos+1))
        return [nodes[i] for i in sorted(nodes)]

if __name__ == '__main__':
    Solution.verticalOrder([TreeNode(val=3,left=TreeNode(val=9,left=None,right=None),right=TreeNode(val=20,left=TreeNode(val=15,left=None,right=None),right=TreeNode(val=7,left=None,right=None)))])