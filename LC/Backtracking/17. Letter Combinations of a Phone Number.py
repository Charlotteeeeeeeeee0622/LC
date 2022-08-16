# ——————————————Solution1————————————————
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtracking(i, cur):
            if i == len(digits):
                if len(cur) > 0:
                    res.append(''.join(cur))
                return
                # if len(cur)==len(digits):
                res.append(''.join(cur))
            # 2 3
            for char in digitsmap[digits[i]]:
                # a d
                cur.append(char)
                # 
                backtracking(i + 1, cur)
                cur.pop()

        res = []
        backtracking(0, [])
        return res


# ——————————————Solution2————————————————
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 组合问题

        def backtracking(m, digits, path):
            if not digits:
                res.append(path)
                return
            for char in m[digits[0]]:
                backtracking(m, digits[1:], path + char)

        m = {"2": "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []
        if not digits:
            return res
        backtracking(m, digits, '')
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 组合问题

        def backtracking(digits, digitsmap, path):
            if not digits:
                return
            for char in digitsmap[digits[0]]:
                backtracking(digits[1:], digitsmap, path + char)

        res = []
        backtracking(digits, digitsmap, [])
        return res
