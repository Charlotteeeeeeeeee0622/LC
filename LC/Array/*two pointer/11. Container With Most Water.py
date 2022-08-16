def maxArea(self, height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    cnt = 0
    res = 0
    while i < j:
        cnt = min(height[i], height[j]) * (j - i)
        res = max(res, cnt)
        if height[i] < height[j]:
            i += 1
        elif height[i] >= height[j]:
            j -= 1
    return res