class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = [0] * len(edges)

        for i, l in enumerate(edges):
            score[l] += i

        high = max(score)

        for i, s in enumerate(score):
            if high == s:
                return i


