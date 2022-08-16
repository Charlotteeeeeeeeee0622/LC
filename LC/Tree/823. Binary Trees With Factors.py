class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        @cache
        def dfs(num):
            res = 1  # 自身
            for i in range(len(arr)):
                if arr[i] >= num:  # 提前退出
                    break
                r = num / arr[i]
                if r in se:
                    res += dfs(r) * dfs(arr[i])  # r 和 arr[i] 是 num 的子结点
            return res

        arr = sorted(arr)
        se = set(arr)
        res = 0
        for a in arr:
            res += dfs(a)
        return res % (10 ** 9 + 7)