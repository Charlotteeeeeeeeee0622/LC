class Leaderboard:

    def __init__(self):
        self.arr = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.arr[playerId] += score

    def top(self, K: int) -> int:
        return sum(score for playerId, score in self.arr.most_common(K))

    def reset(self, playerId: int) -> None:
        self.arr[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)