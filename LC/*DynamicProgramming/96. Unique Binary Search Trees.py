# https://leetcode.cn/problems/unique-binary-search-trees/solution/hua-jie-suan-fa-96-bu-tong-de-er-cha-sou-suo-shu-b/
# https://programmercarl.com/0096.%E4%B8%8D%E5%90%8C%E7%9A%84%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html#%E6%80%9D%E8%B7%AF
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                # dp[nodes] += dp[root - 1] * dp[nodes - root];
                # root-1 为root为头结点左子树节点数量
                # nodes-root 为以root为头结点右子树节点数量
                # 左边几种形式，右边几种形式，组合起来就是乘法
                dp[nodes] += dp[root - 1] * dp[nodes - root]
        return dp[-1]
