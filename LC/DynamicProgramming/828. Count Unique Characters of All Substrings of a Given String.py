class Solution:
    def uniqueLetterString(self, s: str) -> int:
        idx, dp, ans = {}, 0, 0
        for i, c in enumerate(s):
            # j是s[i]上次出现的位置，k是s[i]上上次出现的位置
            j, k = idx.get(c, [-1, -1])
            dp = dp + (i-j) - (j-k)
            ans += dp
            idx[c] = [i, j]

        return ans