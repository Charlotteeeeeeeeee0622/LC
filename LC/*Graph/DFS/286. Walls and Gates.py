class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def dfs(i, j, rooms):
            # rooms[i][j] not an obstacle and rooms[i][j]
            if i >= 1 and rooms[i - 1][j] > 0 and rooms[i][j] + 1 < rooms[i - 1][j]:
                rooms[i - 1][j] = rooms[i][j] + 1
            if j >= 1 and rooms[i][j - 1] > 0 and rooms[i][j] < rooms[i][j - 1]:
                rooms[i][j - 1] = rooms[i][j] + 1
            if i + 1 < len(rooms) and rooms[i + 1][j] > 0 and rooms[i + 1][j] > rooms[i][j]:
                rooms[i + 1][j] = rooms[i][j] + 1
            if j + 1 < len(rooms) and rooms[i][j + 1] and rooms[i][j + 1] > rooms[i][j]:
                rooms[i][j + 1] = rooms[i][j] + 1

        q = []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                # empty
                if rooms[r][c] == 0:
                    q.append((r, c))
                    while q:
                        i, j = q.pop()
                        dfs(i, j, rooms)