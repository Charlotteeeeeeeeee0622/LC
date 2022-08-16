class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # 温度低的要了也没啥用
                T, Ind = stack.pop()
                # 输出的都是index差，这里进行index操作
                res[Ind] = i - Ind

            stack.append([t, i])
        return res
