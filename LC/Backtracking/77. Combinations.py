# ——————————————Solution1————————————————
# https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html#%E5%89%AA%E6%9E%9D%E4%BC%98%E5%8C%96
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 回溯返回值和参数
        result = []
        path = []
        def backtracking(n, k, startidx):
            if len(path) == k:
                result.append(path[:])
                return

            # 剪枝， 最后k - len(path)个节点直接构造结果，无需递归
            last_startidx = n - (k - len(path)) + 1
            result.append(path + [idx for idx in range(last_startidx, n + 1)])

            for x in range(startidx, last_startidx):
                path.append(x)
                backtracking(n, k, x + 1)  # 递归
                path.pop()  # 回溯

        backtracking(n, k, 1)
        return result


# ——————————————Solution2————————————————
# https://leetcode.com/problems/combinations/discuss/844096/Backtracking-cheatsheet-%2B-simple-solution
class Solution:
    def combine(self, n, k):
        sol = []

        def backtrack(remain, comb, nex):
            # solution found
            if remain == 0:
                sol.append(comb.copy())

            # iterate through all possible candidates
            for i in range(nex, n + 1):
                # add candidate
                comb.append(i)
                # backtrack
                backtrack(remain - 1, comb, i + 1)
                # remove candidate
                comb.pop()

        backtrack(k, [], 1)
        return sol


# ——————————————Solution3————————————————
# https://leetcode.com/problems/combinations/discuss/26990/Python-easy-to-understand-DFS-solution
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(nums, k, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(len(nums)):
                backtracking(nums[i + 1:], k, path + [nums[i]])

        res = []
        nums = list(range(1, n + 1))
        backtracking(nums, k, [])
        return res
