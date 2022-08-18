class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {']': '[', '}': '{', ')': '('}

        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or stack.pop() != dict[char]:
                    return False
            else:
                return False
        return stack == []


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            if c == ')':
                if not stack or stack.pop() != '(':
                    return False
            if c == ']':
                if not stack or stack.pop() != '[':
                    return False
            if c == '}':
                if not stack or stack.pop() != '{':
                    return False

        return True if not stack else False
