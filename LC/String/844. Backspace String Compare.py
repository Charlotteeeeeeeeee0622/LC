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


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getchar(string):
            stack = []
            for c in string:
                if c != '#':
                    stack.append(c)
                elif stack and c == '#':
                    stack.pop()

            return stack

        stack1 = getchar(s)
        stack2 = getchar(t)
        if stack1 == stack2:
            return True
        else:
            return False
