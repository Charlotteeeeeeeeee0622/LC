class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(path, l, r):
            if l == 0 and r == 0:
                res.append(path)
                return

                # 还剩下的右括号一定不能比左括号多，不然（（）））
            if r < l:
                return

            if l > 0:
                dfs(path + '(', l - 1, r)

            if r > 0:
                dfs(path + ')', l, r - 1)

        res = []
        dfs('', n, n)
        return res