"""
1. 根据题意，最大波动值只由 s 中的两种字符决定，至于是哪两种我们还不知道，我们可以枚举这两种字符的所有可能值。
    由于 s 只包含小写字母，我们可以从 26 个小写字母中选出 2 个不同的字母
    并假设这两个字母为答案子串中出现次数最多的和最少的
    这一共需要枚举26*25=650 种不同的字母组合。
2.假设出现次数最多的字符为 a，出现次数最少的字符为 b。
    由于题目求的是这两个字符出现次数的差，我们可以把 a 视作 1，b 视作 −1，其余字符视作 0
3.注意 a 和 b 必须都出现在子串中，不能把只有 a 的子串作为答案。
    我们可以用变量 diff 维护 a 和 b 的出现次数之差，初始值为 0。
    同时用另一个变量 diffWithB 维护包含了 b 的 a 和 b 的出现次数之差，初始为 -∞，因为还没有遇到 b。
    遍历字符串 s：
        当遇到a时，diff 和 diffWithB 均加一。
        当遇到b时，diff减一，diffWithB记录此时的diff值。若diff为负则将其置为0.
    统计所有diffWithB的最大值，即为答案。若s只有一种字符则答案为0.
"""
from itertools import permutations
from math import inf
from string import ascii_lowercase


if __name__ == '__main__':
    def largestVariance(s: str) -> int:
        if s.count(s[0]) == len(s):
            return 0
        ans = 0
        diff = [[0] * 26 for _ in range(26)]
        diff_with_b = [[-inf] * 26 for _ in range(26)]
        for ch in s:
            ch = ord(ch) - ord('a')
            for i in range(26):
                if i == ch:
                    continue
                diff[ch][i] += 1  # a=ch, b=i
                diff_with_b[ch][i] += 1
                diff[i][ch] -= 1  # a=i, b=ch
                diff_with_b[i][ch] = diff[i][ch]
                if diff[i][ch] < 0:
                    diff[i][ch] = 0
                ans = max(ans, diff_with_b[ch][i], diff_with_b[i][ch])
        return ans
    largestVariance('aababbb')
