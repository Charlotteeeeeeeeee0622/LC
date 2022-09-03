class Solution:

    # round one
    def __init__(self, w: List[int]):
        self.dp = [0] * (len(w))
        for i in range(len(w)):
            self.dp[i] = self.dp[i - 1] + w[i]

    def pickIndex(self) -> int:
        randint = random.randint(1, self.dp[-1])
        l, r = 0, len(self.dp) - 1
        while l < r:
            mid = (l + r) // 2
            if self.dp[mid] >= randint:
                r = mid
            else:
                l = mid + 1
        return r

from bisect import bisect_left
class Solution:

    # round two
    def __init__(self, w: List[int]):
        self.dp = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        randint = random.randint(1, self.dp[-1])
        return bisect_left(self.dp,randint)