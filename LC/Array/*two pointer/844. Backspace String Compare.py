# https://leetcode.com/problems/backspace-string-compare/discuss/145786/Python-tm
# ——————————————Solution1————————————————
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = self.stack(s, [])
        s2 = self.stack(t, [])

        return s1 == s2

    def stack(self, s, stack):
        for char in s:
            if char != '#':
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack

# ——————————————Solution2————————————————
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r1 = len(s) - 1
        r2 = len(t) - 1

        while r1 >= 0 or r2 >= 0:
            char1 = char2 = ""
            if r1 >= 0:
                char1, r1 = self.getChar(s, r1)
            if r2 >= 0:
                char2, r2 = self.getChar(t, r2)
            if char1 != char2:
                return False
        return True

    # r代表尾部位置
    def getChar(self, s, r):
        char = ''
        count = 0
        while r >= 0 and not char:
            if s[r] == '#':
                count += 1
            elif count == 0:
                char = s[r]
            else:
                count -= 1
            r -= 1
        return char, r