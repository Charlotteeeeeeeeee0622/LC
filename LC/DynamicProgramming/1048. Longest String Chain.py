class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        words = ["a","b","ba","bca","bda","bdca"]
        1. word = "a", prev = "", dp = {"a": 1}; It means that ending with "a", the max size of chain is 1.
        2. word = "b", prev = "", dp = {"a": 1, "b": 1}; It means that ending with "b", the max size of chain is 1.
        3. word = "ba", prev = "a" or "b", dp = {"a": 1, "b": 1, "ba": 2};
            It means that ending with "ba", the max size of chain is 2.
            Here, both "a" and "b" can be the predecessor. We are interested only in length not the actual chain!
        4. word = "bca", prev = "ba", dp = {"a": 1, "b": 1, "ba": 2, "bca":3};
            It means that ending with "bca", the max size of chain is 3.
        5. word = "bda", prev = "ba", dp = {"a": 1, "b": 1, "ba": 2, "bca":3, "bda": 3};
            It means that ending with "bda", the max size of chain is 3.
        6. word = "bdca", prev = "bda" or "bca", dp = {"a": 1, "b": 1, "ba": 2, "bca":3, "bda": 3, "bdca": 4};
            It means that ending with "bdca", the max size of chain is 4.
        """
        dp = {}
        res = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
                    res = max(res, dp[word])
        return res
