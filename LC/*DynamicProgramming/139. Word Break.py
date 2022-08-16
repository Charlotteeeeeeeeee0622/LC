class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # 前n个字符是否能由字典组成
        dp = [False] * (len(s) + 1)

        # 初始状态
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i, -1, -1):
                # 转移公式
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]