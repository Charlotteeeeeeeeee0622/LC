# ——————————————Solution1————————————————

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = nums[::-1]
        ret = []
        for n in reversed(nums):
            while stack and stack[-1] <= n:
                stack.pop()
            ret.append(stack[-1] if stack else -1)
            stack.append(n)
        return ret[::-1]


# ——————————————Solution2————————————————
#https://leetcode.cn/problems/next-greater-element-i/solution/dan-diao-zhan-jie-jue-next-greater-number-yi-lei-w/
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 给stack先赋值来代表创建环形数组
        stack = nums[::-1]
        res = []
        for n in reversed(nums):
            while stack and stack[-1] <= n:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(n)
        return res[::-1]