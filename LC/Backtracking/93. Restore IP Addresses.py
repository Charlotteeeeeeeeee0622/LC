class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtracking(s, ind, path):

            if ind == 4 and not s:
                # 不能把最后一个点算进去
                res.append(path[:-1])
                return

            for i in range(1, len(s) + 1):
                if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                    backtracking(s[i:], ind + 1, path + s[:i] + '.')

        res = []
        backtracking(s, 0, "")
        return res