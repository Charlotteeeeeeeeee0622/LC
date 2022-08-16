class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res=[]
        r=float('INF')
        def build(root):
            if root==None:
                return 0
            build(root.left)
            res.append(root.val)
            build(root.right)
            #返回值
            return res
        build(root)
        for i in range(0,len(res)-1):
            #绝对值
            r=min(abs(res[i]-res[i+1]),r)
        return r