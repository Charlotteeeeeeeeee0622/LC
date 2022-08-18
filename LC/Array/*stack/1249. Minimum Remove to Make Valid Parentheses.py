class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        res = []
        for c in s:
            if c.isalnum():
                res.append(c)

            elif c == '(' or c == '{' or c == '[':
                stack.append(c)
                res.append(c)

            elif c == ']':
                if not stack or stack.pop() != '[':
                    continue
                res.append(c)
            elif c == '}':
                if not stack or stack.pop() != '{':
                    continue
                res.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    continue
                res.append(c)

        return res if not stack else ''
