class Solution:
    def minRefuelStops(self, target, startFuel, s):
        dp = [startFuel] + [0] * len(s)
        for i in range(len(s)):
            for t in range(i + 1)[::-1]:
                if dp[t] >= s[i][0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])
        for t, d in enumerate(dp):
            if d >= target: return t
        return -1