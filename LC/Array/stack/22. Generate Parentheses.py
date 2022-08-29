#https://leetcode.cn/problems/generate-parentheses/solution/shou-hua-tu-jie-gua-hao-sheng-cheng-hui-su-suan-fa/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(op, clo):
            if op == clo == n:
                res.append(''.join(stack))
                return

            if op < n:
                stack.append('(')
                backtrack(op + 1, clo)
                stack.pop()

            if clo < op:
                stack.append(')')
                backtrack(op, clo + 1)
                stack.pop()

        backtrack(0, 0)
        return res





























