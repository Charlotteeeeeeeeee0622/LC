from collections import defaultdict

if __name__ == '__main__':
    x=defaultdict(bool)
    y=defaultdict(list)
    print(x)
    print(y)


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