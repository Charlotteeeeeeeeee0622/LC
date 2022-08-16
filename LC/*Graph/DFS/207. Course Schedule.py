"""
记住这三个标志位对应的状态
i == 0 ： 干净的，未被 DFS 访问
i == -1：其他节点启动的 DFS 访问过了，路径没问题，不需要再访问了
i == 1  ：本节点启动的 DFS 访问过了，一旦遇到了也说明有环了

有0、1、2、3、4、5  共6门课程。 [[5,3],[5,4],[3,0],[3,1],[4,1],[4,2]]。学5之前要先学3，学5之前要先学4......

0          邻接表
   \       下标  0     1     2     3    4    5   同时也表示要先学的课程
   /   3        [3]  [3,4]  [4]   [5]  [5]  [ ]  学完上面的课程才能学的课程，例如学完0才能学3，学完1才能学3和4
1        \
   \     /  5     这个邻接表的创建是通过        for(int[] cp : prerequisites)
      4                                           adjacency.get(cp[1]).add(cp[0]);         实现的
   /
2

然后就是遍历+标记判断有无环：

1、从课程0启动DFS，先判断下，哦，节点0还没被访问，将flag[0]置1，表明被当前节点启动的dfs访问过了，在访问0时
就通过以下代码一连串把3、5都访问了,返回true之前标志位置-1，这样从其他节点进来看到标志位-1时就无需再访问了，
直接返回true.
2.从课程1启动DFS一样的道理，3、5上一步已经访问过了标志位为-1，这一步就不访问了，只要访问4，并把标志位置为-1.,
3、剩下的同理。这里是举了个无环的情况，那有环是什么样子呢？
下标  0     1     2     3    4    5   先学的课程
     [3]  [3,4]  [4]   [5]  [5]  [3 ]  这里多加了一个，先学5才能学3，这回肯定就有问题了

在第一步从课程0启动DFS，一连串访问3，5，从5又遍历到3时，由于我们本节点启动的dfs已经访问过3了，标志位为1，
所以碰到标志位为1，说明有环了，直接返回false;一旦某次df返回了false,整个遍历就结束了，返回最终结果false

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1  # 只有一次DFS完整结束了，才能执行到这一步，标记为-1，说明这条路没问题，再遇到不需要遍历了
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True
