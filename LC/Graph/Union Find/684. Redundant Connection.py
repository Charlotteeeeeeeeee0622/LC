class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        leader = [i for i in range(len(edges) + 1)]
        res = []

        def findleader(leader, node):
            while node != leader[node]: node = leader[node]
            return node

        for edge in edges:

            rootl = findleader(leader, edge[0])
            rootr = findleader(leader, edge[1])

            if rootl != rootr:
                leader[rootl] = rootr

            else:
                res = edge
                return res


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.already_connected = defaultdict(list)
        for edge in edges:
            self.visited = defaultdict(bool)
            x, y = edge[0], edge[1]
            if self.is_already_connected(x, y):
                return edge
            self.already_connected[x].append(y)
            self.already_connected[y].append(x)

    def is_already_connected(self, x, y):
        if x == y:
            return True
        # 遍历x的所有邻居
        for x_adjacent in self.already_connected[x]:
            # 没有visit
            if not self.visited[x_adjacent]:
                self.visited[x_adjacent] = True
                if self.is_already_connected(x_adjacent, y):
                    return True
        return False
