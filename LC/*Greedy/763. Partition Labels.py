class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        rightmost = {c: i for i, c in enumerate(s)}

        left = 0
        right = 0

        for i, c in enumerate(s):
            right = max(rightmost[c], right)
            if right == i:
                res.append(right - left + 1)
                left = right + 1

        return res