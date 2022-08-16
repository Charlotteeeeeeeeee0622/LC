class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for items in tokens:
            if items not in {'+', '-', '*', '/'}:
                stack.append(items)
            else:
                first_ele = stack.pop()
                second_ele = stack.pop()
                stack.append(
                    # f'{}{}{}'
                    int(eval(f'{second_ele}{items}{first_ele}'))
                )
        return int(stack.pop())
