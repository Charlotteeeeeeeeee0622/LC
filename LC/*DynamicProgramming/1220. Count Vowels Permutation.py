# https://leetcode.com/problems/count-vowels-permutation/discuss/398286/Simple-Python-(With-Diagram)
# ——————————————Solution1————————————————
def countVowelPermutation(self, n: int) -> int:
    MODULO = 10 ** 9 + 7
    dp = [1] * 5  # number of string end at character i, with i=[a, e, i, o, u]
    for _ in range(1, n):
        a, e, i, o, u = dp
        dp[0] = (e + i + u) % MODULO
        dp[1] = (a + i) % MODULO
        dp[2] = (e + o) % MODULO
        dp[3] = i % MODULO
        dp[4] = (i + o) % MODULO

    return sum(dp) % MODULO


# ——————————————Solution2————————————————
def count_vowel_permutations(n):
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(n - 1):
        a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
    return (a + e + i + o + u) % (10 ** 9 + 7)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a
        return (a + e + i + o + u) % (10**9 + 7)

# similar questions:
# 552 . Student Attendance Record II
# 935 . Knight Dialer
