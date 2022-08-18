# ——————————————Solution1————————————————
# https://leetcode.cn/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/327718/
class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_max=right_max=0
        ans=0
        while left<=right:
            if left_max<right_max:
                ans+=max(0,left_max-height[left])
                left_max=max(left_max,height[left])
                left+=1
            else:
                ans+=max(0,right_max-height[right])
                right_max=max(right_max,height[right])
                right-=1
        return ans

# ——————————————Solution2————————————————
def trap(self, height: List[int]) -> int:
    if not height or len(height) < 3:
        return 0
    volume = 0
    left, right = 0, len(height) - 1
    left_max = height[0]
    right_max = height[-1]
    while left < right:
        left_max = max(height[left],left_max)
        right_max = max(height[right],right_max)
        if left_max > right_max:
            volume += right_max - height[right]
            right -= 1
        else:
            volume += left_max - height[left]
            left += 1
    return volume
# ——————————————Solution3————————————————

class Solution:
    class Solution:
        def wallsAndGates(self, rooms: List[List[int]]) -> None:
            q = []

            for row in range(len(rooms)):
                for col in range(len(rooms[0])):
                    # empty
                    if rooms[row][col] == 0:
                        # 第一个0坐标
                        q.append((row, col))
                        # queue
                        while q:
                            i, j = q.pop()
                            #
                            self.calc_dist(i, j, q, rooms)

                    # tuple

        def calc_dist(self, i: int, j: int, q: deque, rooms: List[List[int]]) -> None:
            # not obstacle and room-1 is empty
            if i - 1 >= 0 and rooms[i - 1][j] > 0 and rooms[i][j] + 1 < rooms[i - 1][j]:
                # if could reach, append
                rooms[i - 1][j] = rooms[i][j] + 1
                # 坐标
                q.append((i - 1, j))

            if i + 1 < len(rooms) and rooms[i + 1][j] > 0 and rooms[i][j] + 1 < rooms[i + 1][j]:
                rooms[i + 1][j] = rooms[i][j] + 1
                q.append((i + 1, j))

            if j - 1 >= 0 and rooms[i][j - 1] > 0 and rooms[i][j] + 1 < rooms[i][j - 1]:
                rooms[i][j - 1] = rooms[i][j] + 1
                q.append((i, j - 1))
            if j + 1 < len(rooms[0]) and rooms[i][j + 1] > 0 and rooms[i][j] + 1 < rooms[i][j + 1]:
                rooms[i][j + 1] = rooms[i][j] + 1
                q.append((i, j + 1))
# ——————————————Solution4————————————————
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

# https://leetcode.cn/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/