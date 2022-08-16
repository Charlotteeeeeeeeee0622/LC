class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtracking(s, path):
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

            if not s:
                res.append(path)
                return

            # 从i=1开始就可以防止s[:i]invalid，而且s[:i]只能写成这个形式
            for i in range(1, len(s) + 1):
                # 判断在前backtracking在后
                if valid(s[:i]):
                    backtracking(s[i:], path + [s[:i]])

        res = []
        backtracking(s, [])
        return res