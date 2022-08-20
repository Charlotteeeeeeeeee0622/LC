class Solution:
    def findOrder(self, nc: int, pre: List[List[int]]) -> List[int]:

        def findcircle(c, premap, visited, res):
            # exists a circle
            if visited[c] == 2:
                return True

            # searching
            if visited[c] == 1:
                return False

            # mark as visited
            visited[c] = 2

            for precrs in premap[c]:
                if findcircle(precrs, premap, visited, res):
                    return True

            visited[c] = 1

            res.append(c)

            return False

        # if prerequisite==0
        lenc = len(pre)
        if lenc == 0:
            return [i for i in range(nc)]

        # prerequisite map
        premap = [set() for _ in range(nc)]
        for second, first in pre:
            premap[second].add(first)

        # mark if the position is visited
        visited = [0 for _ in range(nc)]

        res = []
        for c in range(nc):
            if findcircle(c, premap, visited, res):
                return []

        return res
