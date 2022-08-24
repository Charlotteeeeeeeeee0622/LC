if __name__ == '__main__':
    def calculate(s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)
    calculate("3+2*2")

    dic={}
    words=["practice", "makes", "perfect", "coding", "makes"]
    for i, w in enumerate(words):
        dic[w] = dic.get(w, []) + [i]
    print(dic)
