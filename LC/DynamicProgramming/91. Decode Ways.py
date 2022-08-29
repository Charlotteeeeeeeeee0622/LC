class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        if s[0] == '0':
            return 0

        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            if s[i] == '0':  # the condition where s[i]=0
                if s[i - 1] == '1' or s[i - 1] == '2':
                    # 由于s[1]指第二个下标，对应为dp[2],所以dp的下标要比s大1，故为dp[i+1]
                    dp[i + 1] = dp[i - 1]

                else:
                    return 0
            else:  # the condition where s[i]!=0
                if (s[i - 1] == '1') or (s[i - 1] == '2' and s[i] <= '6'):
                    # the number of methods of dp[i+1] is composed of two part:
                    # part one : s[i] one digit
                    # part two: s[i-1],s[i] two digits
                    dp[i + 1] = dp[i - 1] + dp[i]
                else:
                    dp[i + 1] = dp[i]
        return dp[len(s)]