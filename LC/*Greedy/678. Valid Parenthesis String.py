class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '*':
                stack.append('(')
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False

        stack = []
        for c in s[::-1]:
            if c == ')' or c == '*':
                stack.append(')')
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False

        return True