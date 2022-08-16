class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            # walk through i and previous
            for j in range(i + 1):
                # dp[j+1][i-1] denotes the previous one
                # which means if the right pointer moves one step to the left
                # and the left pointer moves one step to the right
                # the string is palindr
                # it is necessary
                # i-j<2 denotes a condition where only two chars or one char
                if s[j] == s[i] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    res += 1

        return res