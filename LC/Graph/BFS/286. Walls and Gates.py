def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    queue = collections.deque()
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                queue.append((i, j, 0))
    while queue:
        i, j, steps = queue.popleft()
        for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            dii = i + di
            djj = j + dj
            if 0 <= dii < len(rooms) and 0 <= djj < len(rooms[0]) and rooms[dii][djj] == 2147483647:
                rooms[dii][djj] = steps + 1
                queue.append((dii, djj, steps + 1))