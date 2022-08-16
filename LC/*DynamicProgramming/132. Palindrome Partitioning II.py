class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def valid(path):
            left = 0
            right = len(path) - 1
            while left < right:
                if path[left] == path[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        @lru_cache(None)
        def dp(i):  # s[i..n-1]
            if i == n:
                return 0
            ans = math.inf
            for j in range(i, n):
                if (isPalindrome(i, j)):
                    ans = min(ans, dp(j + 1) + 1)
            return ans

        return dp(0) - 1