# ——————————————Solution1————————————————

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """

        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)

        return res

    def helper(self, s, l, r):

        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        return s[l + 1:r]

# ——————————————Solution2————————————————
class Solution:
    def longestPalindrome(self, s: str) -> str:
        rl = 0
        rr = 0
        n = len(s)
        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n and s[r] == s[l]:
                l -= 1
                r += 1
            if r - l - 1 > rr - rl + 1:
                rl = l + 1
                rr = r - 1

            l = i
            r = i + 1
            while l >= 0 and r < n and s[r] == s[l]:
                l -= 1
                r += 1
            if r - l - 1 > rr - rl + 1:
                rl = l + 1
                rr = r - 1

        return s[rl:rr + 1]
