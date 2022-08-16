# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traversal(nums, 0, len(nums))

    def traversal(self, nums, begin, end):
        if begin == end:
            return None

        max_index = begin
        for i in range(begin, end):
            if nums[i] > nums[max_index]:
                max_index = i

        root = TreeNode(nums[max_index])

        # pay attention to how to traverse
        root.left = self.traversal(nums, begin, max_index)
        root.right = self.traversal(nums, max_index + 1, end)

        return root