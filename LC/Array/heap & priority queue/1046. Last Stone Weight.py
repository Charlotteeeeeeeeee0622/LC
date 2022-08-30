class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            # 最先弹出的是最小的数字
            first_stone = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)

            if first_stone < second_stone:
                heapq.heappush(stones, first_stone - second_stone)

        # 防止最后俩一样大抵消了
        stones.append(0)
        return -stones.pop(0)