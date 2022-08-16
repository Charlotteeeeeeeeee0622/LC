# ——————————————Solution1————————————————
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        mapping = {}

        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)

        while stack:
            mapping[stack.pop()] = -1

        for n in nums1:
            res.append(mapping[n])

        return res

# ——————————————Solution2————————————————
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using monotonic stack
        mono_stack = []
        # initialize res2
        res2 = {i:None for i in range(len(nums2))}
        for i in reversed(range(len(nums2))):
            while mono_stack and mono_stack[-1] <= nums2[i]:
                mono_stack.pop()
            res2[nums2[i]] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(nums2[i])
        res1 = []
        for i in nums1:
            res1.append(res2[i])
        return res1
