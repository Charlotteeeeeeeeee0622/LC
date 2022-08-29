class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(n, i, visited):
            if i > n: return 1
            ans = 0
            for num in range(1, n + 1):
                if not visited[num] and (num % i == 0 or i % num == 0):
                    visited[num] = True
                    ans += dfs(n, i + 1, visited)
                    visited[num] = False
            return ans

        return dfs(n, 1, [False] * (n + 1))

